""" This is a code to determine if a given yesr is a leap year or not. Although the code is simple and require simple if statement.
we will see how to use a function in a code and what are the elements of a fucntion.
First we will go over the logic: A year is a leap year if:
1. It is divisible by 4, but not divisible by 100, or
2. It is divisible by 400.
Here we start with a function with the parameter year and run a if statement requireing the condition 1 and 2 to be fulfilled
then we ask the user to enter a year as an input which then is stored in the variable year and then pass this argument while we call the function
and lastly we print the result"""
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
