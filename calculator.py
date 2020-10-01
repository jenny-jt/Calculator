"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    command = input ("Please input your calculation, starting with function(add, subtract, multiply, divide, square, cube, power, mod), followed by the two numbers, all separated by spaces")
    command_list = command.split(' ')
    which_function = command_list[0]
    num1 = int(command_list[1])
    num2 = int(command_list[2]) 

    if which_function == "q":
        break
    elif which_function == "add":
        print (float(add(num1,num2)))
    elif which_function == "subtract":
        print (float(subtract(num1,num2)))
    elif which_function == "multiply":
        print (float(multiply(num1,num2))
    elif which_function == "divide":
        print (float(divide(num1,num2)))
    elif which_function == "square":
        print (float(square(num1)))
    elif which_function == "cube":
        print (float(cube(num1)))
    elif which_function == "power":
        print (float(power(num1,num2)))
    elif which_function == "mod":
        print (float(mod(num1,num2)))