word = input("Please type in a word: ").strip()  

is_palindrome = True

for i in range(len(word) // 2):
    first_char = word[i]
    last_char = word[-(i + 1)]
    
    if first_char != last_char:
        is_palindrome = False 
        break 

if is_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
