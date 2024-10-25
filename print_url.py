import re

# Print URL which is related to the follow-up question
def print_url(summary, id):
    pattern = r'(\d+)\s*$'
    match = re.search(pattern, summary)
    if match:
      number = match.group(1)
      print(f"https://www.youtube.com/watch?v={id}&t={number}s")