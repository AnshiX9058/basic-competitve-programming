n=int(input("ENTER LIMIT : "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()