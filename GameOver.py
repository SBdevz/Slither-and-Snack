import turtle
from Screen import window
from Main import score

def game_over():
    window.clear()
    window.bgcolor("black")
    write = turtle.Turtle()
    write.hideturtle()
    write.color("red")
    write.penup()
    write.goto(0,0)
    write.write("Game Over", align="center", font=("Arial", 36, "bold"))
    write.goto(0, -50)
    write.write(f'Score: {score}', align="center", font=("Arial", 16, "normal"))


