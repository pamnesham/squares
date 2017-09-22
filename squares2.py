#!python3

import turtle
lengthSide = turtle.numinput('','Enter a number: ')

def drawsquare(arg):
    turtle.speed(10)
    turtle.forward(int(arg))
    turtle.left(90)
    turtle.forward(int(arg))
    turtle.left(90)
    turtle.forward(int(arg))
    turtle.left(90)
    turtle.forward(int(arg))
    turtle.left(90)

def drawAll(amt):
    counter = 0
    while counter < amt:
        counter = counter + 1
        drawsquare(lengthSide)
        turtle.left(36)

def main():
    numSides = turtle.numinput()
    turtle.showturtle()
    drawAll(amt)

drawAll(10)

if __name__=='__main__':
    main()
