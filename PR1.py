import math
import time
from tqdm import tqdm
z=0
while z==0:

    T1=time.time()

    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    L1=[]
    L2=[]
    a1=int(input("Enter = "))
    a2=int(input("Enter = "))


    for i in tqdm(range(a1,a2),desc="Finding 2**n"):
        #A=2**i
        #A1=A-1
        if i%10 == 1 or i%10 == 3 or i%10 == 7 or i%10 == 9:
            L2.append(i)
        else:
            pass
    
        #L2.append(A1)


    
    for i in tqdm(L2,desc="Finding"):
        if is_prime(i)==1:
            #M=i+1
            #M1=math.log(M,2)
            #print(M1,"Yesssssssss")
            #if i%10 == 1 or i%10 == 3 or i%10 == 7 or i%10 == 9:
                #L1.append(i)
            #else:
                #pass
            L1.append(i)
            
            

    
    print(L1)
    print(len(L1))
    T2=time.time()
    T3=T2-T1
    T4=T3/60
    print(T3,"sec",T4,"min")

