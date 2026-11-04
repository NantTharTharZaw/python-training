# match
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    

#Combine Value 
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    
# while loop
i = 1
while i < 6:
  print(i)
  i += 1
  
# break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
# for loop  
for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)
  
#  Nested loops 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)