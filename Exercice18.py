numbers = [1, 2, 3, 4, 5]

def show_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Sort")
    print("6. Reverse")
    print("7. Search")
    print("8. Quit")

def append_element():
    try:
        value = int(input("Enter value to append: "))
        numbers.append(value)
        print(f"Updated List: {numbers}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def insert_element():
    try:
        value = int(input("Enter value to insert: "))
        index = int(input("Enter index to insert at: "))
        if index < 0 or index > len(numbers):
            print("Index out of range.")
        else:
            numbers.insert(index, value)
            print(f"Updated List: {numbers}")
    except ValueError:
        print("Invalid input. Please enter integers for both value and index.")

def pop_element():
    try:
        index = int(input("Enter index to pop from: "))
        if index < 0 or index >= len(numbers):
            print("Index out of range.")
        else:
            numbers.pop(index)
            print(f"Updated List: {numbers}")
    except ValueError:
        print("Invalid input. Please enter an integer index.")

def remove_element():
    try:
        value = int(input("Enter value to remove: "))
        if value in numbers:
            numbers.remove(value)
            print(f"Updated List: {numbers}")
        else:
            print(f"Value {value} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def sort_list():
    numbers.sort()
    print(f"Updated List: {numbers}")

def reverse_list():
    numbers.reverse()
    print(f"Updated List: {numbers}")

def search_element():
    try:
        value = int(input("Enter value to search for: "))
        if value in numbers:
            print(f"{value} found in the list.")
        else:
            print(f"{value} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    print(f"Initial List: {numbers}")
    
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option: "))
            
            if choice == 1:
                append_element()
            elif choice == 2:
                insert_element()
            elif choice == 3:
                pop_element()
            elif choice == 4:
                remove_element()
            elif choice == 5:
                sort_list()
            elif choice == 6:
                reverse_list()
            elif choice == 7:
                search_element()
            elif choice == 8:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter an integer for your choice.")


main()
