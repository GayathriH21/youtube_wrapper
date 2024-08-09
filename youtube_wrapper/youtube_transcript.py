from youtube_transcript_api import YouTubeTranscriptApi as YTTranscriptApi

class YouTubeTranscriptAPI:
    def __init__(self):
        self.api = YTTranscriptApi()

    def get_transcript(self, video_id):
        try:
            transcript = self.api.get_transcript(video_id)
            return transcript
        except Exception as e:
            return str(e)
