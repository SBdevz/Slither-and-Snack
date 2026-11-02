import turtle
from Screen import window

def game_over():
    window.clear()
    window.bgcolor("black")
    write = turtle.Turtle()
    write.hideturtle()
    write.color("red")
    write.penup()
    write.goto(0,0)
    write.write("You Lose", align="center", font=("Arial", 36, "bold"))

