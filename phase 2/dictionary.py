profile = {
    'name' : "imran",
    "age" : 19,
    "city" : "cbp"
}
print(profile)

# for i in profile:
#     print(i,":",profile[i])


# print(profile.keys())

profile["name"] = "aliya"
print(profile)

print(profile.keys())
print(profile.values())
print(profile.items())

for i,values in profile():
    print(i,";",values)

