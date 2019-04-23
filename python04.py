import datetime
birth_year = input(" please enter your birth year ")

current_year = datetime.date.today().year

differnce = current_year - int(birth_year,10)
print("your age is {} years".format(differnce))