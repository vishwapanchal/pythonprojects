from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400)
screen.title("The Turtle Game")
rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour")

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(rainbow_colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"User have won, The {winning_colour} turtle have won the race!")
            else:
                print(f"User have lost, The {winning_colour} turtle have lost the race!")

        random_number = random.randint(1, 10)
        turtle.forward(random_number)

screen.exitonclick()
