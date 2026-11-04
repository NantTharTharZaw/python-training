# If statement
a = 33
b = 200

if b > a:
    print (" b is greater than a")
    #  space-4 or tab-1
    
# Else statement
a = 2000
b = 300
if b > a:
    print (" b is greater than a")
else:
    print (" b is not greater than a")


# budget if else 
budget = 20000
final_total = 23000
if budget >= final_total:
    remaining = budget - final_total
    print(f"Remaining budget:{remaining:,}MMK")
else:
    shortage = final_total -budget
    print(f"Need extra: {shortage:,}MMK")
print("Budget check finished.")
    
# input if else
age = int (input("Enter your age:"))
if age >= 18:
    print("Adult")
else:
    print("Under 18")
    
    
    
# block if else
# true so if ko lote false so else ko lote
is_logged_in = True

if is_logged_in:
    message = "Welcome back!"
else:
    message = "Please log in."

print(message)  # Please log in.



# Elif statement
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Fail")
    
    
# order fee
order_total = 30000

if order_total >= 50000:
    delivery_fee = 0
elif order_total >= 20000:
    delivery_fee = 1000
else:
    delivery_fee = 2000

print(f"Delivery fee: {delivery_fee:,} MMK")

# Nested if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20.")
    else:
        print("but not above 20.")
        
#sec nested if
is_registered = True
has_paid = False

if is_registered:
    if has_paid:
        print("You can join the class.")
    else:
        print("Please complete the payment.")
else:
    print("Please register first.") 
    
        
   
# Pass statement (no error)
# if x > 10:
#     pass

# For loops
fruits = ["apple","banana","orange"]
for x in fruits:
    print(x)

# Match statement
choice = "2"

match choice:
    case "1":
        print("View products")
    case "2":
        print("View cart")
    case "3":
        print("Checkout")
    case _:
        print("Invalid choice")

# sec 
day = "Sunday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Other day")

# third 
command = ["move", 10, 20]

match command:
    case ["move", x, y]:
        print(f"Move to {x}, {y}")
    case ["stop"]:
        print("Stopped")
    case _:
        print("Unknown command")
# Guard နဲ့ condition ထပ်စစ်ခြင်း
score = 85

match score:
    case value if value < 0 or value > 100:
        print("Invalid score")
    case value if value >= 40:
        print("Pass")
    case _:
        print("Fail")


# Break statement
fruits = ["apple","banana","orange"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
    
# Continue statement
fruits = ["apple","banana","orange"]
for x in fruits:
    if x == "banana":
      continue