# function
# Function ဆိုတာ အလုပ်တစ်ခုလုပ်ဖို့ နာမည်ပေးပြီးစုရေးထားတဲ့ code block ပါ။ print()၊ len()၊ input() တို့က Python နဲ့ပါလာတဲ့ built-in functions တွေဖြစ်ပြီး ကိုယ်တိုင် def နဲ့ရေးတဲ့ function ကိုတော့ user-defined function လို့ခေါ်ပါတယ်။

def greet():
    print("Hello World")
greet()
greet()

def greet(name):
    print(f"Hello,{name}!")
    
greet("Aye Aye")
greet("Su Su")

def calculate_item_cost(unit_price, quantity):
    return unit_price * quantity 

item_cost = calculate_item_cost(5000, 3)
delivery_fee = 2000
final_total = item_cost + delivery_fee

print(item_cost)    # 15000
print(final_total)  # 17000

def show_total(price, quantity):
    print(price * quantity)

def get_total(price, quantity):
    return price * quantity

shown = show_total(1000, 2)
saved = get_total(1000, 2)

print(shown)
print(saved)

def can_buy(stock, quantity):
    if quantity <= 0:
        return False
    return stock >= quantity

print(can_buy(5, 3))  # True
print(can_buy(5, 8))  # False
print(can_buy(5, 0))  # False
print(can_buy(2,-1))

def calculate_bill(price, quantity):
    subtotal = price * quantity
    discount = subtotal * 10 // 100
    final_total = subtotal - discount
    return subtotal, final_total

subtotal, final_total = calculate_bill(5000, 2)
print(subtotal)     # 10000
print(final_total)  # 9000

def calculate_total(price, quantity):
    """Return the total cost before discounts."""
    return price * quantity

print(calculate_total(2000, 3))  # 6000

def say_hello():
    print("Hello")

other_name = say_hello
other_name()  # Hello

def is_even(number):
    return number % 2 == 0

print(is_even(8))  # True
print(is_even(7))  # False

def greet(name):
    print(f"Hello, {name}")

greet("Su Su")

def show_profile(name, age):
    print(f"{name} is {age} years old.")

show_profile(age=20, name="Aye Aye")
show_profile("Su Su", age=20)

def greet(name, message="Welcome"):
    return f"{message}, {name}!"

print(greet("Aye Aye"))
print(greet("Hello", "Mg Mg"))
print(greet("Su Su", message="Good morning"))