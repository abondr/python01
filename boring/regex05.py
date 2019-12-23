import re
xmasRegex = re.compile(r'(\d+)\s+(\w+)')
string1 = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese,' +\
    ' 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
list1 = xmasRegex.findall(string1)
print(list1)
print("--------------------------")
nameString = 'First Name: Al Last Name: Sweigart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search(nameString)
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print("----------------------163----")
