print()
greeting = "Welcome to Tip Calculator"
print(greeting.center(60,"."),"\n")
bill = float(input("What is the total bill: ₹"))
tip = int(input("\nwhat is the percentage of the tip you wanna give: "))
person_count = int(input("\nHow many people want to split the bill: "))
total_bill = bill + (tip / 100) * bill
final_bill = total_bill/person_count

print("\nEach person should pay:₹",final_bill,"\n")