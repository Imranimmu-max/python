#runs untill condition become false 
#while loop 

i = 1 
while i <= 5 :
    print(i)
    i = i + 1
#for loops 
for i in range(1,10):
    print(i*2)

print("\n")

for i in range(5,0,-1):
    print(i)


n = int(input("enter a number : "))
total=0
for i in range(1,n+1):
    total = i+total

print(total)