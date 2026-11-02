import turtle 

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
def move():
    global x_direction
    global y_direction
    x = head.xcor()
    y = head.ycor()
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


