from django.db import models

from wrestling_sorted.managers import EpisodeManager


class Show(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    episode_date = models.CharField(max_length=255, unique=True)
    latest_episode = models.BooleanField(default=False)

    objects = EpisodeManager()

    def __str__(self):
        return f"Episode {self.id} of {self.show.name}"


class Highlight(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    video_url = models.URLField()
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    def __str__(self):
        return f"Highlight {self.id}: {self.title} from {self.show.name}, Episode {self.episode.id}"
