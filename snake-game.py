import turtle
import time
import random

delay=0.1
sc=0
hs=0
bodies=[]
#Create a body of a snake
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(width=500,height=500)

#Crewating a head
h=turtle.Turtle()
h.speed(0)
h.shape("circle")
h.color("red")
h.fillcolor("red")
h.penup()
h.goto(0,0)
h.direction="stop"


f=turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("blue")
f.fillcolor("red")
f.penup()
f.ht()
f.goto(200,150)
f.st()



sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-200,240)
sb.write("Score : 0  |  Highest : 0")


def moveUp():
  if h.direction!="down":
    h.direction="up"


def moveDown():
  if h.direction!="up":
    h.direction="down"


def moveLeft():
  if h.direction!="right":
    h.direction="left"


def moveRight():
  if h.direction!="left":
    h.direction="right"        



def moveStop():
  h.direction="stop"


def move():
  if h.direction=="up":
    y=h.ycor()
    h.sety(y+20)

  if h.direction=="right":
    x=h.xcor()
    h.setx(x+20)

  if h.direction=="down":
    y=h.ycor()
    h.sety(y-20)  

  if h.direction=="left":
    x=h.xcor()
    h.setx(x-20)  



s.listen()   
s.onkey(moveUp,"Up") 
s.onkey(moveDown,"Down") 
s.onkey(moveLeft,"Left") 
s.onkey(moveRight,"Right") 
s.onkey(moveStop,"space") 

#main loop
while True:
  
  s.update()
  if h.xcor()>240:

    h.setx(-240)

  if h.xcor()<-240:
    h.setx(240)

  if h.ycor()>240:
    h.sety(-240)

  if h.ycor()<-240:
    h.sety(240)

  #food
  if h.distance(f)<20:
    x=random.randint(-240,240)
    y=random.randint(-240,240)
    f.goto(x,y)
    body=turtle.Turtle()
    body.speed(0)
    body.penup()
    body.shape("square")
    body.color("green")
    bodies.append(body)


    sc=sc+10
    delay=delay-0.001
    
    if sc>hs:
      hs=sc


    sb.clear()
    sb.write(f"score : {sc}   | Highest : {hs}") 

  # move 
  for i in range(len(bodies)-1,0,-1):
    x=bodies[i-1].xcor()
    y=bodies[i-1].ycor()
    bodies[i].goto(x,y)
  if len(bodies)>0:
    x=h.xcor()
    y=h.ycor()
    bodies[0].goto(x,y)
  move()


  for b in bodies:
    if b.distance(h)<20:
      time.sleep(1)
      h.goto(0,0)
      h.direction="stop"

      for body in  bodies:
        body.ht()
      bodies.clear()
      sc=0
      delay=0.1
      sb.clear()

      sb.write(f"Score : {sc}  | Highest : {hs}")
  time.sleep(delay)
s.mainloop()        
turtle.done()
