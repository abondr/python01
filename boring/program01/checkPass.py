passWordFile = open("secretPass.txt")
secretPassword = passWordFile.read()
typedPassword = input("please enter password")
if typedPassword == secretPassword:
    print(" you may enter ")
else:
    print(" Wrong Password")
