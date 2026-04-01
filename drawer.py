import pygame

from config import CONFIG, COLORS


class Drawer:
    def __init__(self, width, height):
        self.__screen = pygame.display.set_mode([width, height])

    def drawGrid(self):
        sizeBtw = CONFIG["width"] // CONFIG["rows"]

        for i in range(CONFIG["rows"]):
            x = i * sizeBtw
            y = i * sizeBtw

            pygame.draw.line(self.__screen, COLORS["white"], (x, 0), (x, CONFIG["width"]))
            pygame.draw.line(self.__screen, COLORS["white"], (0, y), (CONFIG["width"], y))

    def redrawWindow(self):
        self.__screen.fill(COLORS["black"])
        self.drawGrid()
        pygame.display.update()

    def drawRect(self, rect):
        dis = CONFIG["width"] // CONFIG["rows"]
        pos = rect.getPos()
        i = pos[0]
        j = pos[1]

        pygame.draw.rect(self.__screen, rect.getColor(), (i * dis + 1, j * dis + 1, dis - 1, dis - 1))
        pygame.display.update()
