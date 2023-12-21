from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from wrestling_sorted.services.highlights import Highlights


@api_view(["GET"])
def list_shows_highlights(request):
    """
    List the shows highlights.
    """
    shows_highlights = Highlights()
    highlights = shows_highlights.retrieve()

    response = {
        "status": 'success',
        "message": 'Highlights retrieved successfully',
        "data": highlights
    }
    return Response(response, status=status.HTTP_200_OK)
