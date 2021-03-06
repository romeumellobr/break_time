import turtle
import random

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_circle(some_turtle):
    randCircle = random.randrange(-100, 100)
    some_turtle.circle(randCircle)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #Create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("green", "red", "white")
    brad.speed(1)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
        
    window.exitonclick()

draw_art()
