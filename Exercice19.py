unique_words = set()

while True:
    word = input("Enter a word: ").strip()
    if word in unique_words:
        print(f"You typed in {len(unique_words) - 1} unique words.")
        break
    unique_words.add(word)
