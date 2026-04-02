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
    new_snake = Snake([random.randint(0, CONFIG["rows"] - 1), random.randint(0, CONFIG["rows"] - 1)], COLORS["red"])
    new_snack = Food(generate_food_position(new_snake.getSnakeBody(), CONFIG['rows']), COLORS["green"])
    new_score = 0

    return new_snake, new_snack, new_score

if __name__ == '__main__':

    pygame.init()

    drawer = Drawer(CONFIG["width"], CONFIG["width"])
    clock = pygame.time.Clock()

    game_running = True

    snake, snack, score = restart()

    while game_running:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    game_running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP:
                            snake.turn(DIRECTIONS["UP"])
                        case pygame.K_DOWN:
                            snake.turn(DIRECTIONS["DOWN"])
                        case pygame.K_LEFT:
                            snake.turn(DIRECTIONS["LEFT"])
                        case pygame.K_RIGHT:
                            snake.turn(DIRECTIONS["RIGHT"])
                        case pygame.K_q:
                            game_running = False
                        case pygame.K_r if not snake.is_alive():
                            snake, snack, score = restart()

        if snake.is_alive():
            if snake.getHeadPos() == snack.getPos():
                snake.grow(COLORS["orange"])
                snack = Food(generate_food_position(snake.getSnakeBody(), CONFIG['rows']), COLORS["green"])
                score += 1

            snake.move()

            drawer.drawWindow()
            for bodyPart in snake.getSnakeBody():
                drawer.drawRect(bodyPart)
            drawer.drawRect(snack)
            drawer.draw_score(score)
        else:
            drawer.draw_post_game_info(score)

        drawer.update_window()

    pygame.quit()
