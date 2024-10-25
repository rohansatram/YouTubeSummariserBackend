import google.generativeai as genai

# Summarize text
def follow_up(transcript, question):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"This is the transcript of the YouTube video. \n\n{transcript}. The user has a question about the contents of the video, the question is: {question}. Your response must be of the following format:[answer to user's question][which second of the video relates to the user's question]. Your response must always end with a number which is in seconds, end your response with just this number as an integer, without a period after it, which answer's the user's question."
    response = model.generate_content(prompt)

     # Extract summary out of response
    summary = response.candidates[0].content.parts[0].text
    return summary