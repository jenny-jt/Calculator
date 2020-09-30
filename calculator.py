"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


While True:
    command = input ("Please input your calculation, starting with function(add, subtract, ultiply, divide, square, cube, power, mod), followed by the two numbers, all separated by spaces")
    command_list = command.split(' ')
    which_function = command_list[0]
    num1 = command_list[1]
    num2 = command_list[2] 
    