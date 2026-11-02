import turtle
import random
from Walls import walls

apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("red")
apple.penup()
apple.goto(-410,160)

def move_food():
    while True:
        stationary_food_x = random.randint(-28, 28)*15
        stationary_food_y = random.randint(-16,16)*15
        apple.goto(stationary_food_x, stationary_food_y)

        collision = False
        for wall in walls:
            if apple.distance(wall) < 40:
                collision = True
                break
        if not collision:
            break