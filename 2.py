# Even Fibonacci Numbers

f=[1,2]
sumEven=2
while True:
 fNum=f[-1]+f[-2]
 if fNum <= 4000000 :
     f.append(fNum)
     if fNum % 2 == 0:
      sumEven=sumEven+fNum
 else:  
     break

print(sumEven)