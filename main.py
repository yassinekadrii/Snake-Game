from turtle import Screen
import time
from snake import Snake
from Food import Food
from Scoore import Scoreboard

# Configuration de l'écran
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Créer les objets du jeu
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Liaison des touches fléchées avec les méthodes de direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Boucle principale du jeu
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Détecter la collision avec la nourriture
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
