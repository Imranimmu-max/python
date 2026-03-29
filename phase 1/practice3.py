# practice q 1 
def sq(n):
    return n*n

n=int(input("enter a number "))
square=sq(n)
print(square)

#practice q 2 

def multi(a,b):
    print("table of a ")
    for i in range(1,10):
        print(a,"*",i,"=",i*a)
    print("table of b ")
    for i in range(1,10):
        print(b,"*",i,"=",i*b)


multi(5,10)
# practce q 3 😮‍💨
l = [60,70,80,90,100]
max = l[0]
for i in l:
    if i > max:
        max=i 
print(max)

# practice q 4 

x = [1,2,3,4,5,6,7,8,9,10]
y=x[0]
for i in x:
    if i%2==0:
        print(i)


#challange 😋😏

#creating a function 
def sum():
    v = []
    
    sum=0

    for i in range(4):
        n = int(input("enter a num"))
        v.append(n)
    v1=v[0]
    for i in v:
        sum = i+sum
    
    print(sum)

sum()
    