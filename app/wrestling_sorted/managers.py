from django.db import models


class EpisodeManager(models.Manager):
    def create_if_not_exists(self, tv_show, episode_date) -> models.Model:
        try:
            # Try to get the existing episode
            return self.get(tv_show=tv_show, episode_date=episode_date)
        except self.model.DoesNotExist:
            # If the episode doesn't exist, create it
            return self.create(
                tv_show=tv_show,
                episode_date=episode_date
            )


class HighlightManager(models.Manager):
    def create_if_not_exists(
            self,
            title,
            tv_show,
            url,
            thumbnail_default,
            thumbnail_medium,
            thumbnail_high,
            thumbnail_maxres,
            episode):
        try:
            # Try to get the existing highlight
            return self.get(url=url, episode=episode)
        except self.model.DoesNotExist:
            # If the highlight doesn't exist, create a new one
            return self.create(
                title=title,
                tv_show=tv_show,
                url=url,
                thumbnail_default=thumbnail_default,
                thumbnail_medium=thumbnail_medium,
                thumbnail_high=thumbnail_high,
                thumbnail_maxres=thumbnail_maxres,
                episode=episode
            )
