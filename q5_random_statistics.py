import random
import statistics

# Function to generate stats for 25 random integers between 1 and 10
def generate_random_statistics():
    random_numbers = [random.randint(1, 10) for _ in range(25)]
    mean_val = statistics.mean(random_numbers)
    median_val = statistics.median(random_numbers)
    mode_val = statistics.mode(random_numbers)
    return random_numbers, mean_val, median_val, mode_val

# Main program
if __name__ == "__main__":
    numbers, mean, median, mode = generate_random_statistics()
    print(f"Random numbers: {numbers}")
    print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
