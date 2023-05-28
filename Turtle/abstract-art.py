import colorgram
import turtle as t
import random

# Extract 20 colors from an image.
colors=colorgram.extract('./assets/mg4.jpg',20)
rgb_colors=[]

for color in colors:

    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    
    color_tuple=(r,g,b)
    rgb_colors.append(color_tuple)
    
    
#Initializing the turtle
tim=t.Turtle()
tim.shape("turtle")
tim.color("black")
t.colormode(255)

tim.penup()
tim.goto(-250,-250)

#Drawing the dots
for i in range(10):
    for j in range(10):
        tim.dot(20,random.choice(rgb_colors))
        tim.penup()
        tim.forward(50)
    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

screen=t.Screen()
screen.exitonclick()    
    
    
        