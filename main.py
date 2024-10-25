from youtube_transcript_api import YouTubeTranscriptApi
import os
from summarise import *
from get_video_id import *
from follow_up_question import *
from print_url import *

# Add and configure your gemini API key here
os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
      
user_url = input("Enter a youtube URL: ")
video_id = get_yt_vid_url(user_url)

# Get transcript, contains time stamps 
transcript = YouTubeTranscriptApi.get_transcript(video_id)
summarise(transcript)

# Allows the user to ask a follop-up question
question = input("Enter a follow-up question: ")
follow_up_summary = follow_up(transcript, question)
print(follow_up_summary)

# Prints the URL which corresponds to the question the user asked
print_url(follow_up_summary, video_id)