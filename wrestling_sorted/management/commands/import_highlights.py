from django.core.management.base import BaseCommand

from wrestling_sorted import settings
from wrestling_sorted.models import Episode, Highlight, Show
from wrestling_sorted.services.highlights import Highlights


class Command(BaseCommand):
    help = 'Import highlights from YouTube.'

    def handle(self, *args, **options):

        # TODO: determine the actual date of the episode and use that as the episode_date
        # TODO: handle the edge case where we get private videos
        # TODO: handle the edge case where we have one video publish on a day
        # TODO: print summary of report
        # TODO: record summary of report in the database

        show = Show.objects.get(id=1)

        # Save the episodes and highlights
        for episode_date, highlights in self.get_grouped_highlights():
            for i, highlight in enumerate(highlights, start=1):
                # Save episode
                episode = Episode.objects.create_if_not_exists(
                    show=show,
                    episode_date=episode_date,
                    latest_episode=False
                )

                # Save highlight
                Highlight.objects.create_if_not_exists(
                    title=highlight['title'],
                    show=show,
                    video_url=highlight['url'],
                    episode=episode
                )

                print(f"  {i}. {highlight['title']} - {highlight['url']}")

        self.stdout.write(self.style.SUCCESS('Successfully ran your script'))

    @staticmethod
    def get_grouped_highlights():
        highlights = Highlights(
            settings.YOUTUBE_API_KEY,
            settings.MONDAY_NIGHT_RAW_PLAYLIST_ID,
            settings.MAX_ITEMS_TO_PARSE
        )
        highlights.get().group_by_episode()
        return highlights.get_grouped_by_episode().items()
