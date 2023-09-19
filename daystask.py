def calculations():
    try:
        days= int(input("Please Enter Your Days you want to convert! \n"))
        if (days>0):
            unit=input("Minutes(m) or Hours(h) \n")
            days_to_hours = days*24
            days_to_minutes=days*24*60
            if (unit == "m") or (unit == "M"):
                print(f"{days} will be {days_to_minutes} Minutes ! \n")
            elif (unit == "h") or (unit == "H"):
                print(f"{days} will be {days_to_hours } Hours ! \n")
            else:
                print("Wrong Entry!")
        else:
             print("Please you have entered a Invalid Number")
    except ValueError:
         print("Wrong Entry!")         
status=input("To procced press enter ,to close app type 'n or anything' and press enter \n")
while (status!="n"):
    calculations()
else:
    print("Thanks for Using Conversion App !!")
    