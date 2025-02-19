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
t.mainloop()
