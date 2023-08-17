import turtle,pandas

screen = turtle.Screen()
screen.setup(730,500)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_states = []

while len(guessed_states) <50:
    guess_state = screen.textinput(title=f" {len(guessed_states)}/50 States Correct", prompt="Guess the state: ").capitalize()

    if guess_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
        

    if guess_state in all_states:
        guessed_states.append(guess_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == guess_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(guess_state)
