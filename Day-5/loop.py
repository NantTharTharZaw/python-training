# while loop
count = 1

while count <= 3:
    print(count)
    count += 1

print("Done")


number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print(total)  # 15

# while loop
students = ["Aye Aye", "Mg Mg", "Su Su"]

for student in students:
    print(f"Hello, {student}!")
    
for number in range(1, 6):
    print(number)
    
for letter in "Cat":
    print(letter)
    
student = {"name": "Aye Aye", "age": 20}

for key in student:
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")
    
students = ["Aye Aye", "Mg Mg"]

for position, name in enumerate(students, start=1):
    print(f"{position}. {name}")
    
for row in range(1, 3):
    for column in range(1, 4):
        print(row, column)

# you can write quit it stop
command = input("Type a command or quit: ")

while command != "quit":
    print(f"You entered: {command}")
    command = input("Type a command or quit: ")

print("Program closed")