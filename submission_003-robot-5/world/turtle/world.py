import turtle
import maze.crazy_maze as my_obstacles

position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars--=
min_y, max_y = -200, 200
min_x, max_x = -200, 200

# screen set up
set_up_screen = turtle.Screen()
set_up_screen.bgcolor("purple")

# border set up
square_border = turtle.Turtle()
square_border.penup()
square_border.setposition(-200, -200)
square_border.pendown()
square_border.pensize(5)
square_border.speed(100)

for border in range(4):
    square_border.fd(400)
    square_border.lt(90)
square_border.hideturtle()

# moving turtle
moving_robot = turtle.Turtle()
moving_robot.setheading(90)
moving_robot.color("green")
moving_robot.shape("triangle")
moving_robot.penup()
moving_robot.speed(1)
moving_robot.pendown()

# obstacles set up
obstacles = turtle.Turtle()

def place_obstacle(x,y):
    box = obstacles.clone()
    box.speed(80)
    box.color("pink")
    box.penup()
    box.shape("square")
    box.goto(x,y)

def draw_obstacles(obstacle_list):
  
    for obstacle in obstacle_list:
        place_obstacle(obstacle[0],obstacle[1])
        

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        moving_robot.fd(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        moving_robot.bk(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    moving_robot.right(90)
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    moving_robot.left(90)
    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)

def setup_world():
    maze = my_obstacles.maze_drawer()
    print(maze)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 'X':
                turtle.penup()
                turtle.goto(x * 10 - 195, y * 10 - 195)
                turtle.dot(size = 10)


setup_world()