from urllib import request
from nltk import word_tokenize

''' a prefix u or U makes the strings a unicode string. 
Some applications insert a particular combination of bytes at the beginning of a file 
to indicate that the text contained in the file is Unicode. 

This combination of bytes is known as a signature or Byte Order Mark (BOM). 

Some applications - such as a text editor or a browser - will display the BOM as an extra 
line in the file, 
others will display unexpected characters

'''

#nltk.download('punkt')

url = "http://www.gutenberg.org/cache/epub/174/pg174.txt"

response = request.urlopen(url)
#raw = response.read().decode('utf-8')
raw = response.read().decode('utf-8-sig')
print('Number of characters: ', len(raw))
#print (raw)
print('First Line: ', raw[:75])
tokens = word_tokenize(raw)
print('Number of tokens: ', len(tokens))
print('First 20 tokens: ', tokens[:20])
