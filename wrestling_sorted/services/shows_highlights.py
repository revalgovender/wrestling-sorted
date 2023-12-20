import googleapiclient.discovery

from wrestling_sorted import settings


class ShowsHighlights:
    def __init__(self):
        pass

    # Set your YouTube API key
    API_KEY = settings.YOUTUBE_API_KEY

    # Set the playlist ID
    PLAYLIST_ID = "PLF0CB8E7B4C77DB61"

    # Set the number of videos to retrieve
    MAX_RESULTS = 50

    def retrieve(self):
        if not self.API_KEY:
            print("Please set your YouTube API key in the script.")
        else:
            return self.get_youtube_playlist_videos(self.API_KEY, self.PLAYLIST_ID, self.MAX_RESULTS)

            # Print the organized videos
            # for episode_date, videos in videos_by_episode.items():
            #     print(f"{episode_date}:")
            #     for i, video in enumerate(videos, start=1):
            #         print(f"  {i}. {video['title']} - {video['url']}")

    def get_youtube_playlist_videos(self, api_key: str, playlist_id: str, max_results: int) -> dict:
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

        # Retrieve the playlist items
        playlist_items = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=max_results
        ).execute()

        # Organize videos by episode date
        videos_by_episode = {}

        for item in playlist_items["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]
            video_title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            episode_date = item["snippet"]["publishedAt"]
            episode_date = episode_date.split("T")[0]

            if episode_date:
                if episode_date not in videos_by_episode:
                    videos_by_episode[episode_date] = []

                videos_by_episode[episode_date].append({
                    "id": video_id,
                    "title": video_title,
                    "url": video_url
                })

        return videos_by_episode
