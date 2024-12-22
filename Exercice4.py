agePerson1 = int(input("Please type in the age of the first person: "))
agePerson2 = int(input("Please type in the age of the second person: "))

if agePerson1 > agePerson2:
    print(f"The older age is: {agePerson1}")
elif agePerson2 > agePerson1:
    print(f"The older age is: {agePerson2}")
else:
    print("Both people are the same age!")
