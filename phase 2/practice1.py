# practice q1
marks = {
    "eng" : 98,
    "kan" : 78,
    "hindi":89
}

print(marks)

# practice q2

student = {}
student["name"] = input("enter  u r name : ")
student["marks"]= int(input("enter u r marks : "))

for i,marks in student.items():
    print(i,":",marks)

# practice q3

name = "imran"

freq = {}

for ch in name:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

# practice q4

number = {
    "num" : [1,2,3,4,5]
}
# for i in range(10):
#         n = int(input("enter a numbers "))
#         number["num"] = number.append(n)


KeyboardInterrupt
# print(number.items())

for i in number.values():
    for l in i:
        if l%2==0:
            print(l)

#  xhallange 
name = "my name is imran"

freq = {}

for word in name:
    if word in freq:
        freq[word] += 1
    else:
        freq[word]  = 1
print(freq)