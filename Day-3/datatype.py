# Datatype
age=42
price=34.24
calculation = 2 + 4j
myName = "Tun Tun"
isCorrect = True
isEmpty = None
print(f"age:{age}") 
print(type(age))
print(type(price))
print(type(calculation))
print(type(myName))
print(type(isCorrect))
print(type(isEmpty))

isEmpty = None
print(isEmpty)
isEmpty = "hello"
print(isEmpty)


# Dynamic Typed and Strongly type
x = "Hello"
print(x)
x = 4
print(x)


#print (10 + "4") no add this error number not add

#print(10 + int("4")) Casting (Type Conversion)
 
#f-string { } input added
name = "thar"
age = 21
print(f"My name is:{name} and My age is:{age}")
print(f"Next year:{age + 1}")

#input
name = input("What is your name")
print(name)
#Tetminal testing