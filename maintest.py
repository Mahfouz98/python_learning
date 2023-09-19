def calculations():
    try:
        days= int(input("Please Enter Your Days you want to convert! \n"))
        if (days>0):
            unit=input("Minutes(m) or Hours(h) \n")
            if (unit == "m") or (unit == "M"):
                days_to_minutes=days*24*60
                print(f"{days} will be {days_to_minutes} Minutes ! \n")
            elif (unit == "h") or (unit == "H"):
                days_to_hours = days*24
                print(f"{days} will be {days_to_hours } Hours ! \n")
            else:
                #TODO: tekhaly hena yermy exception 3shan yeb2a nafs el error byt-handl mn etnan same enha nafs el moshkela
                raise ValueError
        else:
            raise ValueError
    except ValueError:
         print("Wrong Entry!")         

#TODO: dah awl mara bas fa shof haga esmha do while in python
status=input("To procced press enter ,to close app type 'n or anything' and press enter \n")
while (status!="n"):
    calculations()
else:
    print("Thanks for Using Conversion App !!")