from django.http import JsonResponse
from rest_framework.decorators import api_view

from wrestling_sorted.models import Highlight, Episode
from wrestling_sorted.serializers import HighlightSerializer


@api_view(['GET'])
def highlights(request, tv_show_id, episode_date):
    """
    List all highlights for given episode of a TV show.
    """
    if request.method == 'GET':
        episode = Episode.objects.get(tv_show_id=tv_show_id, episode_date=episode_date)
        tv_show = episode.tv_show
        highlights = Highlight.objects.filter(tv_show_id=tv_show_id, episode=episode)
        serializer = HighlightSerializer(highlights, many=True)

        # Construct payload
        payload = {
            "tv_show": tv_show.name,
            "episode_date": episode_date,
            "total_highlights": serializer.data.__len__(),
            "highlights": serializer.data,
        }

        return JsonResponse(payload, safe=False)
