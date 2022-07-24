# ShapeSpitter.py
# The terminal will ask for an input for a shape, and the program will spit out said shape.
# Improvements in the future can be (allowing user to select character to build shape with, case detection)
shapeList = []
program = True


def fetchShapeList():
    file = open("shapeList.txt", "r")
    for x in file:
        shapeList.append(x)
    file.close()
    for x in shapeList:
        print(x)


# Triangle: size 5
#      *        1
#     ***       3
#    *****      5
#   *******     7     
#  *********    9  

# Square: size 5 - basically print out double the size on one line, go to next line, repeat.
# **********    
# **********
# **********
# **********
# **********

# Rectangle: size 5 - Just print out stars same number as given size for the same rows as size
# *****
# *****
# *****
# *****
# *****

# Circle: size 5 - using an algorithm that draws a square outside, then check if a point lies within said square if it does print an asteri kif not print a space
# 
#         *********
#       **    |    **
#     **      |      **
#    *        |        *
#    *        |        *
#    *        .--------* 8 - to the right
#    *        |        *
#    *        |        *
#     **      |      **
#       **    |    **   always 
#         *********     5 | down (including the .) 9 asteriks at the base, 9-4 = 5 so we can say the base will be size + 4

def drawShape(item, size):
    spaces = ""
    output = ""
    print(f"Now attempting to print a {item} with a size of {size}: ") 
    if item == "triangle":
        output = "*"
        for x in range(size, 0, -1): 
            spaces = ""
            for j in range(x, 0, -1):
                spaces = spaces + " "
            print(spaces + output)
            output = output + "**"
        print("\n")

    elif item == "square":
        output = ""
        spaces = " "
        for x in range(2*size):
            output = output + "*"
        for x in range(size):
            print (spaces + output)

    elif item == "rectangle":
        spaces = " "
        for x in range(size):
            output = output + "*"
        for j in range(size):
            print(spaces + output)

    elif item == "circle":
        r = size
        squareSize = 2*r + 1
        for i in range(squareSize):
            for j in range(squareSize):
                x = i - r #x coord
                y = j - r #y coord
                if x*x + y*y <= r*r + 1:
                  print("*", end = " ")
                else:
                   print(" ", end = " ")
            print()

    else:
        print("That shape is not in our library currently! I will add it to the library to create this shape later on.")
        f = open("shapeList.txt", "a")
        f.write("\n" + item)
        f.close()

fetchShapeList()
while program == True:
    print("Welcome to Shape Spitter, a small practice program by Sasha Barazandeh.")
    shape = input("What kind of shape would you like?: ")
    if shape == "exit" or shape == "no":
        print("Thanks for using Shape Sitter, bye now!")
        program = False
    else:
        size = int(input(f"What size do you want the {shape} to be?: "))
        print(f'You have selected the shape {shape} with a size of {size}')
        drawShape(shape, size)
        ans = input("Would you like to draw another shape?: ")
        if ans == "no":
            program = False
            print("Thanks for using Shape Spitter, bye now!")