from googleapiclient.discovery import build

class YouTubeDataAPI:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_details(self, video_id):
        request = self.youtube.videos().list(part='snippet,statistics', id=video_id)
        response = request.execute()
        return response

    def search_videos(self, query, max_results=5):
        request = self.youtube.search().list(part='snippet', q=query, maxResults=max_results)
        response = request.execute()
        return response

    def list_channel_videos(self, channel_id):
        request = self.youtube.search().list(part='snippet', channelId=channel_id, maxResults=20)
        response = request.execute()
        return response

