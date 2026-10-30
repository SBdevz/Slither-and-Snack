import turtle
import random

#Screen
window = turtle.Screen()

window.setup(width = 600, height = 600)

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
stationary_food.goto(0,100)



#Unstationary Food

#Snake Starting Head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,20)
head.direction = "stop"




# Creating Functions

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 15)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 15)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 15)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 15)

#keybinds

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")

#Main Game Loop

while True:
    move()


    window.update()
turtle.done()
