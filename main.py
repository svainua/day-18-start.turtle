from turtle import Turtle, Screen
import random

colors = ["green", "brown", "yellow", "blue", "red", "black", "grey", "green", "purple", "maroon"]
directions = [0, 90, 180, 270]

tim = Turtle()
tim.shape("turtle")
pan_size = 1
speed = 1

for _ in range(500):
    tim.forward(20)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))
    tim.pensize(pan_size)
    pan_size += 0.05
    tim.speed(speed)
    speed += 0.1

screen = Screen()
screen.exitonclick()


















