l1=[0,1]
n=int(input("Enter the number of terms:"))
for i in range(0,n):
    n1=l1[i]+l1[i+1]
    l1.append(n1)
print(l1)
