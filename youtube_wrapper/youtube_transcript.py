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
    def fetch_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return transcript
        except TranscriptsDisabled:
            return "Transcript is disabled for this video."

    def fetch_transcript_in_language(self, video_id, language_code):
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        return transcript        
