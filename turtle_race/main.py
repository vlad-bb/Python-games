import random
from turtle import Turtle, Screen

colors = ['red', 'green', 'pink', 'blue', 'yellow', 'orange']


def create_turtle() -> list:
    position_y = [-100, -50, 0, 50, 100, 150]
    list_turtle = []
    for i in range(6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-250, y=position_y[i])
        list_turtle.append(new_turtle)
    return list_turtle


def game(user_bet_, all_turtle: list[Turtle]):
    is_rase_on = True if user_bet_ in colors else False
    while is_rase_on:
        for turtle in all_turtle:
            if turtle.xcor() >= 230:
                is_rase_on = False
                if user_bet_ == turtle.color()[0]:
                    print(f'You won. The winner is {turtle.color()[0]}')
                else:
                    print(f'You lose. The winner is {turtle.color()[0]}')
            turtle.forward(random.randrange(1, 10))


def main():
    screen = Screen()
    screen.setup(width=550, height=500)
    turtles = create_turtle()
    user_bet = screen.textinput(title='Make your bet',
                                prompt='Who will be win on race(yellow, red, green, purple, blue, orange)')

    game(user_bet, turtles)
    screen.exitonclick()


if __name__ == '__main__':
    main()
