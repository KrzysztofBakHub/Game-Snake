import random
import pygame
from snake import Snake
from food import Food
from drawer import Drawer
from controls import DIRECTIONS
from config import CONFIG
from config import COLORS
import config

def generate_food_position(snake_body, rows):
    occupied_positions = {tuple(part.getPos()) for part in snake_body}

    while True:
        position = (
            random.randint(0, rows - 1),
            random.randint(0, rows - 1)
        )
        if position not in occupied_positions:
            return [position[0], position[1]]

def restart():
    snake = Snake([random.randint(0, CONFIG["rows"] - 1), random.randint(0, CONFIG["rows"] - 1)], COLORS["red"])
    snack = Food([random.randint(0, CONFIG["rows"] - 1), random.randint(0, CONFIG["rows"] - 1)], COLORS["green"])

    score = 0
    game_over = False
    running = True

    return snake, snack, score, game_over, running

if __name__ == '__main__':

    pygame.init()
    drawer = Drawer(CONFIG["width"], CONFIG["width"])
    clock = pygame.time.Clock()

    snake, snack, score, game_over, running = restart()

    while running:
        clock.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(DIRECTIONS["UP"])
                if event.key == pygame.K_DOWN:
                    snake.turn(DIRECTIONS["DOWN"])
                if event.key == pygame.K_LEFT:
                    snake.turn(DIRECTIONS["LEFT"])
                if event.key == pygame.K_RIGHT:
                    snake.turn(DIRECTIONS["RIGHT"])
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_r:
                    snake, snack, score, game_over, running = restart()

        if not game_over:
            if snake.getHeadPos() == snack.getPos():
                snake.grow(COLORS["orange"])
                snack = Food(generate_food_position(snake.getSnakeBody(), CONFIG['rows']), COLORS["green"])
                score += 1

            game_over = snake.move()

            #print(str(snake.getHeadPos()) + ", " + str(snack.getPos()))

            drawer.redrawWindow()
            for bodyPart in snake.getSnakeBody():
                drawer.drawRect(bodyPart)
            drawer.drawRect(snack)

        drawer.update_window()

    pygame.quit()
