
b=int(input("Enter the no : "))
l1=[0,1]
for i in range(0,1000):
    n1=l1[i]+l1[i+1]
    l1.append(n1)

if b in l1:

    print(b,"Is a fibonacci no") 
else:
    print(b,"Is not a fibonacci no")