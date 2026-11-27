'''By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.'''

#my code
import math

def fab(num: int , num_befor: int) -> int:
    
    num_next = num + num_befor
    
    return num_next

num = 1
num_befor = 0
sum = 0
i=0
while(num < 4_000_000):
    i = i+1
    num_next = fab(num , num_befor)
    if (num_next % 2 == 0):
       sum = sum + num_next
    num_befor = num
    num = num_next 
    
    print(i , num_next , sum)
    
print(sum)


#ai optimised code


def sum_even_fibonacci(limit: int) -> int:
    total = 0
    a, b = 2, 8  # First two even Fibonacci numbers

    while a <= limit:
        total += a
        a, b = b, 4 * b + a

    return total


print(sum_even_fibonacci(4_000_000))