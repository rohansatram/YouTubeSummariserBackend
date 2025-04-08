import google.generativeai as genai

# Summarize text
def follow_up(transcript, question):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""Given this YouTube video transcript: {transcript}
        For the question: {question}
            
    Instructions:
    - If the topic is not covered in the video, respond only with: 'The video does not cover this topic.'
    - If the topic is covered, provide a clear, direct answer based on the transcript content.
    - End your answer with a period ('.')
    - On the next line, provide only the integer timestamp (in seconds) where the relevant content begins
    - For partial matches, provide the relevant information that is covered
    - Do not include any extra phrases, headers, or time ranges
    - Do not use quotation marks or additional punctuation with the timestamp
    - Do not exceed 150 words
    
    Example format:
    The speed of light is 299,792 kilometers per second.
    145"""
    response = model.generate_content(prompt)

     # Extract summary out of response
    summary = response.candidates[0].content.parts[0].text
    return summary