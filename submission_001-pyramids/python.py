height=int(input("enter height;"))
for i in range(1,height+1):
    for j in range(1,height+1):
        if (i==height)or (j==1)or(i==j):
             print("*",end="")
        else:
             print(" ",end="")
    print()