number = {
"num" : [1,2,3,4,5]
}
for i in number.keys():
    print(i)
    for l in number.values():
        print(l)
        for j in l:
            if j%2==0:
                print("even",j)