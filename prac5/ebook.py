from urllib import request
from nltk import word_tokenize

url = "http://www.gutenberg.org/cache/epub/174/pg174.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8')
print('Number of characters: ', len(raw))
print('First Line: ', raw[:75])
tokens = word_tokenize(raw)
print('Number of tokens: ', len(tokens))
print('First 20 tokens: ', tokens[:20])
