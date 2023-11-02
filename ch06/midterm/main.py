import turtle
import random

top = turtle.Turtle()
bottom = turtle.Turtle()
dots = turtle.Turtle()
screen = turtle.Screen()

top.color("red")
bottom.color("yellow")
dots.color("white")

TOP_RADIUS = 100
TOP_WIDTH = 50
TOP_LENGTH = 100
DOTS_RADIUS = 5

def draw_mushroom(radius, length, width):
    top.penup()
    top.goto(radius, 0)
    top.setheading(90)
    top.pendown()
    
    top.fillcolor("red")
    top.begin_fill()
    top.circle(radius, 180)
    top.left(90)
    top.forward(2 * radius)
    top.end_fill()
    top.hideturtle()
    
    bottom.penup()
    bottom.goto(25, 0)
    bottom.setheading(180)
    bottom.pendown()
    
    bottom.fillcolor("yellow")
    bottom.begin_fill()
    
    for _ in range(2):
        bottom.forward(length)
        bottom.left(90)
        bottom.forward(width)
        bottom.left(90)
        
    bottom.end_fill()
    bottom.hideturtle()
    
    dots.penup()
    
    return radius
    
def draw_spots(radius):
    dots.penup()
    for _ in range(7):
        x = random.uniform(-100, 100)
        y = random.uniform(0, 100)
        dots.goto(x, y)
        dots.pendown()
        dots.fillcolor("white")
        dots.begin_fill()
        dots.circle(radius, 360)
        dots.end_fill()
        dots.penup()
    
    dots.hideturtle()
    
    return radius

def main():   
    mushroom_radius = draw_mushroom(TOP_RADIUS, TOP_WIDTH, TOP_LENGTH)
    dots_radius = draw_spots(DOTS_RADIUS)

    print("The radius of the top mushroom part is", mushroom_radius)
    print("The radius of the dots on the mushroom is", dots_radius)
    
    screen.exitonclick()

main()