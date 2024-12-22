try:
    N = int(input("Enter a positive integer: "))
    if N <= 0:
        print("The number must be positive.")
    else:
        for i in range(-N, N + 1):
            if i != 0:
                print(i)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
