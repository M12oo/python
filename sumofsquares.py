a=int(input("Enter a no :"))
for i in range(0,a+1):
    print(i**2)
    
    
print("Sum of the squares is : ",sum (i**2 for i in range(0,a+1)))
   