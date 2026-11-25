'''
Find the sum of all the multiples of  3 or 5 below 1000.

'''

import math
sum = 0
for i in range(1,1000):
    if((i % 3 == 0) or (i % 5 == 0)):
        sum = sum + i
        print (i,sum)
        
        
#optimised ai version

def multiples_sum_below_limit(limit: int , number: int ) -> int :
    
    k = (limit-1) // number
    
    sum = (number * k * (k+1))//2
    
    return sum

sum = multiples_sum_below_limit(1000,3) + multiples_sum_below_limit(1000,5) - multiples_sum_below_limit(1000,15)
print(sum)