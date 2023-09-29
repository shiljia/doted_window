import turtle
import random

t=turtle.Turtle()
t.ht()
t.speed(0)

l=['red','blue','green','black','pink']

while True:
    t.pu()
    t.goto(random.randrange(-350,350),random.randrange(-340,340))
    t.pd()
    t.dot(random.randrange(20,90),random.choice(l))
