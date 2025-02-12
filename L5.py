import turtle as t 
t.bgcolor("#87CEEB")

t.width (5)
t.speed(0)
t.penup()
t.goto(-400,-100)
t.pendown()
t.color("#FAD5A5")
t.begin_fill()
for x in range(2): 
    t.forward (1000)
    t.right (90)
    t.forward(300)
    t.right(90)
t.end_fill()
t.mainloop()
