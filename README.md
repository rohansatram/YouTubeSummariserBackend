Watching entire YouTube videos can be time-consuming.

The goal is to build a system that summariser videos and to take you to the relevant part of the video.

YouTubeTranscriptApi is used to fetch the transcript of a YouTube video based on the video ID.

google.generativeai is used to access Google's gemini models, which are capable of accurately summarising videos.

Flask was used to build APIs.

How to install:

1. Install the required libraries using pip install -r requirements.txt
2. Add your api key in the ".env_example" file and rename it to ".env"
3. run app.py (make sure you have the front-end: https://github.com/RohanSatram/YouTubeSummariserFrontend)
