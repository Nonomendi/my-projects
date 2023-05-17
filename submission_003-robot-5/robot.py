# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 3 exercise.
"""
import world.text.world as my_world
# import maze.obstacles as obstacles
import maze.crazy_maze as obstacles
import sys

# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint','mazerun']
valid_edge =["top", "bottom", "left", "right"]
move_commands = valid_commands[3:]
history = []


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'mazerun':
        if arg1 in valid_edge or arg1 == "":
            return True

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed','').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed','')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""

def get_mazerun(robot_name,valid_edge):
    if valid_edge == "":
        valid_edge = "top"
    return True, (f'{robot_name}: I am at the {valid_edge} edge')

def edge_detect(command,robot_name):
    if command == ''+robot_name+': Sorry, I cannot go outside my safe zone.':
        stop = ''+robot_name+': Sorry, I cannot go outside my safe zone.'
        if my_world.x_coordinates == -100:
            print('Hal is at the left edge')
            my_world.x_coordinates = 0
            my_world.y_coordinates = 0
            return stop
        if my_world.position_x == 100:
            print('Hal is at the right edge')
            my_world.x_coordinates = 0
            my_world.y_coordinates = 0
            return stop
        if my_world.position_y == -200:
            print('Hal is at the bottom edge')
            my_world.x_coordinates = 0
            my_world.y_coordinates = 0
            return stop
        if my_world.position_y == 200:
            print('Hal is at the top edge')
            my_world.x_coordinates = 0
            my_world.y_coordinates = 0
            return stop
    
    


def mazerun_stuff(robot_name):
    command = 'forward'
    args = '50'
    while call_command(command,args,robot_name):
        command = 'forward'
        args = '50'
        if edge_detect == ''+robot_name+': Sorry, I cannot go outside my safe zone.':
            break

def get_commands_history(reverse, relativeStart, relativeEnd):
    """
    Retrieve the commands from history list, already breaking them up into (command_name, arguments) tuples
    :param reverse: if True, then reverse the list
    :param relativeStart: the start index relative to the end position of command, e.g. -5 means from index len(commands)-5; None means from beginning
    :param relativeEnd: the start index relative to the end position of command, e.g. -1 means from index len(commands)-1; None means to the end
    :return: return list of (command_name, arguments) tuples
    """

    commands_to_replay = [(name, args) for (name, args) in list(map(lambda command: split_command_input(command), history)) if name in move_commands]
    if reverse:
        commands_to_replay.reverse()

    range_start = len(commands_to_replay) + relativeStart if (relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
    range_end = len(commands_to_replay) + relativeEnd if  (relativeEnd is not None and (len(commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(commands_to_replay)
    return commands_to_replay[range_start:range_end]


def do_replay(robot_name, arguments):
    """
    Replays historic commands
    :param robot_name:
    :param arguments a string containing arguments for the replay command
    :return: True, output string
    """

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = get_commands_history(reverse, range_start, range_end)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = call_command(command_name, command_arg, robot_name)
        if not silent:
            print(command_output)
            my_world.show_position(robot_name)

    return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')


def call_command(command_name, command_arg, robot_name):
    if command_name == 'help':
        return do_help()
    elif command_name == 'forward':
        return my_world.do_forward(robot_name, int(command_arg))
    elif command_name == 'back':
        return my_world.do_back(robot_name, int(command_arg))
    elif command_name == 'right':
        return my_world.do_right_turn(robot_name)
    elif command_name == 'left':
        return my_world.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return my_world.do_sprint(robot_name, int(command_arg))
    elif command_name == 'replay':
        return do_replay(robot_name, command_arg)
    elif command_name == 'mazerun':
        print(f'{robot_name}: starting maze run..')
        return get_mazerun(robot_name, command_arg)
    return False, None


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    else:
        (do_next, command_output) = call_command(command_name, arg, robot_name)

    print(command_output)
    my_world.show_position(robot_name)
    add_to_history(command)

    return do_next

def allow_obstacles(obstacle_list):

    print("There are some obstacles:")
    for obstacle in obstacle_list:
        x = obstacle [0]
        y = obstacle [1]
        print(f"-At position {x},{y} (to {x +4},{y + 4})")


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    history.append(command)


def robot_start():
    """This is the entry point for starting my robot"""

    global  history,  position_x, position_y, current_direction_index, valid_edge

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    valid_edge =["top", "bottom", "left", "right"]
    position_x = 0
    position_y = 0
    current_direction_index = 0
    history = []

    obstacle_list = obstacles.find_obstacles()


    if 'simple_maze' in sys.argv:
        print(f'{robot_name}: Loaded simple_maze.')
    elif 'empty_maze' in sys.argv:
        print(f'{robot_name}: Loaded empty_maze.')
    elif 'single_obstacle_maze' in sys.argv:
        print(f'{robot_name}: single_obstacle_maze.')
    else:
        print(f'{robot_name}: Loaded obstacles.')
    if len(obstacle_list) > 0 :
        print("There are some obstacles:")
        for i in obstacles.obstacle_list:
            print(f"- At position {i[0]},{i[1]} (to {i[0]+4},{i[1]+4})")            
     
    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv [1] == "turtle":
        import world.turtle.world as my_world
        # my_world.draw_obstacles(obstacles.find_obstacles())
    elif len(sys.argv) == 3:
        import maze.crazy_maze as my_world
    else:
        import world.text.world as my_world
    robot_start()
