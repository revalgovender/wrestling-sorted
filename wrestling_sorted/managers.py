from django.db import models
from psycopg2 import IntegrityError


class EpisodeManager(models.Manager):
    def create_if_not_exists(self, show, episode_date, latest_episode=False) -> models.Model:
        try:
            # Try to get the existing episode
            episode = self.get(show=show, episode_date=episode_date)
        except self.model.DoesNotExist:
            # If the episode doesn't exist, create it
            episode = self.create(
                show=show,
                episode_date=episode_date,
                latest_episode=latest_episode
            )
        except IntegrityError:
            # Handle the case where multiple threads try to create the same episode simultaneously
            episode = self.get(show=show, episode_date=episode_date)

        return episode
