from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
#Detect collision with height of screen
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

#Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
       ball.bounce_x()

#Detect R_paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

#Detect R_paddle misses
    if ball.xcor() < -400:
        ball.reset_position()

screen.exitonclick()
