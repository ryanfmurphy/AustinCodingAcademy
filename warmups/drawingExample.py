from turtle import *

t = Turtle()
#t.shape('turtle')

'''
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
'''

'''
#to draw a square
forward(50)
setheading(270)
forward(50)
setheading(0)
backward(50)
setheading(90)
forward(50)
'''

'''
#to draw an octagon
clear()
goto(0,0)
setheading(0)
forward(50)
right(50)
forward(50)
setheading(270)
forward(50)
setheading(0)
left(50)
backward(50)
setheading(0)
backward(50)
left(-50)
backward(50)
setheading(90)
forward(50)
setheading(180)
right(-50)
backward(50)
'''

'''
#to draw a circle
clear()
goto(0,0)
setheading(0)
circle(200)
'''

def drawSquare(length, angle, t):

    t.forward(length)
    t.left(angle)
    t.forward(length)
    t.left(angle)
    t.forward(length)
    t.left(angle)
    t.forward(length)
    t.left(angle)


def createSpiral(distance, angle, numSpirals, t):
    for i in range(numSpirals):
        t.speed('fastest')
        t.forward(distance)
        t.left(angle)
        angle += 5

def drawSpiral(distance, angle, t):
    t.speed('fastest')
    while True:
        forward(distance)
        left(angle)
        distance += .01
        if distance == 5:
            break



#drawSquare(50, 90, t)
#createSpiral(50, 10, 100, t)
drawSpiral(0, 3, t)