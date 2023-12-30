from django.core.management.base import BaseCommand

from wrestling_sorted import settings
from wrestling_sorted.models import Episode, Highlight, TvShow
from wrestling_sorted.services.highlights import Highlights


class Command(BaseCommand):
    help = 'Import highlights from YouTube.'

    def add_arguments(self, parser):
        # Add command line arguments
        parser.add_argument('--tv_show_id', type=str, help='TV Show ID', required=True)
        parser.add_argument('--max_items_to_parse', type=int, help='Maximum number of items to parse', required=True)

    def handle(self, *args, **options):
        # Get command line arguments or use default values
        playlist_id = options['tv_show_id']
        max_items_to_parse = options['max_items_to_parse']

        # Get the tv show
        tv_show = TvShow.objects.get(id=playlist_id)

        # Get grouped highlights
        grouped_highlights = self.get_grouped_highlights(
            playlist_id=tv_show.playlist_id,
            max_items_to_parse=max_items_to_parse
        )

        # Save the episodes and highlights
        for episode_date, highlights in grouped_highlights:
            for i, highlight in enumerate(highlights, start=1):
                # Save episode
                episode = Episode.objects.create_if_not_exists(
                    tv_show=tv_show,
                    episode_date=episode_date
                )

                # Save highlight
                Highlight.objects.create_if_not_exists(
                    title=highlight['title'],
                    tv_show=tv_show,
                    url=highlight['url'],
                    thumbnail_default=highlight['thumbnail_default'],
                    thumbnail_medium=highlight['thumbnail_medium'],
                    thumbnail_high=highlight['thumbnail_high'],
                    thumbnail_maxres=highlight['thumbnail_maxres'],
                    episode=episode
                )

        self.stdout.write(self.style.SUCCESS('Successfully ran your script'))

    @staticmethod
    def get_grouped_highlights(playlist_id, max_items_to_parse):
        highlights = Highlights(settings.YOUTUBE_API_KEY, playlist_id, max_items_to_parse)
        highlights.get_all().group_by_episode()
        return highlights.get_grouped_by_episode().items()
