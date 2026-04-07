f = open("test.txt","w")
f.write("helloe chudail\ntesting next line \t")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()