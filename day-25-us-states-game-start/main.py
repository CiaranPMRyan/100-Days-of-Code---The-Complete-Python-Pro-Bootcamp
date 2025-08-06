import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list() # Pull out a whole column and convert to list. Use the ["Column names with spaces"]
                                    # formatting if there are spaces in the headings, otherwise the period is cleaner
answer_list = []
current_score = len(answer_list)

while len(answer_list) < 50:
    answer_state = screen.textinput(f"Score:{len(answer_list)}/50", prompt="Guess another State name!").title()

    if answer_state == "Exit":
        # list comprehension - new_list = [new_item for item in list if test]
        to_learn = [state for state in states_list if state not in answer_list]
        #for state in states_list:
            #if state not in answer_list:
                #to_learn.append(state)
        # print(to_learn)
        data_dict = {
            "States": to_learn
        }

        df = pandas.DataFrame(data_dict)
        df.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in states_list:
        answer_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # This pulls the exact row by comparing the answer(input) with the data in the column we specified (in this case .state)
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0])) # Use this type of format to pull out a column from a selected row
        t.write(state_data.state.iloc[0])


# TODO: Write the correct guess on to the map

# TODO: Record correct guess to a list

# TODO: Keep track of the score

# TODO: Use a loop to keep guessing (while final_score != 50 or something like that)