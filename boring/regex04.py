import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
string1 = 'Cell: 415-555-9999 Work: 212-555-0000'
mo1 = phoneNumRegex.search(string1)
print(mo1.group())
print("--------------------------")
phoneNumRegex.findall(string1)
mo2 = phoneNumRegex.findall(string1)
for i in range(0, len(mo2)):
    print(mo2[i])
print("--------------------------")
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})?')  # has groups
mo3 = phoneNumRegex.findall(string1)
print(mo3)
for i in range(0, len(mo3)):
    print(mo2[i])
print("--------------------------")
