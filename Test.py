status=input("You want to sell or buy a car ? \n")
if (status=="sell"):
    nameof =input("May you enter your Car name? ,Please! \n")
    typeof =input("Your car's type \n")
    colorof=input("Car's color \n")
    input_details=list([nameof, typeof ,colorof])
    print(f"{input_details} is this your Cars Details ")
        
else:
    print("sorry we dont buy cars ATM")
    

