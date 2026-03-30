#practice q 
# Take a string
# Print number of vowels

n = "aliya"
count = 0
for i in n:
    if i == "a" and "e" and "i" and "o" and "u" : 
        count = count+1

print(count)
    
#practice q 2
# Take a string
# Reverse it

def rev():
    #using def for fun though 
    n="imran"
    # char=""
    # l = len(n)
    # for i in n:
    #     charecter = i[-1]
    # print(charecter)
    print("reverse is ",n[::-1])
rev()

# prctice q 3 
# Check if string is palindrome
# (madam → yes)

a = input("enter a string : ")

b = a[::-1]

if a == b :
    print("polindrone ")
else :
    print("not")

# practice q 4 
#challange
# Count number of words in a sentence

sem = "my name is imran "
print(len(sem))

