# Largest Prime Factor
from sympy import prime
i=1
Num=600851475143
while  Num!=1:
    if Num % prime(i) == 0:
            largestPrime=prime(i)
            print(largestPrime)
            Num= Num / largestPrime
            print(Num)
            i=i+1
    else:
            i=i+1
    
 
        
print(largestPrime)