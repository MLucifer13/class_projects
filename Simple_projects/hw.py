#check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")





#check if num is divisible by 3 and 5

if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")




# check if the entered year is a leap year
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")