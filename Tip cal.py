print("Welcome to Jolie the tip calculator")
total_bill = float(input ("What is the total bill? "))
percen = int(input ("What percentage tip would you like to give? (10, 12 or 15?) "))
people = int(input ("How many people that will split the bill? "))
result1 = round((total_bill*percen/100 + total_bill)/people,2)
result2 = "{:.2f}".format(result1)
print(f"Each people should pay {result2} dollars")