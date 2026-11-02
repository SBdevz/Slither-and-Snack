import turtle
import time

from Screen import window
from Walls import walls
from SnakeMovement import head, go_up, go_down, go_right, go_left, move
from GameOver import game_over
from NewSegment import NewSegment, segments
from Food import move_food, apple

move_food()

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
    if head.distance(apple) < 20:
        move_food()
        NewSegment()
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game_over()
            head.direction = "stop"
            game_running = False
    time.sleep(0.1)
    
turtle.done()
