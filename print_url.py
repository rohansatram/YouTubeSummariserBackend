import re

# Print URL which is related to the follow-up question
def print_url(summary, id, count):
    if count == 0:
      return f"https://www.youtube.com/embed/{id}"
    pattern = r'(\d+)\s*$'
    match = re.search(pattern, summary)
    if match:
      number = match.group(1)
      return f"https://www.youtube.com/embed/{id}?start={number}"
    else:
       return f"https://www.youtube.com/embed/{id}"