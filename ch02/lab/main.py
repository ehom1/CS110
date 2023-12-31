import turtle  # 1. import modules 
import random
import pygame
import math 

# Part A
window = turtle.Screen()  # 2. Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3. Create two turtles 
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pens so we don't get lines 
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

rand1 = random.randint(1,100)  # Race 1
rand2 = random.randint(1,100)
michelangelo.forward(rand1)
leonardo.forward(rand2)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

for _ in range(10):  # Race 2
    random1 = random.randrange(1,11)
    michelangelo.forward(random1)  
    
for _ in range(10):
    random2 = random.randrange(1,11)
    leonardo.forward(random2)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
window.exitonclick()

# Part B
pygame.init()
window = pygame.display.set_mode((800, 600))
window.fill("white")

colors = ("darkgreen")
num_sides = [3, 4, 6, 20, 100, 360]
side_length = 100
xpos = 400
ypos = 300

for j in num_sides:
    points = []
    for i in range(j):
        angles = 360 / j
        radians = math.radians(angles * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append((x,y))
    
    pygame.draw.polygon(window, colors, points)
    pygame.display.flip()
    pygame.time.wait(500)
    window.fill("white")
    pygame.display.flip()
    pygame.time.wait(1000)