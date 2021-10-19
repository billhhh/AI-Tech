# ex1 (1)

import re

# line = "Matches bat, bet, bit, bot and but Also matches cricket bat, bitter lemon bppt"
#
# pattern = re.compile(r'b[aeiou]t')
# result = pattern.findall(line)
# print ("========match bat========")
# print(result)


# (2)
line = "batman"
line2 = "cricket bat"

print(line.find('man'))

# anchor our patterns to the beginning and ends of lines using ^ and $ respectively (or \A and \Z for multiline strings)
# pattern = re.compile(r'^b[a-z0-9_-]{6,18}')
# result = pattern.findall(line)
# print ("========anchors========")
# print(result)
# result = pattern.findall(line2)
# print(result)


# (3)
# passwords = ['my_p8ss-w0rd', 'my_p8ss-w0rdmy_p8ss-w0rdmy_p8ss-w0rd\t' , 'aaaaaaaaaaa', '22222222222', '____________', '$asd123_']
# # pattern = re.compile(r"\d")
# # pattern = re.compile(r"[0-9]")
# # pattern = re.compile(r"[A-Za-z0-9_]")
# pattern = re.compile(r"\s")
# # pattern = re.compile(r"[ \t\r\n\f]")
#
# print ("========shorthand character========")
# for pwd in passwords:
#     result = pattern.findall(pwd)
#     print(result)


# (4)
# pattern = re.compile(r"^[a-z0-9_-]{6,18}$")
# # pattern = re.compile(r"[a-z0-9_-]{6,18}")
#
# print ("========match/search========")
# for pwd in passwords:
#     t = re.match(pattern, pwd)
#     if (t):
#         print(t.group(0))
#     else:
#         print("Not match \"%s\"" % pwd)
