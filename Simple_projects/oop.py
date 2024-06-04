# def main():
#     student = Student()
#     if student["name"] == "Ram":
#         student["house"] = "Gryffindor"
#     print(f"{student['name']} is from {student['house']}")

# def Student():
#     student_name = input("Enter your name: ")
#     house = input("Enter your house: ")
#     return {"name": student_name, "house": house}

# if __name__ == "__main__":
# #     main()
# numbers = [12,12,1,2,13,13,14,13,14,15,18,18]
# unique_numbers = set(numbers)
# print(unique_numbers)
# seen = []
# count = 0
# while count < len(numbers):
#     if numbers[count] not in seen:
#         seen.append(numbers[count])
#     count += 1
# print(seen)

# users = [
#     {"id": 1, "name": "John", "gender": "male","status": True},
#     {"id": 2, "name": "Ram", "gender": "male","status": True},
#     {"id": 3, "name": "Shyam", "gender": "male","status": False},
#     {"id": 4, "name": "Hari", "gender": "male","status": True},
#     {"id": 5, "name": "Sita", "gender": "female","status": False},
#     {"id": 6, "name": "Ramya", "gender": "female","status": True},
# ]
# active_user = 0
# inactive_user = 0
# female = 0
# male = 0
# active_male = 0
# active_female = 0
# inactive_male = 0
# inactive_female = 0
# for user in users:
#     if user["status"] == True:
#         active_user += 1
#     if user["status"] == False:
#         inactive_user += 1
#     if user["gender"] == "male":
#         male += 1
#         if user["status"] == True:
#             active_male += 1
#         if user["status"] == False:
#             inactive_male += 1
#     if user["gender"] == "female":
#         female += 1
#         if user["status"] == True:
#             active_female += 1
#         if user["status"] == False:
#             inactive_female += 1
# print(f"Total number of active users are {active_user}")
# print(f"Total number of inactive users are {inactive_user}")
# print(f"Total number of male users are {male}")
# print(f"Total number of female users are {female}")
# print(f"Total number of active male users are {active_male}")
# print(f"Total number of active female users are {active_female}")
# print(f"Total number of inactive male users are {inactive_male}")
# print(f"Total number of inactive female users are {inactive_female}")

users = [
    {"username": "ram", "password": "ram123"},
    {"username": "shyam", "password": "shyam123"},
    {"username": "hari", "password": "hari123"},
    {"username": "sita", "password": "sita123"},
    {"username": "ramya", "password": "ramya123"}
]

books = [
    {"id": 1, "title": "The Great Gatsby", "price": 10.99},
    {"id": 2, "title": "To Kill a Mockingbird", "price": 8.99},
    {"id": 3, "title": "1984", "price": 12.99},
    {"id": 4, "title": "Pride and Prejudice", "price": 9.99},
    {"id": 5, "title": "The Catcher in the Rye", "price": 7.99}
]

username = input("Enter your username: ")

user_found = False
for user in users:
    if username == user["username"]:
        password = input("Enter your password: ")
        if password == user["password"]:
            print("Login successful")
            user_found = True
            for book in books:
                print("Books available: ")
                print(f"{book['id']} {book['title']} {book['price']}")
            break
        else:
            print("Incorrect password")
            user_found = True
            break

if not user_found:
    print("Username not found")
