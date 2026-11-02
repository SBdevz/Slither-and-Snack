import turtle

wall_positions = []

for x in range(-60, 61, 30):
    wall_positions.append((x, -40))
for y in range (-100, 21, 30):
    if y != -40:
        wall_positions.append((0, y))
#LSHAPE AT THE SIDES

#Top Left
for x in range(-440, -349, 30):
    wall_positions.append((x, 220))
for y in range(130, 220, 30):
    wall_positions.append((-440, y))
#Top Right
for x in range(350, 441, 30):
    wall_positions.append((x, 220))
for y in range(130, 220, 30):
    wall_positions.append((440, y))
#Bottom Left
for x in range(-440, -349, 30):
    wall_positions.append((x, -220))
for y in range(-220, -129, 30):
    wall_positions.append((-440, y))
#Bottom Right
for x in range(350, 441, 30):
    wall_positions.append((x, -220))
for y in range(-220, -129, 30):
    wall_positions.append((440, y))

walls = []

for pos in wall_positions:
    wall_segment = turtle.Turtle()
    wall_segment.shape("square")
    wall_segment.shapesize(stretch_wid=1.4, stretch_len= 1.4)
    wall_segment.color("black")
    wall_segment.penup()
    wall_segment.goto(pos)
    walls.append(wall_segment)

