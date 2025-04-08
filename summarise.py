import google.generativeai as genai
# Summarize text

def summarise(text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""You are an expert in text summarization. Create a concise summary of the following text that MUST:
    - Be STRICTLY under 150 words
    - Focus only on the most essential points
    - Use clear, simple language
    - Present information using bullet points (maximum 5-7 points)
    - Each bullet point should be 15-25 words maximum

    Text to summarize:
    {text}"""
    response = model.generate_content(prompt)

     # Extract summary out of response
    summary = response.candidates[0].content.parts[0].text
    return summary