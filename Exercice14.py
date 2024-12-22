word = input("Word: ")

spaces_before = (30 - len(word)) // 2
spaces_after = 30 - len(word) - spaces_before

print(" " + "*" * 30)

print("*" + " " * spaces_before + word + " " * spaces_after + "*")

print(" " + "*" * 30)
