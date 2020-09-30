"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


While True:
    command = input ("Please input your calculation, starting with function(add, subtract, multiply, divide, square, cube, power, mod), followed by the two numbers, all separated by spaces")
    command_list = command.split(' ')
    which_function = command_list[0]
    num1 = command_list[1]
    num2 = command_list[2] 

    if which_function == "q":
        break
    elif which_function == "add":
        return add(num1,num2)
    elif which_function == "subtract":
        return subtract(num1,num2)
    elif which_function == "multiply":
        return multiply(num1,num2)
    elif which_function == "divide":
        return divide(num1,num2)
    elif which_function == "square":
        return square(num1,num2)
    elif which_function == "cube":
        return cube(num1,num2)
    elif which_function == "power":
        return power(num1,num2)
    elif which_function == "mod":
        return mod(num1,num2)