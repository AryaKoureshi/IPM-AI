# Step 0: Imports
import re
from collections import Counter
from docx import Document

# Step 1: Read the Office Word file
document = Document('doc.docx')
content = document.paragraphs[0].text

# Step 2: Text Processing
processed_text = re.sub(r'[^\w\s]', '', content)  # Remove special characters
processed_text = processed_text.lower()          # Convert text to lowercase

# Step 3: Extract Unique Words
unique_words = set(processed_text.split())

# Step 4: Count Word Occurrences
word_occurrences = Counter(processed_text.split())

# Step 5: Sort Words by Occurrences
sorted_words = sorted(unique_words, key=lambda word: word_occurrences[word], reverse=True)


# Step 6: Print the Ten Most Repeated Words
print("Ten most repeated words:")
for word in sorted_words[:10]:
    print(f"{word}: {word_occurrences[word]}")

# Step 7: Save Unique Words to a Text File
output_file_path = "unique_words.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for word in unique_words:
        output_file.write(word + '\n')
