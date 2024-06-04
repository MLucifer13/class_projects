print("--------------------------COMPUTER BAZZAR---------------------")

print("Welcome to Computer Bazzar")
list = [["Dell", 90000], ["Asus" , 200000], ["Apple" , 150000]]
print("Available computers: ")
for brand,price in list:
    print(f"{brand} costs: {price}")

computer = int(input("Which computer do you want? "))
if computer == 1 or computer =="Dell":
    price = int(list[0][1])
if computer == 2 or computer =="Asus":
    price = list[1][1]
if computer == 3 or computer =="Ap":
    price = list[2][1]


quantity = int(input("Enter the number of computer you want"))

print("-----------1. Home Delivery = Rs.1000-------------")
print("-----------2. Pickup = Free-------------")

delivery_option = int(input("Which pickup do you want? "))
if delivery_option == 1:
    delivery_fee = 1000
elif delivery_option == 2:
    delivery_fee = 0
else:
    print("Invalid option")

total_amount = price*quantity + delivery_fee
tax = total_amount*0.13
final_price = total_amount + tax
details = input("Whats your name and address? ")
name, address = details.split(",")
print(f"Name:{name}")
print(f"Address: {address}")
print(f"Total amount = {total_amount}" )
print(f"Total tax = {tax}")
print(f"Grand Total = {final_price}")
