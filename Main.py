import turtle
import time
from Screen import window
from Walls import walls
from SnakeMovement import head, go_up, go_down, go_right, go_left, move
from GameOver import game_over
from NewSegment import NewSegment
from Food import move_food, apple


#keybinds

window.listen()
from SnakeMovement import go_up, go_down, go_right, go_left, move
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")



#Wall Setup

#Cross at the MIDDLE

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
    time.sleep(0.1)
    
turtle.done()
