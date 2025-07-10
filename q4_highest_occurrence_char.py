from collections import Counter

# Function to find most frequent alphabet character
def highest_occurrence_char(input_string):
    # Filter only alphabets and convert to lowercase
    filtered = ''.join(filter(str.isalpha, input_string.lower()))
    if not filtered:
        return None, 0
    frequency = Counter(filtered)
    character, count = frequency.most_common(1)[0]
    return character, count

# Main program
if __name__ == "__main__":
    test_string = "hippopotamus"
    char, count = highest_occurrence_char(test_string)
    print(f"Highest occurring character: '{char}', Count: {count}")
