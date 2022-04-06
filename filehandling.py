n=int(input("Enter the size of the dictionary\n"))
d={}
l=[]
for i in range(0,n):
    print("Enter the name of the state")
    l.append(str(input()))
    print("Enter the capital of the state")
    l.append(str(input()))
    print("Enter the population")
    l.append(int(input()))
    print("Enter the area")
    l.append(int(input()))
    d[(i+1)]=l
    l=[]
maximum=0 #veriable to store the maximum population
for i in range(0,n):
    if(d[(i+1)][2]>maximum):   
        maximum=d[(i+1)][2]

max_area = 0
for i in range(0,n):
    if(d[(i+1)][3]>max_area):
        max_area=d[(i+1)][3]

hpd=[]
for i in range(0,n):
    hpd.append((d[i+1][2]/d[i+1][3]))

max=0
for i in hpd:
    if(i>max):
        max=i
add = 0
for i in range(0,n):
    add = add+(d[(i+1)][2])
avg = add/n
with open ("Ans6.txt", "w+") as Ans6:
         Ans6.write(str(d))
         Ans6.write(str("\nThe highest population is %d"%maximum))
         Ans6.write(str("\nThe average population is : %f"%avg))
         Ans6.write(str("\nThe Maximum Area is : %d"%max_area))
         Ans6.write(str("\nThe Highest Population Density is : %f"%max))