# Program for circuler pattern
'''
    Author : Samadhan Gaikwad.
    Software Developer
    Location: Pune.
'''

import turtle
# s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(5)
t.goto(-300, 0)
for i in range(5):
    for j in ["magenta", "red", "blue", "green", "cyan", "yellow", "white", "purple"]:
        t.color(j)
        t.pensize(3)
        t.circle(150)
        t.forward(20)
        t.speed(11)
t.hideturtle()
turtle.done()
