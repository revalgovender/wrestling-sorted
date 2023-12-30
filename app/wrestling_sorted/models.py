from django.db import models

from wrestling_sorted.managers import EpisodeManager, HighlightManager


class TvShow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    playlist_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    tv_show = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    episode_date = models.CharField(max_length=255)

    objects = EpisodeManager()

    def __str__(self):
        return f"Episode {self.id} of {self.tv_show.name}"


class Highlight(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    tv_show = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    thumbnail_default = models.URLField(default=None, null=True)
    thumbnail_medium = models.URLField(default=None, null=True)
    thumbnail_high = models.URLField(default=None, null=True)
    thumbnail_maxres = models.URLField(default=None, null=True)

    objects = HighlightManager()

    def __str__(self):
        return f"Highlight {self.id}: {self.title} from {self.tv_show.name}, Episode {self.episode.id}"
