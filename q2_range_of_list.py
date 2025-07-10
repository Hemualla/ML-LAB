# Function to calculate range of the list
def calculate_range(real_list):
    if len(real_list) < 3:
        return "Range determination not possible"
    return max(real_list) - min(real_list)

# Main program
if __name__ == "__main__":
    real_numbers = [5, 3, 8, 1, 0, 4]
    result = calculate_range(real_numbers)
    print(f"Range of list: {result}")
