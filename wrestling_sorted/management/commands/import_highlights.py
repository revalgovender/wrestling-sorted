from django.core.management.base import BaseCommand

from wrestling_sorted.models import Episode, Highlight, Show
from wrestling_sorted.services.highlights import ShowsHighlights


class Command(BaseCommand):
    help = 'Import highlights from YouTube.'

    def handle(self, *args, **options):

        # TODO: add a check to see if the highlights have already been imported
        # TODO: determine the actual date of the episode and use that as the episode_date
        # TODO: handle the edge case where we get private videos
        # TODO: handle the edge case where we have one video publish on a day

        highlights = ShowsHighlights()
        highlights.retrieve().sort()
        sorted_highlights = highlights.get_sorted_by_episode()
        show = Show.objects.get(id=1)

        for episode_date, highlights in sorted_highlights.items():
            for i, highlight in enumerate(highlights, start=1):
                episode = Episode.objects.create_if_not_exists(
                    show=show,
                    episode_date=episode_date,
                    latest_episode=False
                )

                Highlight.objects.create(
                    title=highlight['title'],
                    show=show,
                    video_url=highlight['url'],
                    episode=episode
                )

                print(f"  {i}. {highlight['title']} - {highlight['url']}")

        self.stdout.write(self.style.SUCCESS('Successfully ran your script'))
