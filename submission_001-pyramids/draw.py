

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    while True:
         shape_param=input('Shape?: ').lower()
         if shape_param=='pyramid'or shape_param == 'triangle'or shape_param =='square':
             return shape_param
 



# TODO: Step 1 - get height (it must be int eger
def get_height():
    while True:
        height_param=input('Height?: ')
        if height_param.isdigit():
            return int(height_param)
             

# TODO: Step 2
def draw_pyramid(height, outline):
    
    if not outline:
        for i in range(0,height):
            for j in range(0,height-i-1):
                 print(" ",end='')
            for j in range(0,2*i+1):
                print('*',end='')
            print()

    else:
        


        for i in range(height):
            if i==0 or i == height-1:
                print(" "*(height-i-1)+ "*" * (2*i+1))
            else:
                print(" "* (height-i-1) + "*" + " "*(2*i-1)+ "*")




# TODO: Step 3
def draw_square(height, outline):
    if not outline:
         for i in range(0,height):
             for j in range(0,height):
                  print("*",end="")  
             print()    

    else:
    
        for i in range(height) :
            for j in range(height):
                if(i==0)or (i==height-1)or (j==0)or (j==height-1 ):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
                        


# TODO: Step 4
def draw_triangle(height, outline):
    if not outline:
        for i in range(0,height):
            for j in range(0,height-i-1):
                print(end='')
            for j in range(0,i+1):
                print("*",end='')
            print()

    else:
         for i in range(1,height+1):
             for j in range(1,i+1):
                  if (i==height)or (j==1)or(i==j):
                       print("*",end="")
                  else:
                       print(" ",end="")
             print()
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'square':
        draw_square(height, outline)
    elif shape =='pyramid':
       draw_pyramid(height, outline)
    elif shape== "triangle":
        draw_triangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline=input('Outline only? (y/N):')
    if outline =="y":
            return True
    elif outline =="n":
        return False
    elif outline=="":
        return False 



if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)
