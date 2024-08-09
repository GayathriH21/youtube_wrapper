from .youtube_data import YouTubeDataAPI
from .youtube_transcript import YouTubeTranscriptAPI

class YouTubeAPIWrapper:
    def __init__(self, api_key):
        self.data_api = YouTubeDataAPI(api_key)
        self.transcript_api = YouTubeTranscriptAPI()

    def get_video_details_with_transcript(self, video_id):
        details = self.data_api.get_video_details(video_id)
        transcript = self.transcript_api.fetch_transcript(video_id)
        return {"details": details, "transcript": transcript}

