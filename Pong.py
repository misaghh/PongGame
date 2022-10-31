#Two player pong game 

# import turtle;

# wn = turtle.Screen()

# wn.title("Pong game")
# #background color
# wn.bgcolor("black")
# #window size
# wn.setup(width=800, height=600)
# #speed of game
# wn.tracer(0)


# #adding paddles
# #paddle A
# paddleA = turtle.Turtle()
# paddleA.speed(0)  #max speed 
# paddleA.shape("square")
# paddleA.color("white")
# paddleA.penup()
# paddleA.goto(-350,0)
# paddleA.shapesize(stretch_wid=5, stretch_len=1)

# #paddle B
# paddleB = turtle.Turtle()
# paddleB.speed(0)  #max speed 
# paddleB.shape("square")
# paddleB.color("white")
# paddleB.penup()
# paddleB.goto(350,0)
# paddleB.shapesize(stretch_wid = 5, stretch_len = 1)

# #ball
# ball = turtle.Turtle()
# ball.speed(0)  #max speed 
# ball.shape("square")
# ball.color("white")
# ball.penup()
# ball.goto(0, 0)
# ball.dx = 2
# ball.dy = 2

# #pen 
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0,260)
# pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# #Score
# scoreA = 0
# scoreB = 0



# # paddle movement function
# def paddleA_up():
#     #getting y coordinate
#     y = paddleA.ycor()
#     y += 20
#     paddleA.sety(y)

# def paddleA_down():
#     #getting y coordinate
#     y = paddleA.ycor()
#     y -= 20
#     paddleA.sety(y)

# def paddleB_up():
#     #getting y coordinate
#     y = paddleB.ycor()
#     y += 20
#     paddleB.sety(y)

# def paddleB_down():
#     #getting y coordinate
#     y = paddleB.ycor()
#     y -= 20
#     paddleB.sety(y)


# #keyboard binding, based w,s, and up,down Keys
# wn.listen()
# wn.onkeypress(paddleA_up, "w")
# wn.onkeypress(paddleA_down,"s")
# wn.onkeypress(paddleB_up, "Up")
# wn.onkeypress(paddleB_down,"Down")




# #Main game loop
# while True:
#     wn.update()

#     #Moving the ball
#     ball.setx(ball.xcor() + ball.dx)
#     ball.sety(ball.ycor() + ball.dy)

#     #setting borders for the ball
#     if ball.ycor() > 290:
#         ball.sety(290)
#         ball.dy *= -1

#     elif ball.ycor() < -290:
#         ball.sety(-290)
#         ball.dy *= -1

#     if ball.xcor() > 390:
#         ball.goto(0,0)
#         ball.dx *= -1
#         scoreA += 1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))



#     elif (ball.xcor() < -390):
#         ball.goto(0,0)
#         ball.dx *= -1
#         scoreB += 1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        
    
#     # Ball boucing off paddle
#     if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40):
#         ball.setx(340)
#         ball.dx *= -1

#     if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40):
#         ball.setx(-340)
#         ball.dx *= -1
   


##CORRECT CODE BELOW

import turtle
#import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)
paddle_a.fillcolor("#A2C5EB")

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.fillcolor("#414F5E")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold italic"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold italic"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold italic"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        # os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        # os.system("afplay bounce.wav&")
    
    

