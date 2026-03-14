import time
from tqdm import tqdm

z=0

while z==0:


    per=[]
    k=1
    k1=2
    count=0
    r=int(input("Enter the Number of Perfect number = "))
    time_start=time.time()
    r1=r-1

    while count < r1 :

        for n in range(k, k1,):
                
                mersenne_number = 2**n - 1
                s = 4
                for _ in range(n - 2):
                    s = (s**2 - 2) % mersenne_number
                    print(s**2 - 2)
                if s == 0:
                    #print(f"Mersenne number for n = {n} is {mersenne_number}. It is prime.")
                    per.append(n)
                    print(len(per)," = ",n)
                else:
                    pass
                    #print(f"Mersenne number for n = {n} is {mersenne_number}. It is not prime.")
        k=k1
        k1+=1
        
        count=len(per)

    print(per)
    print(count)

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
    time_end=time.time()
    Time_taken=time_end-time_start
    print(Time_taken)