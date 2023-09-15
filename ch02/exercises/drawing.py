import turtle 

number_sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))

tu = turtle.Turtle()
screen = turtle.Screen()
tu.shape("turtle")
tu.color("blue")
int_angle = 360 / number_sides
colors = ["blue", "green", "yellow", "red"]

for i in colors:
    tu.color(i)
    for _ in range(number_sides):
        tu.forward(length)
        tu.right(int_angle)

screen.exitonclick() 