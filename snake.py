from config import CONFIG
from controls import DIRECTIONS
from food import Food


class Snake:

    def __init__(self, pos, headColor):
        self.__body = []
        self.__body.append(Food(pos, headColor))
        self.head = self.__body[0]
        self.direction = DIRECTIONS["DOWN"]

    def turn(self, direction):
        if (direction == DIRECTIONS["UP"]) and (self.direction != DIRECTIONS["DOWN"]):
            self.direction = DIRECTIONS["UP"]
        if (direction == DIRECTIONS["DOWN"]) and (self.direction != DIRECTIONS["UP"]):
            self.direction = DIRECTIONS["DOWN"]
        if (direction == DIRECTIONS["LEFT"]) and (self.direction != DIRECTIONS["RIGHT"]):
            self.direction = DIRECTIONS["LEFT"]
        if (direction == DIRECTIONS["RIGHT"]) and (self.direction != DIRECTIONS["LEFT"]):
            self.direction = DIRECTIONS["RIGHT"]

    def addCube(self, color):
        pos = self.__body[-1].getPos()
        self.__body.append(Food(pos, color))

    def move(self):
        if len(self.__body) > 1:
            for i in range(len(self.__body)-1, 0, -1):
                self.__body[i].setPos(self.__body[i-1].getPos())

        self.head.setPos([x + y for x, y in zip(self.head.getPos(), self.direction)])

        if len(self.__body) > 1:
            for part in self.__body[1:]:
                if self.head.getPos() == part.getPos():
                    return False

        pos = self.head.getPos()
        if pos[0] < CONFIG["zero"]:
            pos[0] = CONFIG["rows"] - 1
            self.head.setPos(pos)
        if pos[0] > CONFIG["rows"] - 1:
            pos[0] = CONFIG["zero"]
            self.head.setPos(pos)
        if pos[1] < CONFIG["zero"]:
            pos[1] = CONFIG["rows"] - 1
            self.head.setPos(pos)
        if pos[1] > CONFIG["rows"] - 1:
            pos[1] = CONFIG["zero"]
            self.head.setPos(pos)

        return True

    def getHeadPos(self):
        return self.head.getPos()

    def getSnakeBody(self):
        return self.__body
