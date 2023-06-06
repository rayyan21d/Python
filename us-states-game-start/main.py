#Install pandas and turtle
import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()

guessed_states = []

screen.addshape(image)
turtle.shape(image)

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data.state == answer_state]
        print(state_data)
        state.goto(int(state_data.x), int(state_data.y))
        state.write(state_data.state.item())
        
        
turtle.mainloop()
