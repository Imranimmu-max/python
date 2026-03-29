# practice q 1 

n = int(input("enter a number : "))

if n > 0:
    print("is a positive number : ",n)
elif n < 0:
    print(n,"is a nagative number : ")
else:
    print("zero")

#practice q 2 
n1=int(input("enter  n : "))
for i in range(1,n1+1):
    print(i)
print("\n")

# practice q 3 
for i in range(1,21):
    if(i%2==0):
        print(i)

# practice q 4 
x = int(input("enter a nuumbber "))
fact=1
for i in range(1,x+1):
    fact = fact*i
print(fact)

#challenge 😋
p="*"
c="*"
for i in range(6):
    print(c)
    c+=p
    

