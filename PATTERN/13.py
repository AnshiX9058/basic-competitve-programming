n=int(input("ENTER LIMIT : "))
for i in range(n,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()