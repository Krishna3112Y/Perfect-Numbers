def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def lucas_lehmer_test(n):
    if n == 1:
        return True  # 2^1 - 1 = 1, which is not prime
    mersenne_number = 2**n - 1
    s = 4
    for _ in range(n - 2):
        s = (s**2 - 2) % mersenne_number
    return s == 0

def main():
    for n in range(1, 101):
        mersenne_number = 2**n - 1
        if lucas_lehmer_test(n):
            print(f"Mersenne number for n = {n} is {mersenne_number}. It is prime.")
        else:
            print(f"Mersenne number for n = {n} is {mersenne_number}. It is not prime.")

if __name__ == "__main__":
    main()
