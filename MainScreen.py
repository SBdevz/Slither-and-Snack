import turtle
import time
import random

#Screen
window = turtle.Screen()

window.setup(width = 1000, height = 600)

window.bgcolor("lightgreen")

window.title("Slither and Snack!")

window.tracer(0)

#Food - Moving Food / Stationary 

#Stationary Food 

stationary_food = turtle.Turtle()
stationary_food.speed(0)
stationary_food.shape("square")
stationary_food.color("red")
stationary_food.penup()
stationary_food.goto(-410,160)

#Stationary Food Eating

def move_food():
    while True:
        stationary_food_x = random.randint(-14, 14)*30
        stationary_food_y = random.randint(-8,8)*30
        stationary_food.goto(stationary_food_x, stationary_food_y)

        collision = False
        for wall in walls:
            if stationary_food.distance(wall) < 20:
                collision = True
                break
        if not collision:
            break

#Unstationary Food

#Snake Starting Head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(250,-150)
head.direction = "stop"

#Snake Segments

segments = []







# Movement

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
    head.setx(x + x_direction*15)
    head.sety(y + y_direction*15)
    

#keybinds

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")



#Wall Setup

#Cross at the MIDDLE
wall_positions = []

for x in range(-60, 61, 30):
    wall_positions.append((x, -40))
for y in range (-100, 21, 30):
    if y != -40:
        wall_positions.append((0, y))
#LSHAPE AT THE SIDES

#Top Left
for x in range(-440, -349, 30):
    wall_positions.append((x, 220))
for y in range(130, 220, 30):
    wall_positions.append((-440, y))
#Top Right
for x in range(350, 441, 30):
    wall_positions.append((x, 220))
for y in range(130, 220, 30):
    wall_positions.append((440, y))
#Bottom Left
for x in range(-440, -349, 30):
    wall_positions.append((x, -220))
for y in range(-220, -129, 30):
    wall_positions.append((-440, y))
#Bottom Right
for x in range(350, 441, 30):
    wall_positions.append((x, -220))
for y in range(-220, -129, 30):
    wall_positions.append((440, y))

walls = []

for pos in wall_positions:
    wall_segment = turtle.Turtle()
    wall_segment.shape("square")
    wall_segment.shapesize(stretch_wid=1.4, stretch_len= 1.4)
    wall_segment.color("black")
    wall_segment.penup()
    wall_segment.goto(pos)
    walls.append(wall_segment)

#Wall Collision

def game_over():
    window.clear()
    window.bgcolor("black")
    write = turtle.Turtle()
    write.hideturtle()
    write.color("red")
    write.penup()
    write.goto(0,0)
    write.write("You Lose", align="center", font=("Arial", 36, "bold"))

                
        

#Calls Move Food After Walls is Defined

move_food()

#Main Game Loop

game_running = True
while game_running == True:
    window.update()
    move()


    if (head.xcor() >= 500 or head.xcor() <= -500) or (head.ycor() >= 300 or head.ycor() <= -300):
        game_over()
        head.direction = "stop"
        game_running = False
    for wall in walls:
        if head.distance(wall) < 20:
            game_over()
            head.direction = "stop"  
            game_running = False 
    time.sleep(0.1)
    
turtle.done()
