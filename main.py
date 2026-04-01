import random
import pygame
from snake import Snake
from food import Food
from drawer import Drawer
from controls import DIRECTIONS
from config import CONFIG
from config import COLORS


if __name__ == '__main__':

    pygame.init()
    drawer = Drawer(CONFIG["width"], CONFIG["width"])
    clock = pygame.time.Clock()

    snake = Snake([random.randint(0, CONFIG["rows"] - 1), random.randint(0, CONFIG["rows"] - 1)], COLORS["red"])
    snack = Food([random.randint(0, CONFIG["rows"] - 1), random.randint(0, CONFIG["rows"] - 1)], COLORS["green"])

    running = True

    while running:
        pygame.time.delay(100)
        clock.tick(10)

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

        if snake.getHeadPos() == snack.getPos():
            snake.addCube(COLORS["orange"])
            snack = Food([random.randint(0, CONFIG["rows"] - 1), random.randint(0, CONFIG["rows"] - 1)],
                         COLORS["green"])
        else:
            running = snake.move()

        print(str(snake.getHeadPos()) + ", " + str(snack.getPos()))

        drawer.redrawWindow()
        for bodyPart in snake.getSnakeBody():
            drawer.drawRect(bodyPart)
        drawer.drawRect(snack)

    pygame.quit()
