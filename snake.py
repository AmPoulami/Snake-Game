#import modules
import turtle
import time
import random

delay=0.1

#scores
score=0
high_score=0

segments=[]

#set up screen
win=turtle.Screen()
win.title("Snake Game")
win.bgcolor("Black")
win.setup(width=600,height=600)
win.tracer(0)

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
x=random.randint(-290,290)
y=random.randint(-290,260)
food.goto(x,y)

#scoreboards
sc=turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score: 0   High Score: 0",align="center",font=("Calibri",24,"bold","underline","italic"))

#Functions
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#keyboard bindings
win.listen()
win.onkeypress(go_up,'Up')
win.onkeypress(go_down,'Down')
win.onkeypress(go_left,"Left")
win.onkeypress(go_right,"Right")

#Main Game Loop
while True:
    win.update()

    #check collision with food(consume)
    if head.distance(food)<20:
        # move the food to random point within the screen boundary
        x=random.randint(-290,290)
        y=random.randint(-290,260)
        food.goto(x,y)

        #add a new segment to the head
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#ffffb3")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay-=.001
        #increase the score
        score+=10

        if score>high_score:
            high_score=score
        sc.clear()
        sc.color("#d9ff66")
        sc.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Calibri",24,"bold","underline","italic"))
    
    #move the segments along with head in reverse order
    for i in range(len(segments)-1,0,-1):
            x=segments[i-1].xcor()
            y=segments[i-1].ycor()
            segments[i].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    #check collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"
        #colors=random.choice(["red","blue","green","yellow"])
        #shape=random.choice(["square","circle"])

        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) 
        #clear the segments
        segments.clear()

        #reset score and delay
        score=0
        delay=0.1
        
        sc.clear()
        sc.color("white")
        sc.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Calibri",24,"bold","underline","italic"))

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #colors=random.choice(["red","blue","green","yellow"])
            #shape=random.choice(["square","circle"])
                
            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score=0
            delay=0.1

            #update the score
            sc.clear()
            sc.color("white")
            sc.write("Score: {}   High Score: {}".format(score,high_score),align="center",font=("Calibri",24,"bold","underline","italic"))
 
    time.sleep(delay)
win.mainloop()