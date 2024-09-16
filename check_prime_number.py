#Function to determine if a given number is a prime number or not
def check_prime(n):
    # first check is to see if the number is less than 2, if yes then it returns false since 1 is not a prime
    if n < 2:
        return False
    # Now check for factors from 2 to the square root of the numberi
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: #if remainder=0, then n is not a prime num, so it returns false
            return False
    return True #if it comes out of all of the above (retun false), then it is a prime num, hence returning true


number = int(input("Enter a number: ")) #asking for input from user and storing in number
if check_prime(number):    #calling check_prime with if statement, if true (prime)
    print(f"{number} is a prime number.")   #it will print number is prime
else:
    print(f"{number} is not a prime number.") #if not true (not a prime), it will print this
