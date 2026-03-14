import random
import time
import math
from tqdm import tqdm  # Import tqdm for progress bar
z=0
while z==0:

    T1=time.time()

    def power(x, y, p):
        res = 1
        x = x % p
        while y > 0:
            if y & 1:
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res

    def miller_test(d, n):
        a = 2 + random.randint(1, n - 4)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    def is_prime(n, k):
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True
        d = n - 1
        while d % 2 == 0:
            d //= 2
        for _ in tqdm(range(k), desc="Finding prime numbers"):
            if not miller_test(d, n):
                return False
        return True

    def prime_range(num,num1):
        prime_numbers = []
        mer=[]
        mer1=[]
        for i in range(num,num1):
            A=2**i
            A1=A-1
            mer.append(A1)

        for i in mer:
            if is_prime(i, 10):  # Use 10 iterations for reasonable accuracy
                prime_numbers.append(i)
                M=i+1
                M1=math.log(M,2)
                print(M1,"Yesssssssss")
                mer1.append(M1)
                print(mer1)
            else:
                M=i+1
                M1=math.log(M,2)
                print(M1,"Noooooooo")
                
        return prime_numbers 

    def main():
        number = int(input("Enter starting number = "))  # Change this to the desired range
        number1=int(input("Enter ending number = "))
        prime_list = prime_range(number,number1)
        print("Prime numbers from 1 to", number, ":", prime_list)
        print("Sum of prime numbers:", sum(prime_list))
        print(len(prime_list))
    
        T2=time.time()
        T3=T2-T1
        T4=T3/60
        print(T3,"sec",T4,"min")

    if __name__ == "__main__":
        main()
