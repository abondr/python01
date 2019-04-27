print("1. kilo to pound ")
print("2. pound to kilo ")
converter = 0.453592
choise = int(input(" please enter choise "),10)
value = float(input(" now enter value to be converted "))
if choise == 1:
    print("{0} kilo is equal to {1} pound".format(value,(value*converter)))
elif choise == 2:
    print("{0} pound is equal to {1} kilo".format(value,(value / converter)))
else:
    print(" wrong option entered ")
