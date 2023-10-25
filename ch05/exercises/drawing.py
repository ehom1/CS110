import turtle 

sides = int(input("How many sides? "))
length = int(input("What length? "))
t = turtle.Turtle()
s = turtle.Screen()

t.color("green")
t.shape("turtle")

def draw_eq_shape(pen, num_sides, length = 50):
    angle = 360 / num_sides
    for _ in range(num_sides):
        pen.forward(length)
        pen.right(angle)
        
draw_eq_shape(t, sides, length)

s.exitonclick()
        