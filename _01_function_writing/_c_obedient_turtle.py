"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

rob = turtle.Turtle()


def square():
    for i in range(4):
        rob.forward(50)
        rob.right(90)


def triangle():
    for i in range(3):
        rob.forward(50)
        rob.right(120)

if __name__ == '__main__':
    shape = simpledialog.askstring('', "What shape do you want")
    if shape == "square":
        square()
    elif shape == "triangle":
        triangle()
    else:
        print("idk")
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass

