print("Prime numbers between 1 and 20 are:")
ulmt=20;
for num in range(ulmt):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)