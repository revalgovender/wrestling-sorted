import googleapiclient.discovery
from datetime import datetime, timedelta
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

    def get_all(self):
        if not settings.YOUTUBE_API_KEY:
            print("Please set your YouTube API key in the script.")
        else:
            return self.get_all_youtube_playlist_videos()

    def get_youtube_playlist_videos(self) -> 'Highlights':
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=self.api_key)

        # Retrieve the playlist items
        playlist_response = youtube.playlistItems().list(
            part="snippet",
            playlistId=self.playlist_id,
            maxResults=self.max_results
        ).execute()
        self.playlist_items = playlist_response.get("items", [])

        return self

    def get_all_youtube_playlist_videos(self) -> 'Highlights':
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=self.api_key)

        next_page_token = None

        while True:
            # Retrieve the playlist items with the current page token
            playlist_response = youtube.playlistItems().list(
                part="snippet",
                playlistId=self.playlist_id,
                maxResults=self.max_results,
                pageToken=next_page_token
            ).execute()

            # Add or append the items to the list
            if self.playlist_items == 0:
                self.playlist_items = playlist_response.get("items", [])
            else:
                self.playlist_items.extend(playlist_response.get("items", []))

            # Check if there are more pages
            next_page_token = playlist_response.get("nextPageToken")

            # Break the loop if there are no more pages
            if not next_page_token:
                break

        return self

    def group_by_episode(self) -> 'Highlights':
        highlights_by_episode = {}

        for item in self.playlist_items:
            # Get the video ID, title, and URL
            video_id = item["snippet"]["resourceId"]["videoId"]
            video_title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            episode_date = self.get_episode_date(item["snippet"]["publishedAt"])

            # Skip highlights that are private
            if video_title == "Private video":
                continue

            # Skip highlights that were uploaded during the week
            if self.highlight_is_a_package_highlight(item["snippet"]["publishedAt"]):
                continue

            if episode_date:
                # Create a new episode if it doesn't exist
                if episode_date not in highlights_by_episode:
                    highlights_by_episode[episode_date] = []

                # Add the highlight to the episode
                highlights_by_episode[episode_date].append({
                    "id": video_id,
                    "title": video_title,
                    "url": video_url
                })

        self.grouped_by_episode = highlights_by_episode

        return self

    @staticmethod
    def get_episode_date(published_at: str) -> str:
        """Get the date the episode aired.

        WWE always publishes the highlights the day after the episode airs.
        We can therefore subtract one day from the published date to get the date the episode aired.

        """
        # Convert published date to a datetime object
        parsed_date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')

        # Subtract one day to get the date the episode aired
        new_date = (parsed_date - timedelta(days=1)).date()

        # Format the result back to the standard Postgres date field format
        return new_date.isoformat()

    @staticmethod
    def highlight_is_a_package_highlight(published_at: str) -> bool:
        """Rule to check if we need this highlight.

        On rare occasions, WWE will publish the highlights during the week when something important happens.
        WWE will publish a special highlight package for the one or two important segments/matches.
        We want to skip these highlights and only save the highlights for the full episode.
        We will use the day of the week to determine if the highlight is for the full episode or not.

        """
        # Convert published date to a datetime object
        parsed_date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')

        # Subtract one day to get the date the episode aired
        new_date = (parsed_date - timedelta(days=1)).date()

        if new_date.weekday() != 0:
            return True

        return False

    def get_grouped_by_episode(self) -> dict:
        return self.grouped_by_episode
