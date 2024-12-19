# Dictionary of letters and their corresponding point values
letter_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

def calculate_word_value(word):
    word = word.upper()
    total_value = 0

    for letter in word:
        if letter in letter_values:
            total_value += letter_values[letter]
        else:
            print(f"Warning: Ignoring unknown letter '{letter}'")

    return total_value

# Define stop words
stop_words = ['quit', 'q']

while True:
    word = input("Enter a word (or a stop word to exit): ").strip().lower()

    if word in stop_words:
        break

    base_total_value = calculate_word_value(word)
    print(f"The base total value of '{word}' is {base_total_value} points.")

print("Exiting the program.")
