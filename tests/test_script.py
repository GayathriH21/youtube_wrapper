from youtube_wrapper.youtube_data import YouTubeDataAPI
from youtube_wrapper.youtube_transcript import YouTubeTranscriptAPI

# Replace with your API key and video ID
api_key = 'YOUR_ACTUAL_YOUTUBE_API_KEY'
video_id = 'YOUR_ACTUAL_VIDEO_ID'


# Initialize the APIs
data_api = YouTubeDataAPI(api_key)
transcript_api = YouTubeTranscriptAPI()

# Fetch video details
try:
    video_details = data_api.get_video_details(video_id)
    print("Video Details:")
    print(f"Title: {video_details['items'][0]['snippet']['title']}")
    print(f"Description: {video_details['items'][0]['snippet']['description']}")
    print(f"View Count: {video_details['items'][0]['statistics']['viewCount']}")
except Exception as e:
    print(f"Error fetching video details: {e}")

# Fetch video transcript
try:
    transcript = transcript_api.get_transcript(video_id)
    print("\nTranscript:")
    for entry in transcript:
        print(f"{entry['start']:.2f}s: {entry['text']}")
except Exception as e:
    print(f"Error fetching transcript: {e}")
