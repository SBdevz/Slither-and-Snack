import turtle
from SnakeMovement import head, head_x, head_y

total_segments = 1
segments = []

def NewSegment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.penup()
    global total_segments
    total_segments += 1
    if len(segments) > 0:
        x = segments[-1].xcor() 
        y = segments[-1].ycor() 
    else:
        x = head.xcor() - 15
        y = head.ycor()
    new_segment.goto(x, y)
    segments.append(new_segment)
    
        
