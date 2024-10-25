import re

# Get video_id, handle multiple types of URLs
def get_yt_vid_url(url):
  patterns = [
        r'youtu\.be/([a-zA-Z0-9_-]{11})',  # youtu.be format
        r'youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})'  # youtube.com format
    ]
    
  for pattern in patterns:
      match = re.search(pattern, url)
      if match:
          return match.group(1)