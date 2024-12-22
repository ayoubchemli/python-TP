print ("Total amount:")
amount = int(input())

print("Number of items:")
items = int(input())

print("Day of the week:")
day = str(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday": 
    discount = 10 
elif day == "Saturday" or day == "Sunday":
    discount = 20
    
if amount > 5:
    discount += 5
    
total = amount - (amount * discount / 100)

print ("Total price after discount:", total)