from django.urls import path

from wrestling_sorted import views

urlpatterns = [
    path(
        'api/v1/tv_shows/<int:tv_show_id>/episode/<str:episode_date>/highlights/',
        views.highlights,
        name='tv_shows_highlights'
    ),
]
