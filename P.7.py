import time
from tqdm import tqdm  # Import tqdm for progress bar

def is_perfect(n):
    """
    Checks if a given number n is perfect.
    """
    sum_divisors = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                sum_divisors += i + n // i
            i += 1
    return sum_divisors == n and n != 1

def find_perfect_numbers(n):
    """
    Finds all perfect numbers up to a given number n.
    """
    perfect_numbers = []
    for i in tqdm(range(1, n + 1), desc="Finding perfect numbers"):
        if is_perfect(i):
            perfect_numbers.append(i)
    return perfect_numbers


a=0
while a==0:
    # Take input from the user
    end = int(input("Enter a number to find all perfect numbers up to: "))

    # Measure the time taken to find perfect numbers
    start_time = time.time()
    perfect_numbers = find_perfect_numbers(end)
    end_time = time.time()

    # Print the result
    print(f"Perfect numbers up to {end}: {perfect_numbers}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
