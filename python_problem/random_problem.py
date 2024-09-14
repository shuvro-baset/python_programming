"""
    input: aaaabbbccd
    output: 4a3b2c1d
"""

str1 = input("Enter Your String")
output = ''
# checked_item = []
# for ch in str1:
#     if ch not in checked_item:
#         count = str1.count(ch)
#         checked_item.append(ch)
#         output = output + str(count) + ch

char = str1[0]
count = 0
for ch in str1:
    if ch == char:
        char = ch
        count = count + 1
    else:
        output = output + str(count) + char
        count = 1
        char = ch

print(output)
