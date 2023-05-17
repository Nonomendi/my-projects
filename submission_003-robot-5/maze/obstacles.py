# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------import random 

import random

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
        return obstacle_closed


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
