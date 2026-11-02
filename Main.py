import turtle
import time

from Screen import window 
from Walls import walls
from SnakeMovement import head, go_up, go_down, go_right, go_left, move
from GameOver import game_over
from NewSegment import NewSegment, segments
from Food import move_food, apple

score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
move_food()
score_display.goto(-480, 260)
score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

game_running = True
while game_running == True:
    window.update()
    move()
    if (head.xcor() >= 500 or head.xcor() <= -500) or (head.ycor() >= 300 or head.ycor() <= -300):
        game_over(score)
        head.direction = "stop"
        game_running = False
    for wall in walls:
        if head.distance(wall) < 20:
            game_over(score)
            head.direction = "stop"  
            game_running = False 
    if head.distance(apple) < 20:
        move_food()
        NewSegment()
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))
        for segment in segments:
            if head.distance(segment) < 10:
                game_over(score)
                head.direction = "stop"
                game_running = False
    time.sleep(0.1)
    
turtle.done()
