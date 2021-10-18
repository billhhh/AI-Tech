# ex1

import re

line = "Matches bat, bet, bit, bot and but Also matches cricket bat, bitter lemon"

matchObj = re.match(r'b[aeiou]t', line)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
