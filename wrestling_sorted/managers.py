from django.db import models


class EpisodeManager(models.Manager):
    def create_if_not_exists(self, show, episode_date, latest_episode=False) -> models.Model:
        try:
            # Try to get the existing episode
            return self.get(show=show, episode_date=episode_date)
        except self.model.DoesNotExist:
            # If the episode doesn't exist, create it
            return self.create(
                show=show,
                episode_date=episode_date,
                latest_episode=latest_episode
            )


class HighlightManager(models.Manager):
    def create_if_not_exists(self, title, show, url, episode):
        try:
            # Try to get the existing highlight
            return self.get(url=url, episode=episode)
        except self.model.DoesNotExist:
            # If the highlight doesn't exist, create a new one
            return self.create(
                title=title,
                show=show,
                url=url,
                episode=episode
            )
