price = float(input("Please type in a price: "))

dinars = int(price) 

centimes = int(round((price - dinars) * 100))  # Get the decimal part as an integer

# Output the results
print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")
