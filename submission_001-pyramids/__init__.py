height=int(input("enter height:"))
for i in range(height) :
     for j in range(height):
         if(i==0)or (i==height-1)or (j==0)or (j==height-1):
              print("*",end="")
         else:
              print(" ",end="")
     print()