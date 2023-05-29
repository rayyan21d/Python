from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.pencolor("aquamarine")
tim.pensize(15)


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)www
    
def turn_left():
    tim.left(10)
    
def turn_right():
    tim.right(10)
 
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
 
#Listens to key inputs    
screen.listen()

#Handles key inputs
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear, "c")

#prevents window from closing
screen.exitonclick()
