from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from gameover import Game_over
from score import Score
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))   
ball = Ball()

player_score = Score((-60, 250))
cpu_score = Score((40, 250))

center_line = Turtle()
center_line.hideturtle()
center_line.penup()
center_line.setpos(0, -270)
center_line.pendown()
center_line.color('white')
center_line.left(90)
center_line.forward(540)

screen.listen()
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=r_paddle.rup, key="i")
screen.onkey(fun=r_paddle.rdown, key="k")        
game_is_on = True
speed = 0.01
while game_is_on:
    ball_is_out = False
    if ball_is_out == True:
        game_is_on = False
    time.sleep(speed)
    screen.update()
    ball.move()
    # Detect collision wall:
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.shapesize(stretch_wid=1, stretch_len=-1.5, outline=1)
        ball.bounce()
        ball.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        print(ball.xcor())
    elif ball.xcor() == -330 and ball.distance(l_paddle) < 60:
        ball.shapesize(stretch_wid=-1.5, stretch_len=-1, outline=1)
        speed *= 0.9
        ball.hit_x()
        ball.shapesize(stretch_wid=1, stretch_len=-1, outline=1)        
    elif ball.xcor() == 330 and ball.distance(r_paddle) < 60:
        ball.shapesize(stretch_wid=-1.5, stretch_len=-1, outline=1)
        speed *= 0.9
        ball.hit_x()
        ball.shapesize(stretch_wid=1, stretch_len=-1, outline=1)
    elif ball.xcor() > 390: 
        player_score.increase_score()
        if player_score.score_count() == 10:
            game_over = Game_over()
            game_is_on = False
        else:
            ball.hideturtle()
            ball.home()
            ball.showturtle()
            ball.new_move()        
    elif ball.xcor() < -390:
        cpu_score.increase_score()
        if cpu_score.score_count() == 10:
            game_over = Game_over()
            game_is_on = False
        else:
            ball.hideturtle()
            ball.home()
            ball.showturtle()
            ball.new_move()
        






















screen.exitonclick()