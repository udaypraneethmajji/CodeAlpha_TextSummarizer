import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

# Download once
nltk.download('punkt')
nltk.download('stopwords')

text = input("Enter paragraph:\n")

# Tokenize
words = word_tokenize(text.lower())
stop_words = set(stopwords.words("english"))

# Word frequency
freq = defaultdict(int)
for word in words:
    if word not in stop_words:
        freq[word] += 1

# Sentence scoring
sentences = sent_tokenize(text)
sentence_scores = {}

for sent in sentences:
    for word in word_tokenize(sent.lower()):
        if word in freq:
            sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]

# Get top sentences
summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

print("\nSummary:")
for s in summary:
    print(s)