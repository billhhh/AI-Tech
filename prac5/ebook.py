from urllib import request
from nltk import word_tokenize

url = "http://www.gutenberg.org/cache/epub/174/pg174.txt"
req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})

response = request.urlopen(req)
raw = response.read().decode('utf-8')
print('Number of characters: ', len(raw))
print('First Line: ', raw[:75])
tokens = word_tokenize(raw)
print('Number of tokens: ', len(tokens))
print('First 20 tokens: ', tokens[:20])
