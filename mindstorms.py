import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")

    pat = turtle.Turtle()
    pat.shape("turtle")
    pat.color("red")
    pat.speed(1)
    patCounter = 0
    patPasses = 3
    while(patCounter <= patPasses):
        pat.forward(100)
        pat.right(90)
        patCounter = patCounter + 1

    window.exitonclick()

draw_square()
