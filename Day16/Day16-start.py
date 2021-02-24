from turtle import Turtle, Screen
import random

timmy = Turtle()                # creating a turtle object
print(timmy)

my_screen = Screen()            # creating a screen object
print(my_screen.canvheight)     # checking the height of the canvas of Screen
print(my_screen.canvwidth)      # checking the width of the canvas of Screen

# changing the shape of the timmy(turtle)
colours = ['aquamarine4', 'green', 'blue4', 'chartreuse', 'deeppink', 'cyan', 'black', 'coral']
timmy.shape("turtle")
for i in range(50):
    timmy.color(random.choice(colours))
    timmy.forward(20 + i)
    timmy.backward(20 + i)
    timmy.left(90)
    timmy.forward(5)
    timmy.right(90)
for i in range(50):
    timmy.color(random.choice(colours))
    timmy.right(180)
    timmy.forward(20 + i)
    timmy.backward(20 + i)
    timmy.left(90)
    timmy.forward(5)
    timmy.left(90)


# making the graphics screen exit on click
my_screen.exitonclick()
