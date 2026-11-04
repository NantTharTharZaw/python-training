# Datetime
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)

print(x.strftime("%Y"))


# Math
x = min(5, 20 ,25)
y = max(5, 20 ,25)

print(x)
print(y)
print(abs(5))
print(pow(4,3))


import math
print(math.sqrt(144))

# big num
print(math.ceil(1.4))
# small num
print(math.floor(1.4))


prices = [3000, 1000, 2000]
print(sum(prices))

# JSON
import json
x = {
    "name": "John",
    "age": "13"   
}
print(json.dumps(x))

# Try Except (error handling)
#  print(x)
x = 5
try:
    print(x)
except:
    print("Name is not defined")
else:
    print("x is defined")
finally:
    print("The program is done")
    
print("it is working")


# Raise an exception
def calculate_total(price,quantity):
    if price < 0:
        raise ValueError("Price can't be negative")
    if price <= 0:
            raise ValueError("Price can't be positive")
    return price * quantity

try:
    total = calculate_total(1000,0)
except ValueError as error:
    print(error)
    
    

