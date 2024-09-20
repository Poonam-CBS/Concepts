def leap_year(inp_year):
    if (inp_year < 0):
        print("Please enter a positive value, year can not be negative")
    else:
        if (inp_year % 4 == 0):
            return True
        if (inp_year % 100 != 0):
            return True
        if (inp_year % 400 == 0):
            return True

inp_year=int(input("Enter the year: "))
if leap_year(inp_year):
    print(f"{inp_year} is a leap year")
else:
    print(f"{inp_year} is not a leap year")
