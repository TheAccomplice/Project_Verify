import requests
from bs4 import BeautifulSoup

# URL of the news article
url = "https://www.channelnewsasia.com/singapore/ge2025-singapore-election-pap-pm-lawrence-wong-strong-mandate-5107136"

# Send HTTP GET request
response = requests.get(url)
response.raise_for_status()

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract title
title = soup.find('h1') or soup.title
title_text = title.get_text(strip=True) if title else "Untitled Article"

# Extract content
article_body = soup.find('div', class_='article-body') or soup.find('article') or soup
paragraphs = article_body.find_all('p') if article_body else []
content = "\n".join(p.get_text(strip=True) for p in paragraphs)

# Filename-safe title (remove problematic characters)
safe_title = "".join(c for c in title_text if c.isalnum() or c in (' ', '_')).rstrip()
filename = f"{safe_title[:101]}.txt"  # limit to 101 characters

# Save to local file
with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"Title: {title_text}\n\n")
    f.write(content)

print(f"Article saved as '{filename}'")