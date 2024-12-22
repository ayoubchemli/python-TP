cities = []  

print("Enter the name of a city (type 'stop' to finish):")

while True:
    city = input()  
    if city.lower() == "stop":  
        break
    cities.append(city)  

city_populations = {city: len(city.replace(" ", "")) * 1_000_000 for city in cities}

sorted_cities = sorted(city_populations.items(), key=lambda item: item[1], reverse=True)

print("\nCity Populations (sorted by largest to smallest):")
for city, population in sorted_cities:
    print(f"{city}: {population:,} citizens")
