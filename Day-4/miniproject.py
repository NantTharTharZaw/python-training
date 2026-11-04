print("=== Student Registration ===")


student_name = input("Enter student name: ")
age_text = input("Enter age: ")
course_name = input("Enter course name: ")
total_fee_text = input("Enter total course fee (MMK): ")
paid_amount_text = input("Enter paid amount (MMK): ")


age = int(age_text)
total_fee = int(total_fee_text)
paid_amount = int(paid_amount_text)

remaining_amount = total_fee - paid_amount



print("=== Registration Summary ===")
print(f"Student: {student_name}")
print(f"Age: {age} years old")
print(f"Course: {course_name}")
print(f"Total fee: {total_fee:,} MMK")
print(f"Paid amount: {paid_amount:,} MMK")
print(f"Remaining amount: {remaining_amount:,} MMK")