import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.color("black")
tim.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap, radius_of_circle):
    
    for _ in range(int(360/size_of_gap)):
       
        tim.circle(radius_of_circle)
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(radius_of_circle)

#For a given size of gap, draw a series of spirographs with different radius
def draw_radius_series_of_spirographs(size_of_gap,limiting_radius, delta_radius):
    
    for radius in range(10, limiting_radius, delta_radius):
        
        draw_spirograph(size_of_gap= size_of_gap ,radius_of_circle=radius)
        tim.color(random_color())
  
#For a given radius, draw a series of spirographs with different size of gaps    
def draw_angle_series_of_spirographs(limiting_size_of_gap, radius_of_circle, delta_angle):
    
    
    for angle in range(1, int(360/limiting_size_of_gap), delta_angle):
        
        draw_spirograph(size_of_gap=angle, radius_of_circle=radius_of_circle)
        tim.color(random_color())

#draw_spirograph(120, 100)

#draw_angle_series_of_spirographs(10, 50, 1)
#draw_radius_series_of_spirographs(51,500, 7)
draw_angle_series_of_spirographs(51, 300, 7)
screen = t.Screen()
screen.exitonclick()
