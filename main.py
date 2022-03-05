import turtle
import pandas

screen = turtle.Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
list_name = data.state.tolist()
all_guess = []

while len(all_guess) < 50:
    guess = screen.textinput("guss", "guess the state").title()
    if guess in list_name:
        all_guess.append(guess)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        g_state = data[data.state == guess]
        t.goto(int(g_state.x), int(g_state.y))
        t.write(guess)
