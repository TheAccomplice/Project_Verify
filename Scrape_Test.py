import os
import requests
from bs4 import BeautifulSoup

# URL of the news article
url = input("Url:")

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
folder = "Articles"
os.makedirs(folder, exist_ok=True)  # Ensure the folder exists
safe_title = "".join(c for c in title_text if c.isalnum() or c in (' ', '_')).rstrip()
filename = os.path.join(folder, f"{safe_title[:101]}.txt")  # File path under folder

# Save to local file
with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"Title: {title_text}\n\n")
    f.write(content)

print(f"Article saved as '{filename}'")