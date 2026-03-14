import time
import tqdm
import math

z=0
while z==0:
    L1=[]
    a1=int(input("Enter = "))
    a2=int(input("Enter = "))
    for i in range(a1,a2):
        if i%10 == 1 or i%10 == 3 or i%10 == 7 or i%10 == 9:
            M=math.factorial(i-1)+1
            if type(M)==int :
                L1.append(i)
        else:
            pass

    print(L1)
    