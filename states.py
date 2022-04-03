l=[]
l1=[]

n=int(input("Enter the number of states\n"))

for i in range(0,n):
    print("Enter the name of the state")
    l1.append(str(input()))

    print("Enter the name of the capital")
    l1.append(str(input()))

    print("Enter the population")
    l1.append(str(input()))

    print("Enter the area")

    l1.append(str(input()))
    l.append(l1)
    l1=[]

print("State\tCapital\tpopulation\tarea")

for i in range(0,n):
    print(l[i][0],"\t",l[i][1],"\t",l[i][2],"\t\t",l[i][3])
    