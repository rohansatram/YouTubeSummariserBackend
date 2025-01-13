import google.generativeai as genai

# Summarize text
def follow_up(transcript, question):
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    prompt = f"This is the transcript of a YouTube video: {transcript}. Based on this transcript, answer the user's question: {question}. If the question is unrelated to the video's content, respond: 'The video does not cover this topic.' Provide your response as a direct answer, without necessarily directly quoting the transcript, end your answer to the user's question with a period ('.'), then, the starting time in seconds where the relevant content begins, ending with an integer (rounded down, if applicable) and no punctuation following it. Do not include any extra phrases like 'Answer to the user's question' in your response. Do not provide a time range."
    response = model.generate_content(prompt)

     # Extract summary out of response
    summary = response.candidates[0].content.parts[0].text
    return summary