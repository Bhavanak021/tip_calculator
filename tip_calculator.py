#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Tip Calculator")
bill = float(input("Your total bill?"))
percentage = input("The percentage of tip you want to pay 10,12 or 15?")
no_person = int(input("No. of people?"))

total_percentage = 1 + (float(percentage)/100)

total_bill = bill*total_percentage
tip_per_person = total_bill/no_person
print(tip_per_person)