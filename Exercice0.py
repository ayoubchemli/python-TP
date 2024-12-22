print(" how many people need a ride?")
x = int(input())
print("Ask the user how many people can fit in one tax?")
y = int(input())

if x % y == 0:
    print("You will need", x // y, "taxi(s) to transport", x, "people.")

else:
    print("You will need", x // y + 1, "taxi(s) to transport", x, "people.")