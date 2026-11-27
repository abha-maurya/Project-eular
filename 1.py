'''
Find the sum of all the multiples of  3 or 5 below 1000.

'''

import time

ts = time.perf_counter()
total = 0
n=9_000_000

for i in range(1,n):
    if((i % 3 == 0) or (i % 5 == 0)):
        total = total + i
        
print (total)        
print(time.perf_counter() - ts)       
#optimised ai version

ts = time.perf_counter()
def multiples_sum_below_limit(limit: int , number: int ) -> int :
    
    k = (limit-1) // number
    
    total = (number * k * (k+1))//2
    
    return total

total = multiples_sum_below_limit(n,3) + multiples_sum_below_limit(n,5) - multiples_sum_below_limit(n,15)
print(total)

print(time.perf_counter()-ts)

#farooqu sir version
ts = time.perf_counter()
new_tota = sum(range(0,n,3))+ sum(range(0,n,5)) - sum(range(0,n,15)) 
print(new_tota)

print(time.perf_counter()-ts)
