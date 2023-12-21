import googleapiclient.discovery

from wrestling_sorted import settings


class Highlights:
    def __init__(self, api_key: str, playlist_id: str, max_results: int):
        self.playlist_items: dict = 0
        self.grouped_by_episode: dict = 0
        self.api_key = api_key
        self.playlist_id = playlist_id
        self.max_results = max_results

        pass

    def get(self):
        if not settings.YOUTUBE_API_KEY:
            print("Please set your YouTube API key in the script.")
        else:
            return self.get_youtube_playlist_videos()

    def get_youtube_playlist_videos(self) -> 'Highlights':
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=self.api_key)

        # Retrieve the playlist items
        self.playlist_items = youtube.playlistItems().list(
            part="snippet",
            playlistId=self.playlist_id,
            maxResults=self.max_results
        ).execute()

        return self

    def group_by_episode(self) -> 'Highlights':
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

        self.grouped_by_episode = highlights_by_episode

        return self

    def get_grouped_by_episode(self) -> dict:
        return self.grouped_by_episode
