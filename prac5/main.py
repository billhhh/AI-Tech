# ex1 (1)

import re

line = "Matches bat, bet, bit, bot and but Also matches cricket bat, bitter lemon"

pattern = re.compile(r'b[aeiou]t')
result = pattern.findall(line)
print(result)


# (2)
line = "batman"
line2 = "cricket bat"

# anchor our patterns to the beginning and ends of lines using ^ and $ respectively (or \A and \Z for multiline strings)
pattern = re.compile(r'^b[aeiou]t')
result = pattern.findall(line)
print(result)
result = pattern.findall(line2)
print(result)
