# Multiples of 3 or 5
multiple=0
for i in range (1,1000):
    if(i%3==0 or i%5 == 0):
        multiple=multiple+i
        
        
print(multiple)