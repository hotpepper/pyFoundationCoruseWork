import turtle
import math

def draw(color):
    window = turtle.Screen()
    window.bgcolor(color)
##    brad = turtle.Turtle()
##    for j in range(36):
##        drawSquare(brad, "turtle", "yellow", 100)
##        brad.right(10)
##
##    angie = turtle.Turtle()
##    drawCircle(angie, "arrow", "blue", 100)
    
    mina = turtle.Turtle()
    for k in range(72):
        drawTriangle(mina, "square", "orange", 100)
        mina.right(5)
    mina.right(90)
    mina.color("green")
    mina.forward(200)
    window.exitonclick()
    
    

def drawSquare(name, shape, color, size):
    name.shape(shape)
    name.color(color)
    name.speed(10)     
    for i in range(4):
        name.forward(size)
        name.right(90)
        
def drawCircle(name, shape, color, size):
    name.shape(shape)
    name.color(color)
    name.circle(size)
    

def drawTriangle(name, shape, color, size, angle = 90):
    name.shape(shape)
    name.color(color)
    name.speed(30)
    for i in range(3):
        #raw_input(i)
        name.forward(size)
        if i>0:
            name.left(angle/2)
            size = math.sqrt((size**2+size**2))
        name.left(angle)
    
draw("red")
