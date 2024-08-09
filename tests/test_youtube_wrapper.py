import pytest
from youtube_wrapper import YouTubeAPIWrapper

def test_get_video_details_with_transcript():
    wrapper = YouTubeAPIWrapper('YOUR_API_KEY')
    result = wrapper.get_video_details_with_transcript('YOUR_VIDEO_ID')
    assert 'details' in result
    assert 'transcript' in result

