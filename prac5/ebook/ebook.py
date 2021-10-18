from urllib import request
import nltk
from nltk import word_tokenize

# url = "http://www.gutenberg.org/cache/epub/174/pg174.txt"
url = "https://raw.githubusercontent.com/billhhh/AI-Tech/master/prac5/ebook/pg174.txt"

nltk.download('punkt')

response = request.urlopen(url)
# raw = response.read().decode('utf-8')
raw = response.read().decode('utf-8-sig')
print('Number of characters: ', len(raw))
print('First Line: ', raw[:75])
tokens = word_tokenize(raw)
print('Number of tokens: ', len(tokens))
print('First 20 tokens: ', tokens[:20])
