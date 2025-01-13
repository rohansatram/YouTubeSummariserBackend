from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import os
import re
from dotenv import load_dotenv
from summarise import *
from get_video_id import *
from follow_up_question import *
from print_url import *

load_dotenv()

# Add and configure your gemini API key here
os.environ['GOOGLE_API_KEY'] = os.getenv('API_KEY')
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


def main(url):
    global video_id 
    video_id = get_yt_vid_url(url)
    global transcript 
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    link = print_url(transcript, video_id, 0)
    r = requests.get(f"https://www.youtube.com/watch?v={video_id}")
    soup = BeautifulSoup(r.text, features="html.parser")
    bs = soup.find_all(name="title")[0]
    title = bs.text
    video_title = title[0:-10]
    return summarise(transcript), link, video_id, video_title

def question(question):
# Allows the user to ask a follow-up question
    global video_id
    global transcript
    follow_up_summary = follow_up(transcript, question)
    link = print_url(follow_up_summary, video_id, 1)

    follow_up_summary = follow_up_summary.strip()

    if '.' in follow_up_summary:
        last = follow_up_summary.rfind('.')
        follow_up_summary = follow_up_summary[:last + 1]
        return follow_up_summary, link

    return follow_up_summary, link