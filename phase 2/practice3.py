#q1
f = open("name.txt","w")
f.write("my name isimran  imran ")
f.close()

#q2

f = open("name.txt","r")
print(f.read())
f.close()

s = [1,2,3,4,5]

import os 

# os.remove("name.txt")
# f = open("name.txt","r")
# text = f.read()
# words = text.split()
# print(len(words))
# f.close()

with open("name.txt") as f:
    text = f.read()
    words = text.split()
    print(len(words))



