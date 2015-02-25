__author__ = 'MR028042'

import turtle

window = turtle.Screen()
window.bgcolor('white')
window.exitonclick()

def draw_square(brad):

    for i in range (1,5):
        brad.forward(100)
        brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.circle(100)

def draw_art():
    for i in range(1,5):
        brad = turtle.Turtle()
        draw_square(brad)
        brad.right(10)
    #draw_circle()

draw_art()





