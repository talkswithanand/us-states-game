import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game")

# Load image to screen.
image = "blank_states_img.gif"
screen.addshape(image)
# turtle shape converted to image.
turtle.shape(image)

file = pandas.read_csv("50_states.csv")
all_states = file.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="What's another state name?")
    guess = answer_state.title()
    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # to check if answer_state is one of the states in 50_states.csv file.
    if guess in all_states:
        # Create turtle to goto to that state x & y cord.
        guessed_state.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = file[file.state == guess]
        t.goto(int(data.x), int(data.y))
        t.write(guess)
        # OR t.write(data.state.item()) --- fetches only first word.



