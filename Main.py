import turtle
import time

from Screen import window 
from Walls import walls, create_walls
from SnakeMovement import head, go_up, go_down, go_right, go_left, move
from GameOver import game_over
from NewSegment import NewSegment, segments
from Food import move_food, apple

game_state = "menu"
score = 0
delay = .1





score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()


menu_pen = turtle.Turtle()
menu_pen.hideturtle()
menu_pen.penup()
menu_pen.color("black")

head.hideturtle() 
apple.hideturtle()

def draw_homescreen():
    menu_pen.clear()
    menu_pen.goto(0, 80)
    menu_pen.write("Slither and Snack", align= "center", font=("Arial", 36))
    menu_pen.goto(0, -20)
    menu_pen.write("Press \"SPACE\" to start game!", align="center", font=("arial", 36))
    window.update()

def start_game():
    global game_state
    if game_state == "menu":
        game_state = "running"
        menu_pen.clear()

        create_walls()

        head.goto(250, -150)
        head.showturtle()
        apple.showturtle()
        move_food()
        score_display.clear()
        score_display.penup()
        score_display.goto(-480, 260)
        score_display.write("Score: " + str(score), align="left", font=("Arial", 16))
        window.update()

window.listen()
window.onkey(start_game, "space")

draw_homescreen()




game_running = True
while game_running == True:
    window.update()


    if game_state == "menu":
        draw_homescreen()
        time.sleep(.1)
        continue

    if game_state == "running":

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
            score_display.write("Score: " + str(score), align="left", font=("Arial", 16))
            for segment in segments:
                if head.distance(segment) < 10:
                    game_over(score)
                    head.direction = "stop"
                    game_running = False
        if score >= 5:
            delay = .08
        if score >= 10:
            delay = .05
        if score >= 15:
            delay = .02
        time.sleep(delay)
    
turtle.done()
