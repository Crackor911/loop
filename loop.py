import turtle

t = turtle.Pen()
t.speed(0)
for i in range(1280):
    t.forward(50)
    t.left(45)
    t.circle(i/0.33)

t.done()