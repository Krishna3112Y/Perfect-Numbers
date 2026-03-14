# Create a list to store the sum of divisors for each number from 1 to 100
all_divisor_sums = []
Perfect=[]

# Iterate through numbers from 1 to 100
for number in range(86619373, 86619374):
    divisor_sum = 0
    # Find divisors for the current number
    for i in range(1, number ):
        if number % i == 0:
            divisor_sum += i
    
    all_divisor_sums.append(divisor_sum)
    if number==divisor_sum :
        print("Yes",number)
        Perfect.append(number)
        print(number)
        #Perfect.append()
        

# Print the sum of divisors for each number
#for i, divisor_sum in enumerate(all_divisor_sums, start=1):
    #print(f"Sum of divisors for {i}: {divisor_sum}")

print(Perfect)
