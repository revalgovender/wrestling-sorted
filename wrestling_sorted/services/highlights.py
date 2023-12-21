import googleapiclient.discovery

from wrestling_sorted import settings


class ShowsHighlights:
    def __init__(self):
        self.playlist_items: dict = 0
        self.sorted_by_episode: dict = 0

        pass

    def retrieve(self):
        if not settings.YOUTUBE_API_KEY:
            print("Please set your YouTube API key in the script.")
        else:
            return self.get_youtube_playlist_videos(
                settings.YOUTUBE_API_KEY,
                settings.MONDAY_NIGHT_RAW_PLAYLIST_ID,
                settings.MAX_ITEMS_TO_PARSE
            )

    def get_youtube_playlist_videos(self, api_key: str, playlist_id: str, max_results: int) -> 'ShowsHighlights':
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

        # Retrieve the playlist items
        self.playlist_items = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=max_results
        ).execute()

        return self

    def sort(self) -> 'ShowsHighlights':
        """
        Sort the videos by date.
        """
        highlights_by_episode = {}

        for item in self.playlist_items["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]
            video_title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            episode_date = item["snippet"]["publishedAt"]
            episode_date = episode_date.split("T")[0]

            if episode_date:
                if episode_date not in highlights_by_episode:
                    highlights_by_episode[episode_date] = []

                highlights_by_episode[episode_date].append({
                    "id": video_id,
                    "title": video_title,
                    "url": video_url
                })

        self.sorted_by_episode = highlights_by_episode

        return self

    def get_sorted_by_episode(self) -> dict:
        return self.sorted_by_episode
