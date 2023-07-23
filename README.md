# IPM-AI
This repository contains quizzes and projects completed for the course "Artificial Intelligence" at IPM.
---
## Quiz

[Q1](https://github.com/AryaKoureshi/IPM-AI/blob/412e872a98575a8d7d76107d6078e72703a2da24/Python-Quiz/Q1.jpg)

---

[Q2](https://github.com/AryaKoureshi/IPM-AI/blob/601b6241931707eaf08f8e9d5deb057759b7fc56/Python-Quiz/Q2.jpeg)

---
[Q3,4](https://github.com/AryaKoureshi/IPM-AI/blob/601b6241931707eaf08f8e9d5deb057759b7fc56/Python-Quiz/Q3%264.png)

---
[Q5](IPM-AI/Python-Quiz)

[doc.docx](https://github.com/AryaKoureshi/IPM-AI/blob/601b6241931707eaf08f8e9d5deb057759b7fc56/Python-Quiz/Q5/doc.docx)

```
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
```
