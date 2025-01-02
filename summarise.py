import google.generativeai as genai
# Summarize text

def summarise(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"You are an expert text summarizer. Summarize the following text with important details and keep the length to less than 1000 words:\n\n{text}"
    response = model.generate_content(prompt)

     # Extract summary out of response
    summary = response.candidates[0].content.parts[0].text
    return summary