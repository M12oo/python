n = int(input('Enter a number : '))
flag=True
if n > 1:
    for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           flag=False
           break
    if flag:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")



