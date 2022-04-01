T1 = ()
L1 = list(T1)
n=int(input("Enter the number of numbers : "))
for i in range(0,n):
    L1.append(int(input("Enter the number : ")))
T2 = tuple(L1)
add = sum(T2)
print("The final tuple is : " + str(T2))
print("The sum of all the elements of the tuple is : " + str(add))