import turtle
import random
import time

win = turtle.Screen()

tom = turtle.Turtle()
tom.penup()
tom.goto(-140, 140)
col_width = 20
row_width = 150
tom.speed(0)

endx = 150 * 15 - 140
for count in range(16):
    tom.write(count, align="center")
    tom.right(90)
    tom.pendown()
    tom.forward(row_width)
    tom.back(row_width)
    tom.left(90)
    tom.penup()
    tom.forward(col_width)
endx = tom.xcor() - col_width

adam = turtle.Turtle()
adam.color("red")
bob = turtle.Turtle()
bob.color("yellow")
charlie = turtle.Turtle()
charlie.color("green")
daryl = turtle.Turtle()
daryl.color("purple")
edward = turtle.Turtle()
edward.color("orange")

turtles_list = []
turtles_list.append(adam)
turtles_list.append(bob)
turtles_list.append(charlie)
turtles_list.append(daryl)
turtles_list.append(edward)
counter = 0;
xpos = -140
ypos = 110
num_turtles = 5

for start_turtle in turtles_list:
    start_turtle.penup()
    start_turtle.goto(xpos, ypos)
    ypos = ypos - 30
    start_turtle.shape("turtle")
    start_turtle.pendown()

t = turtle.Turtle()
stop = False
for moves in range(200 * num_turtles):
    turtlenum = random.randint(1, len(turtles_list)) - 1
    move = random.randint(1, 5)
    t = turtles_list[turtlenum]
    t.speed(0)
    t.pendown()
    t.forward(move * 2)
    if t.xcor() > endx:
        stop = True
        for x in range(3):
            for y in range(50):
                t.right(360 / 100)
            for z in range(2):
                t.hideturtle()
                time.sleep(.2)
                t.showturtle()
                time.sleep(.1)
        # time.sleep()
        break
win.exitonclick()