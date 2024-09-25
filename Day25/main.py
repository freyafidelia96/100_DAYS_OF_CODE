import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S states game")
image = "Day25/blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

states_data = pd.read_csv("Day25/50_states.csv")
score = 0


for i in range(50):
    another_state = screen.textinput(title= f"Guess a state  {score}/50", prompt="What is another state name").title()
    results = (states_data.state == another_state).any()

    if another_state == "Exit":
        break

    if results:
        each_state_data = states_data[states_data.state == another_state]
        state_index = states_data.index[states_data.state == another_state].item()
        states_data.drop(state_index, inplace=True)
        state_xcor = each_state_data.x.item()
        state_ycor = each_state_data.y.item()
        cordinates = (state_xcor, state_ycor)
        turtle.penup()
        turtle.goto(cordinates)
        turtle.write(arg=another_state, align="center", font=("Arial", 12, "normal"))

states_data.to_csv("Day25/States to learn.csv")
print(f"States you need to learn {states_data.state.to_list()}")
    


turtle.mainloop()