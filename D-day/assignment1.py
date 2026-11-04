# Collect user input
print("Shopping Bill & Budget Checker")
customer_name = input("Customer name")
customer_budget = int(input ("Customer budget(MMK)"))

# print("First item:")
item1_name = input("First item name")
item1_price = int(input("First item unit price(MMK)"))
item1_quantity = int(input("First item quantity"))


# print("Second item")
item2_name = input("Second item name")
item2_price = int(input("Second item unit price(MMK)"))
item2_quantity = int(input("Second item quantity"))

# Set fixed values
Discount = 10
Delivery_fee = 2000

# Calculate

item1_cost = item1_price * item1_quantity
item2_cost = item2_price * item2_quantity

Total_item_cost = item1_cost + item2_cost
Discount_amount = Total_item_cost * Discount/100
Final_total = Total_item_cost - Discount_amount + Delivery_fee
Remaining_budget = customer_budget - Final_total

# Check
Within_budget = Remaining_budget >= 0


# Display
print(f"Customer name: {customer_name}")

print(f"First item name: {item1_name}")
print(f"First item unit price: {item1_price}MMK")
print(f"First item quantities: {item1_quantity}")
print(f"First item cost: {item1_cost}")

print(f"Second item name: {item2_name}")
print(f"Second item unit price: {item2_price}MMK")
print(f"Second item quantities: {item2_quantity}")
print(f"Second item cost: {item2_cost}")

print(f"Total item cost: {Total_item_cost}MMK")
print(f"discount amount: {Discount_amount}")
print(f"deliver fee: {Delivery_fee}")
print(f"final total:{Final_total}")


print(f"Original budget:{customer_budget}")
print(f"remaining budget:{Remaining_budget}")
print(f"Boolean budget:{Within_budget}")












 

