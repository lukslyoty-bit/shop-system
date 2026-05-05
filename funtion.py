def validated_and_check_year(year):
    if not isinstance(year,int):
        print (False, "invalid year, year must be an integer")
    if year <=0:
        print (False, "invalid year, year must be greater than 0")
    if year>9999:
        print(False, "invalid year, year must be <=9999")
    if year % 4==0 and year % 100!=0:
        print(True,f"year is a leap year")
    else:
        print(True, f"year is not a leap year")
while True:
    print("1. check the year")
    print("2. exit")

    choice=input("choose an option")
    if choice== "1":
        y=input("enter a year")
        if y. isdigit():
            print("validated_and_check_the_year(int(y))")
        else:
            print(False,"invalid year, year must be an integer")
    elif choice=="2":
        print("Good buy")
        break
    else:
        print("invalid option please try again")



