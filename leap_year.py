#May the Force be with you!
"""This is a code to determine if a given year is a leap year or not.
Now to determine is if a given year is a leap year or not there are two criterias
1. The year should be divisible by 4 but not 100
2. The year should be divisible by 400"""
def leap_year(inp_year): #We start a function with the parameter int_year, this will be user input later
    if (inp_year < 0): # we check if the input is less than 0 (-ve) then we raise an error
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
