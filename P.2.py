# Create a nested list to store divisors for each number from 1 to 100
all_divisors_nested = []
all_divisor_sums = []

# Iterate through numbers from 1 to 100
for number in range(1, 101):
    divisors = []
    divisor_sum = 0
    # Find divisors for the current number
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
            divisor_sum += i
    all_divisors_nested.append(divisors)
    all_divisor_sums.append(divisor_sum)

# Print the divisors for each number
for i, divisors in enumerate(all_divisors_nested, start=1):
    print(f"Divisors of {i}: {divisors}")

print(all_divisors_nested)

for i, divisor_sum in enumerate(all_divisor_sums, start=1):
    print(f"Sum of divisors for {i}: {divisor_sum}")

print(all_divisor_sums)


