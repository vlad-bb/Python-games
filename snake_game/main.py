import time

from turtle import Screen
from snake_game.snake import Snake
from snake_game.food import Food
from snake_game.scorebord import ScoreBord


def main():
    screen = Screen()
    screen.bgcolor('black')
    screen.title('Snake game')
    screen.setup(width=600, height=600)
    screen.tracer(0)
    snake = Snake()
    food = Food()
    score = ScoreBord()
    game_is_on = True
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    while game_is_on:
        screen.update()
        time.sleep(0.2)
        snake.move()

        if snake.head_snake.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.add()
        if snake.head_snake.xcor() > 280 or snake.head_snake.xcor() < -300 or \
                snake.head_snake.ycor() > 280 or snake.head_snake.ycor() < -280:
            game_is_on = False
            score.game_over()
        for segment in snake.body_snake[1:]:
            if snake.head_snake.distance(segment) < 10:
                game_is_on = False
                score.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
