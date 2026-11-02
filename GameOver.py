import turtle
from Screen import window

def game_over(finalScore):
    window.clear()
    window.bgcolor("black")
    write = turtle.Turtle()
    write.hideturtle()
    write.color("red")
    write.penup()
    write.goto(0,0)
    write.write("Game Over", align="center", font=("Arial", 36, "bold"))
    write.goto(0, -50)
    write.write(f'Score: {finalScore}', align="center", font=("Arial", 16, "normal"))


