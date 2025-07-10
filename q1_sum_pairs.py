# Function to count number of unique pairs in the list with a given sum
def count_sum_pairs(input_list, target_sum=10):
    count = 0
    seen = set()
    for number in input_list:
        complement = target_sum - number
        if complement in seen:
            count += 1
        seen.add(number)
    return count

# Main program
if __name__ == "__main__":
    numbers = [2, 7, 4, 1, 3, 6]
    result = count_sum_pairs(numbers)
    print(f"Number of pairs with sum 10: {result}")
