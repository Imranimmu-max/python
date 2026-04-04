profile = {
    'name' : "imran",
    "age" : 19,
    "city" : "cbp"
}
print(profile)

for i in profile:
    print(i,":",profile[i])
    print(profile.keys())

print(profile.keys())
print(profile.values())
print(profile.items())

std = {}

std["name"] = input("enter ur name : ")
std["age"]  = int(input("enter u r age "))
std["city"] = input("enter u r city")

print(std)