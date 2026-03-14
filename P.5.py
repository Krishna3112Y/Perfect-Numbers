import time
from tqdm import tqdm


per=[]

w=0
while w==0:
    k=int(input("enter The NUmber For Finding Mersenne number = "))

    for n in tqdm(range(1, k), desc="Finding Mersenne number"):
        
        mersenne_number = 2**n - 1
        s = 4
        for _ in range(n - 2):
            s = (s**2 - 2) % mersenne_number
        if s == 0:
            #print(f"Mersenne number for n = {n} is {mersenne_number}. It is prime.")
            per.append(n)
        else:
            pass
            #print(f"Mersenne number for n = {n} is {mersenne_number}. It is not prime.")

    print(per)

    per1=[6]
    


    for i in tqdm(per,desc="Finding Perfect Number "):
        A=2**i
        A1=1
        A2=A-A1 
        A3=i-1
        A4=2**A3 
        A5=A2*A4
        per1.append(A5)
    
    L1=len(per1)

    for x in range(0,L1):
        print(x+1,"st Perfect Number = ",per1[x])