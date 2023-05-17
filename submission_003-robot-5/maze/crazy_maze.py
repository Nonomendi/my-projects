
import turtle
import random

def maze_drawer():
    maze = [
'XXXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXX',
'         X  X  X                 X    XX',
'X  XXXXXXX  X  X  X  XXXX  XXXXXXXXXXXXX',
'X           X     X     X              X',
'XXXX  XXXXXXXXXXX X  XXXX  XXXXXXXXX   X',
'X        X  X           X        X     X',
'X  X  XXXX  X  XX X  XXXX  XXXX  XXXXXXX',
'X  X     X        X     X  X           X',
'X XXXXX  X  X  XX XXXXXXXXXXXXX  X  XXXX',
'X  X        X  X              X  X  X  X',
'X  XXXXXXXXXXXXXX X  XXXXXXX  X  X  X  X',
'X              X  X     X     X  X     X',
'X  X  XXXXXXXXXX  X  X  XXXXXXX  XXX  XX',
'X  X           X     X  X              X',
'X  XXXXXXXXXX  XX XXXX  XXXX  X  XXXXXXX',
'X        X              X     X  X  X  X',
'XXXX  X  XXXXXXXX XXXX  XXXX  XXXX  X  X',
'X     X  X  X           X              X',
'X  X  X  X  XXXXX X  XXXX  X  XXXX  X XX',
'X  X  X        X        X  X  X     X  X',
'XXXX  XXXXXXX  XX X  X  XXXX  XXXXXXX  X',
'                                        ',
'XXXXXXX  X  X  X  XXXXXXXXXXXXX  X  X  X',
'X  X     X                 X     X     X',
'X  XXXXXXXXXXXXX  XXXXXXXXXX  X  XXXX  X',
'X  X        X  X              X  X  X  X',
'X  X  XXXXXXX  X  XXXX  XXXXXXX  X  X XX',
'X        X  X     X  X        X  X     X',
'XXXXXXX  X  X  X  X  XXXX  XXXXXXXXX  XX',
'X  X              X  X     X        X  X',
'X  XXXX  XXXXXXX  X  X  XXXX  X  X  XXXX',
'X           X  X  X     X     X  X     X',
'XXXXXXXXXX  X  X  XXXX  XXXX  XXXX  XXXX',
'X  X  X     X     X           X        X',
'X  X  X  XXXXXXX  XXXX  X  X  XXXXXXX XX',
'X           X  X  X     X  X     X     X',
'X  XXXXXXX  X  X  XXXXXXX  XXXXXXXXX  XX',
'X        X  X              X  X    X  XX',
'X  XXXX  XXXX  X  XXXXXXXXXX  X  X  X  X',
'X  X     X                       X  X  X',
'XXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXX',
]
    return maze 

obstacle_list = list()

def find_obstacles():
    global obstacle_list
    number_of_obstacles = random.randint(0,10)
    for i in range(number_of_obstacles):
        x_coordinate = random.randint(-200,200)
        y_coordinate = random.randint(-200,200)
        coordinates_tuple = (x_coordinate,y_coordinate)

        obstacle_list.append((coordinates_tuple))
    # print(obstacle_list)
    return obstacle_list

    
def inform_user(obstacle_list):
    if len(obstacle_list) > 0 :
        print("There are some obstacles:")
        for i in range(len(obstacle_list)):
            print(
                f"-At position {obstacle_list[i][0]},{obstacle_list[i][1]} (to {obstacle_list[i][0]+4},{obstacle_list[i][1]+4})"
            )            
def return_max_first(number_range):
    f,s = number_range[0],number_range[1]
    return s,f if f > s else f,s
# print(return_max_first([20,10]))

def position_closed(x,y):
    global obstacle_list
    # print(obstacle_list)
    obstacle_closed = False
    for coordinate in obstacle_list:
        x_coordinate = coordinate[0]
        y_coordinate = coordinate[1]
        obstacle_closed = x >= x_coordinate and x <=x_coordinate + 4 and  y >= y_coordinate and y <= y_coordinate + 4
        if obstacle_closed:
            break
        # print(obstacle_closed)
        return obstacle_list


def path_closed(x1,y1,x2,y2):
    if y1 == y2:
        x1 , x2 =  return_max_first([x1,x2])
        for x_cor in range(x1,x2):
            if position_closed(x_cor,y2):
                return True
    elif x1 == x2 :
        y1,y2 = return_max_first(y1,y2)
        for y_cor in range(y1,y2):
            if position_closed(y_cor,x2):
                return True
    return False



# def maze_cal(maze=[], maze_points=[]):
#     pass


# def draw_maze():
#     pass


