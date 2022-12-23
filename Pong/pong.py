# Author: Sasiru Ushan Hettiarachchi
# Source: Pong game
# Date: 5th Dec 2022

import turtle
import os

window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=800, height=600)
# stops the window from updating
window.tracer(0)

score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Main Title
pen = turtle.Turtle()
pen.speed(0)
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("0 | 0", align="center", font=("Courier", 30, "normal"))

# 2nd Title
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("red")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 200)



# move up paddle A 
def paddle_a_up():
	y = paddle_a.ycor()
	y = y+30
	paddle_a.sety(y)

# move down paddle A 
def paddle_a_down():
	y = paddle_a.ycor()
	y = y-30
	paddle_a.sety(y)

# move up paddle B
def paddle_b_up():
	y = paddle_b.ycor()
	y = y+30
	paddle_b.sety(y)

# move down paddle B
def paddle_b_down():
	y = paddle_b.ycor()
	y = y-30
	paddle_b.sety(y)

def move_ball():
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

def reset_paddle():
	paddle_b.goto(350, 0)
	paddle_a.goto(-350, 0)

def reset_ball():
	ball.goto(0, 0)
	ball.dx = 0
	ball.dy = 0

def reset_score():
	global score_a, score_b
	score_a = 0
	score_b = 0

def reset():
	reset_paddle()
	reset_ball()
	reset_score()
	pen.clear()
	pen1.clear()
	pen.write("{} | {}".format(score_a, score_b), align="center", font=("Courier", 30, "normal"))
	pen1.pendown()

def pause_on_win():
	reset_paddle()
	reset_ball()
	reset_score()

def play():
	reset()
	ball.dx = 2
	ball.dy = 2
	move_ball()
	ball_functionality()
		
def ball_functionality():
	if(ball.dx > 0 and ball.dy > 0):
			ball.dx += 0.002
			ball.dy += 0.002
			ball.setx(ball.xcor()+ball.dx)
			ball.sety(ball.ycor()+ball.dy)
	
	if(ball.dx < 0 and ball.dy < 0):
		ball.dx -= 0.002
		ball.dy -= 0.002
		ball.setx(ball.xcor()+ball.dx)
		ball.sety(ball.ycor()+ball.dy)




# listen for keyboard input
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(play, "p")


# Main
while (True):
	window.update()

	move_ball()

	if(score_a == 11 or score_b==11):
		if(score_a == 11):
			reset_score()
			pen.clear()
			pen1.clear()
			os.system("afplay ending_song.wav&")
			pen.write("Player A Won ! ", align="center", font=("Courier", 30, "normal"))
			pen1.write("Press p to play....", align="center", font=("Courier", 20, "normal"))
			pause_on_win()
		if(score_b == 11):
			reset_score()
			pen.clear()
			pen1.clear()
			os.system("afplay ending_song.wav&")
			pen.write("Player B Won ! ", align="center", font=("Courier", 30, "normal"))
			pen1.write("Press p to play....", align="center", font=("Courier", 20, "normal"))
			pause_on_win()

	
	move_ball()
	
	ball_functionality()

	if ball.ycor()>290:
		ball.sety(290)
		ball.dy = ball.dy * -1

	if(ball.ycor()< -290):
		ball.sety(-290)
		ball.dy = ball.dy * -1

	# left and right border
	if(ball.xcor()>390):
		ball.goto(0, 0)
		ball.dx = ball.dx * -1
		score_a +=1
		os.system("afplay score_point.wav&")
		pen.clear()
		pen.write("{} | {}".format(score_a, score_b), align="center", font=("Courier", 30, "normal"))

	if(ball.xcor()< -390):
		ball.goto(0, 0)
		ball.dx = ball.dx * -1 
		score_b +=1
		os.system("afplay score_point.wav&")
		pen.clear()
		pen.write("{} | {}".format(score_a, score_b), align="center", font=("Courier", 30, "normal"))

	# if ball hits the right paddle.
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50): 
		ball.setx(340)
		ball.dx *= -1
		# & is used to prevent sound delay
		os.system("afplay sound1.wav&")

	# if ball hits the left paddle.
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50): 
		ball.setx(-340)
		ball.dx *= -1
		# & is used to prevent sound delay
		os.system("afplay sound1.wav&")







	




