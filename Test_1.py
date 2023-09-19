import datetime 

user_input=input("please enter your goal & deadline separated by a colon \n")
user_inputspl=user_input.split(":")
goal = user_inputspl[0]
date = user_inputspl[1]
deadline=(datetime.datetime.strptime(date,"%d.%m.%Y"))
now=datetime.datetime.today()
daysremaining=deadline - datetime.datetime.today()
print(f"{daysremaining} is remaining for your Goal {goal}")

