user_list = []

while True:
    try:
        num = int(input("Enter a number (0 to quit): "))
        if num == 0:
            break
        user_list.append(num)
        print(f"Current List: {user_list}")
        print(f"Sorted List: {sorted(user_list)}")
    except ValueError:
        print("Please enter a valid number.")
