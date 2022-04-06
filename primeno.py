# n = int(input('Enter a number : '))
# flag=True
# if n > 1:
#     for i in range(2,n):
#        if (n % i) == 0:
#            print(n,"is not a prime number")
#            flag=False
#            break
#     if flag:
#         print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")



# Program to check if a number is prime or not

num = -29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = True

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = False
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is a prime number")
    
else:
    print(num, "is not a prime number")