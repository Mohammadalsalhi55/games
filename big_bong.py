import turtle

wind=turtle.Screen()
wind.title("ping pong by heda")
wind.bgcolor("gray")
wind.setup(width=800,height=600)
wind.tracer(0)


paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(+350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1:0 player 2:0", align="center",font=("courier",24,"normal"))

def paddle1_up():
    y=paddle1.ycor()
    y+=20
    paddle1.sety(y)

def paddle1_down():
    y=paddle1.ycor()
    y-=20
    paddle1.sety(y)

def paddle2_down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)

def paddle2_up():
    y=paddle2.ycor()
    y+=20
    paddle2.sety(y)

wind.listen()
wind.onkeypress(paddle1_up,"w")
wind.onkeypress(paddle1_down,"s")
wind.onkeypress(paddle2_up,"Up")
wind.onkeypress(paddle2_down,"Down")


while True:
    wind.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() >290:
     ball.sety(290)
     ball.dy *=-1
    if ball.ycor() <-290:
      ball.sety(-290)
      ball.dy *=-1
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
        score1 +=1
        score.clear()
        score.write("player 1:{} player 2:{}".format(score1,score2), align="center",font=("courier",24,"normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *=-1
        score2 +=1
        score.clear()
        score.write("player 1:{} player 2:{}".format(score1,score2), align="center",font=("courier",24,"normal"))

    if (ball.xcor()> 340 and ball.xcor()<350)and(ball.ycor()<paddle2.ycor() + 40 and ball.ycor()>paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1
    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor()<paddle1.ycor() + 40 and ball.ycor()> paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1

