#!python3

import turtle

#Pop-up window asks user for input determining square size
lengthSide = turtle.numinput('','Enter a number for square size: ')

#function for drawing a single square
def drawsquare(arg):
    turtle.delay(0)
    turtle.forward(int(arg))
    turtle.left(90)
    turtle.forward(int(arg))
    turtle.left(90)
    turtle.forward(int(arg))
    turtle.left(90)
    turtle.forward(int(arg))
    turtle.left(90)

#function that determines how many squares will be drawn
def drawAll(amt):
    counter = 0
    while counter < amt:
        counter = counter + 1
        drawsquare(lengthSide)
        turtle.left(36)

#Shows the turtle window and determines amount of squares to draw
def main():
    turtle.showturtle()
    drawAll(10)

if __name__=='__main__':
    main()
