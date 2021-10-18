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


# (3)
passwords = ['my_p8ss-w0rd', 'my_p8ss-w0rdmy_p8ss-w0rdmy_p8ss-w0rd' , 'aaaaaaaaaaa', '22222222222', '____________', '$asd123_']

#pattern = re.compile(r"^[a-z0-9_-]{6,18}$")
pattern = re.compile(r"[a-z0-9_-]{6,18}")

print ("========match/search========")
for pwd in passwords:
    t = re.match(pattern,pwd)
    if (t):
        print(t.group(0))
    else:
        print("Not match \"%s\"" % pwd)
