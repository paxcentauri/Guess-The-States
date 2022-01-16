import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


def write_on_map(ans, x, y):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.goto(x, y)
    state.write(ans)


game_is_on = True
user_score = 0
states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()    
gtitle = ""
guessed_list = []


def generate_missing():
    missing_states = [states for states in states_list if states not in guessed_list]
    missing_dict = {
        "State Names": missing_states
    }
    missing_data = pandas.DataFrame(missing_dict)
    missing_data.to_csv("states_to_learn.csv")


while game_is_on is True:
    if len(guessed_list) == 0:
        gtitle = "Guess the States"
    else:
        gtitle = f"Guessed {user_score}/50"
    answer = screen.textinput(title=gtitle, prompt="Guess a US State name.")
    answer = answer.title()
    if answer == "Exit":
        generate_missing()
        game_is_on = False

    if answer in states_list and answer not in guessed_list:
        guessed_list.append(answer)
        user_score += 1
        rec = states_data[states_data.state == answer]
        ans_x = float(rec.x)
        ans_y = float(rec.y)
        write_on_map(answer, ans_x, ans_y)
    if user_score == 50:
        game_is_on = False



