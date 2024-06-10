import re
text="Regular Expression are a powerful tool for text processing.They can be used for pattern matching."
word_pattern=r'\w+'
words=re.findall(word_pattern,text)
print(words)
