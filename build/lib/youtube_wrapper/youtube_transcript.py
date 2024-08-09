from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

class YouTubeTranscriptAPI:
    def fetch_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return transcript
        except TranscriptsDisabled:
            return "Transcript is disabled for this video."

    def fetch_transcript_in_language(self, video_id, language_code):
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        return transcript

