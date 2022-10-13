#Xabien Loor
#CS175L
#Stop Sign

import math
import turtle

m = math
t = turtle
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10


t.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)


t.color('red')
for x in range(8):
    t.forward(100)
    t.left(45)

t.pencolor('black')
t.write('STOP', align='center', font=('Calibri',60))
turtle.done()

