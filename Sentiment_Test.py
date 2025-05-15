from textblob import TextBlob

# Load the text file
with open('./Articles/GE2025 Clear and strong mandate for PAP will put Singapore in better position to face turbulent world[Cleaned].txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Analyze each line
for i, line in enumerate(lines, 1):
    blob = TextBlob(line)
    subjectivity = blob.sentiment.subjectivity
    classification = "Subjective" if subjectivity > 0.5 else "Objective"
    print(f"Line {i}: {classification} (Subjectivity: {subjectivity:.2f}) - {line.strip()}")
