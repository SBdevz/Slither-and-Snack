import turtle 
from Screen import window

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(250,-150)
head.direction = "stop"

head_x = head.xcor()
head_y = head.ycor()

x_direction = 0
y_direction = 0

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")

def move():
    global x_direction
    global y_direction
    old_x = head.xcor()
    old_y = head.ycor()
    if head.direction == "up":
        x_direction = 0
        y_direction = 1
    if head.direction == "down":
        y_direction = -1
        x_direction = 0
    if head.direction == "right":
        x_direction = 1
        y_direction = 0
    if head.direction == "left":
        x_direction = -1
        y_direction = 0

    old_x = head.xcor()
    old_y = head.ycor()

    head.setx(old_x + x_direction*15)
    head.sety(old_y + y_direction*15)

    from NewSegment import segments

    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(old_x, old_y)


