from django.urls import path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from wrestling_sorted import views

urlpatterns = [
    path(
        'api_schema',
        get_schema_view(title='API Schema', description='Guide for the REST API'),
        name='api_schema'
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "api_schema"},
        ),
        name="docs",
    ),
    path(
        'v1/tv_shows/<int:tv_show_id>/episode/<str:episode_date>/highlights/',
        views.highlights,
        name='tv_shows_highlights'
    ),
]
