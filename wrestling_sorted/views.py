from django.core.paginator import Paginator
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
        # Get episode
        episode = Episode.objects.get(tv_show_id=tv_show_id, episode_date=episode_date)

        # Get highlights
        highlights = Highlight.objects.filter(tv_show_id=tv_show_id, episode=episode)

        # Paginate highlights
        page_number = request.GET.get("page", 1)
        paginator = Paginator(highlights, per_page=15)
        page_object = paginator.get_page(page_number)
        serializer = HighlightSerializer(page_object, many=True)

        # Construct payload
        payload = {
            "page": {
                "current": page_object.number,
                "total": paginator.num_pages,
            },
            "highlights": {
                "total": paginator.count,
                "results": serializer.data,
            }
        }

        return JsonResponse(payload, safe=False)
