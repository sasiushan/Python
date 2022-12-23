from ast import alias
import turtle
import random
import os

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.shapesize(stretch_wid=1.2, stretch_len=1.2)
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(random.randint(-300, 200), random.randint(-300, 200))


scoreDesc = turtle.Turtle()
scoreDesc.speed(0)
scoreDesc.color("white")
scoreDesc.penup()
scoreDesc.hideturtle()
scoreDesc.goto(0, 250)
scoreDesc.write("Score: 0 | High Score: 0", align="center", font=("Courier", 24, "normal"))

score = 0
highScore = 0
segment = []

# this logic is down to prevent the snake from crashing into itself
def up():
    if snake.direction!="down":
        snake.direction="up"

def down():
    if snake.direction!="up":
        snake.direction="down"

def right():
    if snake.direction!="left":
        snake.direction="right"

def left():
    if snake.direction!="right":
        snake.direction="left"


window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(left, "a")
window.onkeypress(right, "d")


snake_blocks = []
game_over = False
speed = 3
flag = 1

b = turtle.Turtle()
b.speed(0) 
b.shape("square")
b.color("red")
b.penup()
b.goto(snake.xcor(), snake.ycor())

# snake_blocks.append(b)

while not game_over:
    window.update()

    # snake_blocks.append(b)

    if(flag ==1):
        for x in range(20):
            snake_blocks.append(b)
        flag=0



    # check if the snake has hit the boundaries
    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 300 or snake.ycor() < -300:
        snake.goto(0,0)
        snake.direction = "stop"
        score = 0
        speed = 3
        flag = 1
        for seg in snake_blocks:
            seg.goto(1000, 1000)
            seg.clear()
        snake_blocks.clear()
        scoreDesc.clear()
        os.system("afplay ending_song.wav&")
        scoreDesc.write("Score: {} | High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    if snake.direction == "up":
        snake.sety(snake.ycor() + speed)
    if snake.direction == "down":
        snake.sety(snake.ycor() - speed)
    if snake.direction == "left":
        snake.setx(snake.xcor() - speed)
    if snake.direction == "right":
        snake.setx(snake.xcor() + speed)

    # speed of the snake
    if score == 18:
        speed = 4
    if score == 29:
        speed = 5
    if score == 41:
        speed = 6
    if score == 59:
        speed = 7
    if score == 72:
        speed = 8
    if score == 95:
        speed = 9
    if score == 110:
        speed = 10
    if score == 130:
        speed = 11
    if score == 152:
        speed = 12


    # check if the snake has eaten the food
    if snake.distance(food) < 20:

        os.system("afplay sound1.wav&")
        
         # Create a new block for the snake
        new_block = turtle.Turtle()
        new_block.speed(0) 
        new_block.shape("square")
        new_block.color("red")
        new_block.penup()
        new_block.goto(snake.xcor(), snake.ycor())

        snake_blocks.append(new_block)

        score = score+1
        if(score>highScore):
            highScore=score
        scoreDesc.clear()
        scoreDesc.write("Score: {} | High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))
        food.goto(random.randint(-250, 300), random.randint(-250, 300))

    for index in range(len(snake_blocks)-1, 0, -1):
        x = snake_blocks[index-1].xcor()
        y = snake_blocks[index-1].ycor()
        snake_blocks[index].goto(x, y)
    if len(snake_blocks) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_blocks[0].goto(x, y)







    