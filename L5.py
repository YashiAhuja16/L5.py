import turtle as t  
import random as r

t.bgcolor("#87CEEB")
t.speed(100)
#ground
t.width (5)
t.penup()
t.goto(-400,-100)
t.pendown()
t.color("#FAD5A5")
t.begin_fill()
for x in range(2): 
    t.forward (800)
    t.right (90)
    t.forward(300)
    t.right(90)
t.end_fill()

#sand particles
for x in range(35):
    x = r.randint(-400,400)
    y=r.randint (-400,-100)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("#695b34")
    t.dot(5)


#pyramid 
t.penup()
t.goto(-200,-100)
t.pendown()
t.color("#695b34", "#FAD5A5")
t.begin_fill()
for x in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()


# pyramid lines 
t.penup()
t.goto(-160,-40)
t.pendown()
t.forward(122)

t.penup()
t.goto(-140,5)
t.pendown()
t.forward(80)

t.penup()
t.goto(-180,-75)
t.pendown()
t.forward(165)


# cactus
t.penup()
t.goto(165,-50)
t.pendown()
t.setheading (90)
t.color("#126109")
t.begin_fill()
t.forward(50)
t.setheading(0)
t.circle(20,180)
t.setheading(90)
t.forward(20)
t.circle(25,180)
t.forward(50)
t.setheading(180)
t.circle(20,180)
t.setheading(270)
t.forward(30)
t.end_fill()


#sand dune
t.penup()
t.goto(200,-100)
t.pendown()
t.setheading(90)
t.color("#FAD5A5")
t.begin_fill()
t.circle(50,180)
t.end_fill()

#sun
t.penup()
t.goto(200,250)
t.pendown()
t.color("#edf065")
for x in range (20):
    t.forward(70)
    t.right(150)

t.mainloop()



