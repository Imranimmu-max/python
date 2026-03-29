#lists 
#like arrays in c 😋
#a list stores multiple value in a variable :

#example code :
a = [1,2,3,4,5]
names = ["aliya","imran","jasiya"]

# eccessing the list elements 

print(a[2])
print(names[0])

#accessing lists through loops 🔥

for i in names:
    print(i)

for i in a:
    print(i)

#adding elemets 
a.append(6)
print(a[5])
a.remove(5)
for i in a:
    print(i)

print("\n")

numbs = []

for i in range(5):
    n = int(input("enter a number : "))
    numbs.append(n)

for i in numbs:
    print(i,"\t")