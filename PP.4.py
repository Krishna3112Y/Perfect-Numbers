import math
from tqdm import tqdm

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def main():
    given_list=[]
    for i in range(1,81):
        A=2**i
        A1=A-1
        given_list.append(A1)

    
    prime_numbers = []

    print("Checking for prime numbers in the given list:")
    for num in tqdm(given_list, desc="Progress", unit="number"):
        if is_prime(num):
            prime_numbers.append(num)

    print("\nPrime numbers found in the list:")
    print(prime_numbers)





if __name__ == "__main__":
    main()
