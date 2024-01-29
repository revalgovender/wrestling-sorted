from django.http import JsonResponse
from rest_framework.decorators import api_view

from wrestling_sorted.models import Highlight, Episode
from wrestling_sorted.serializers import HighlightSerializer


@api_view(['GET'])
def highlights(request, tv_show_id, episode_date):
    """
    List all highlights for given episode of a TV show.
    """
    # Initialize data.
    response = {
        "status": "success",
    }
    tv_show_id = int(tv_show_id)

    # Retrieve highlights.
    if request.method == 'GET':
        try:
            episode = Episode.objects.get(tv_show_id=tv_show_id, episode_date=episode_date)
            tv_show = episode.tv_show
            highlights = Highlight.objects.filter(tv_show_id=tv_show_id, episode=episode)
            serializer = HighlightSerializer(highlights, many=True)
            response['data'] = {
                "tv_show": tv_show.name,
                "episode_date": episode_date,
                "total_highlights": serializer.data.__len__(),
                "highlights": serializer.data,
            }
        except Episode.DoesNotExist:
            response['status'] = "error"
            response['message'] = "Episode does not found."
            return JsonResponse(response, safe=False, status=404)
        except Highlight.DoesNotExist:
            response['status'] = "error"
            response['message'] = "Highlight does not found."
            return JsonResponse(response, safe=False, status=404)
        except Exception as e:
            response['status'] = "error"
            response['message'] = "Something went wrong."
            return JsonResponse(response, safe=False, status=500)

    return JsonResponse(response, safe=False)
