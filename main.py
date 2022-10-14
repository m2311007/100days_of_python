print("Welcome to the tip calculator")
bill = float(input("What is the total bill? "))
number_of_people = int(input("How many people to spil the bill? "))
tip = float(input("What % of tip would you like to give? "))

percent_of_tip = tip * 0.01

total_bill = bill + (bill * percent_of_tip)

bill_per_person = total_bill / number_of_people


print(f"Each person should pay: {bill_per_person}")