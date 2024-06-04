# print("1. NTC to NCELL")
# print("2. NTC to NTC")
# print("3. NCELL to NTC")
# print("4. NCELL to NCELL")
# id = int(input("Which ISP do you want to call? (Enter 1, 2, 3, or 4): "))
# duration = int(input("Whats your call duration? "))
# if id == 1:
#     bonus = 2.5
#     if 0 <= duration < 10:
#         print(f"You get Rs {bonus} Bonus")
#     elif 10 <= duration < 20:
#         print(f"You get Rs.{bonus * 2} Bonus")
#     elif 20 <= duration < 30:
#         print(f"You get Rs.{bonus * 3} Bonus")
#     elif 30 <= duration < 40:
#         print(f"You get Rs.{bonus * 4} Bonus")
#     elif 40 <= duration < 50:
#         print(f"You get Rs.{bonus * 5} Bonus")
#     elif 50 <= duration < 60:
#         print(f"You get Rs.{bonus * 6} Bonus")
#     elif 60 <= duration < 70:
#         print(f"You get Rs.{bonus * 7} Bonus")
#     elif 70 <= duration < 80:
#         print(f"You get Rs.{bonus * 8} Bonus")
#     elif 80 <= duration < 90:
#         print(f"You get Rs.{bonus * 9} Bonus")
#     elif 90 <= duration < 100:
#         print(f"You get Rs.{bonus * 10} Bonus")

# elif id == 2:
#     bonus = 3.55
#     if 0 <= duration < 10:
#         print(f"You get Rs {bonus} Bonus")
#     elif 10 <= duration < 20:
#         print(f"You get Rs.{bonus * 2} Bonus")
#     elif 20 <= duration < 30:
#         print(f"You get Rs.{bonus * 3} Bonus")
#     elif 30 <= duration < 40:
#         print(f"You get Rs.{bonus * 4} Bonus")
#     elif 40 <= duration < 50:
#         print(f"You get Rs.{bonus * 5} Bonus")
#     elif 50 <= duration < 60:
#         print(f"You get Rs.{bonus * 6} Bonus")
#     elif 60 <= duration < 70:
#         print(f"You get Rs.{bonus * 7} Bonus")
#     elif 70 <= duration < 80:
#         print(f"You get Rs.{bonus * 8} Bonus")
#     elif 80 <= duration < 90:
#         print(f"You get Rs.{bonus * 9} Bonus")
#     elif 90 <= duration < 100:
#         print(f"You get Rs.{bonus * 10} Bonus")

# elif id == 3:
#     bonus = 4.5
#     if 0 <= duration < 10:
#         print(f"You get Rs {bonus} Bonus")
#     elif 10 <= duration < 20:
#         print(f"You get Rs.{bonus * 2} Bonus")
#     elif 20 <= duration < 30:
#         print(f"You get Rs.{bonus * 3} Bonus")
#     elif 30 <= duration < 40:
#         print(f"You get Rs.{bonus * 4} Bonus")
#     elif 40 <= duration < 50:
#         print(f"You get Rs.{bonus * 5} Bonus")
#     elif 50 <= duration < 60:
#         print(f"You get Rs.{bonus * 6} Bonus")
#     elif 60 <= duration < 70:
#         print(f"You get Rs.{bonus * 7} Bonus")
#     elif 70 <= duration < 80:
#         print(f"You get Rs.{bonus * 8} Bonus")
#     elif 80 <= duration < 90:
#         print(f"You get Rs.{bonus * 9} Bonus")
#     elif 90 <= duration < 100:
#         print(f"You get Rs.{bonus * 10} Bonus")

# elif id == 4:
#     bonus = 10
#     if 0 <= duration < 10:
#         print(f"You get Rs {bonus} Bonus")
#     elif 10 <= duration < 20:
#         print(f"You get Rs.{bonus * 2} Bonus")
#     elif 20 <= duration < 30:
#         print(f"You get Rs.{bonus * 3} Bonus")
#     elif 30 <= duration < 40:
#         print(f"You get Rs.{bonus * 4} Bonus")
#     elif 40 <= duration < 50:
#         print(f"You get Rs.{bonus * 5} Bonus")
#     elif 50 <= duration < 60:
#         print(f"You get Rs.{bonus * 6} Bonus")
#     elif 60 <= duration < 70:
#         print(f"You get Rs.{bonus * 7} Bonus")
#     elif 70 <= duration < 80:
#         print(f"You get Rs.{bonus * 8} Bonus")
#     elif 80 <= duration < 90:
#         print(f"You get Rs.{bonus * 9} Bonus")
#     elif 90 <= duration < 100:
#         print(f"You get Rs.{bonus * 10} Bonus")

# print(f"You talked for {duration} minutes")
# remaining_time = 100 - duration
# print(f"You have {remaining_time} minutes remaining")



print("1. NTC to NCELL")
print("2. NTC to NTC")
print("3. NCELL to NTC")
print("4. NCELL to NCELL")

id = int(input("Which ISP do you want to call? (Enter 1, 2, 3, or 4): "))
duration = int(input("What's your call duration? "))

bonus_values = {
    1: 2.5,
    2: 3.5,
    3: 4.5,
    4: 10
}

bonus = 0
if 0 <= duration < 10:
    bonus = bonus_values[id]
elif 10 <= duration < 20:
    bonus = bonus_values[id] * 2
elif 20 <= duration < 30:
    bonus = bonus_values[id] * 3
elif 30 <= duration < 40:
    bonus = bonus_values[id] * 4
elif 40 <= duration < 50:
    bonus = bonus_values[id] * 5
elif 50 <= duration < 60:
    bonus = bonus_values[id] * 6
elif 60 <= duration < 70:
    bonus = bonus_values[id] * 7
elif 70 <= duration < 80:
    bonus = bonus_values[id] * 8
elif 80 <= duration < 90:
    bonus = bonus_values[id] * 9
elif 90 <= duration < 100:
    bonus = bonus_values[id] * 10

if bonus > 0:
    print(f"You get Rs.{bonus} Bonus")
else:
    print("No bonus for this duration")

print(f"You talked for {duration} minutes")
remaining_time = 100 - duration
print(f"You have {remaining_time} minutes remaining")
