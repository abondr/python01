spam1 = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['apples', 'dog', 'tofu', 'cats']


def getList2Text(list1):
    textOutput = ""
    len1 = len(list1)
    if(len1 > 2):
        lastItem = list1[-1]
        firstItem = list1[0]
        for i in range(0, len1):
            if list1[i] == firstItem:
                textOutput += list1[i]
            elif list1[i] == lastItem:
                textOutput += " and "+list1[i]
            else:
                textOutput += " , "+list1[i]
    return textOutput


print(getList2Text(spam1))
print(getList2Text(spam2))
