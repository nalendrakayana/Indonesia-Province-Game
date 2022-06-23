import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("Indonesia Provinces Game")
image = "indonesia_map.gif"
screen.addshape(image)
screen.setup(800, 600)
t.shape(image)
t.penup()

data = pd.read_csv("provinces.csv")
province_list = data["province"].to_list()
total_province = len(province_list)
guessed_province = []
score = 0

while score < 34:
    answer_province = screen.textinput(title=f"{score}/{total_province} State Correct", 
                                            prompt="What's Another province's name? ").title()
    if answer_province == "Exit":
        missing_province = []
        for province in province_list:
            if province not in guessed_province:
                missing_province.append(province)
        df = pd.DataFrame(missing_province)
        df.to_csv("province_to_learn.csv")
        break
    if answer_province in province_list and answer_province not in guessed_province:
        score += 1
        province_data = data[data.province == answer_province]

        name_province = (province_data.no.item(), province_data.province.item())

        user_guess = t.Turtle()
        user_guess.hideturtle()
        user_guess.penup()

        user_guess.goto(x=int(province_data.x), y=int(province_data.y))
        user_guess.write(arg=province_data.no.item(), align="center", font=("Arial", 10, "normal"))
        user_guess.goto(province_data.x_name.item(), province_data.y_name.item())
        user_guess.write(name_province)
        guessed_province.append(answer_province)



























