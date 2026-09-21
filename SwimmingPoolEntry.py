print("=== Swimming Pool Entry ===")
print("Answer 3 quick questions and get sorted into the correct pool!/n")

name = input("What is your full name?").strip().capitalize()
age = input("What is your age?").strip().lower()
weight = input("What is your weight?").strip().lower()
password = input("Enter the swimming pool's password :").strip().lower()

print()
print("=== Here is your entry results ===")
print("-" * 35)

print(name)
print(age)
print(weight)

if password == "swimming123":
    print("Password Correct!")
else:
    print("Password Invalid Please type again")

password2 = input("Enter the swimming pool's password again :").strip().lower()

if password2 == "swimming123":
    print("Password Correct!")
else:
    print("Invalid Entry!")

