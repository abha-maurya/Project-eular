'''
if we add all the square numbers till 308 thousands 
what will be the sum of odd valued squares 
'''



# my solution

import math

sum = 0

for i in range(1, 308_001,2):
    
    print(i)
    square= i*i
    sum = sum + square
    print(sum)
    
    
    

#optimised solution by ai
    
total = 0

for i in range(1, 308_001, 2):
    total += i * i

print(total)