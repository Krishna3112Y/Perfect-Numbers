import time
from tqdm import tqdm
z=0
while z==0:
    per=[]
    k=0

    k1=875899
    count=0
    r=int(input("Enter the Number of Perfect number = "))
    time_start=time.time()
    r1=r-1


    while count < r1 :

            for n in tqdm(range(k, k1,),desc="Finding the Next"):
                    
                    mersenne_number = 2**n - 1
                    s = 4
                    for _ in range(n - 2):
                        s = (s**2 - 2) % mersenne_number
                    if s == 0:
                        #print(f"Mersenne number for n = {n} is {mersenne_number}. It is prime.")
                        per.append(n)
                        print(len(per)," = ",n)
                    else:
                        pass
                        #print(f"Mersenne number for n = {n} is {mersenne_number}. It is not prime.")
            k=k1
            k1+=1000
            
            count=len(per)

    print(per)
    print(count)
