from config import CONFIG
from controls import DIRECTIONS
from food import Food


class Snake:

    def __init__(self, pos, headColor):
        self.body = []
        self.body.append(Food(pos, headColor))
        self.head = self.body[0]
        self.direction = DIRECTIONS["DOWN"]
        self.alive = True

    def turn(self, direction):
        opposite = {
            DIRECTIONS["UP"]: DIRECTIONS["DOWN"],
            DIRECTIONS["DOWN"]: DIRECTIONS["UP"],
            DIRECTIONS["LEFT"]: DIRECTIONS["RIGHT"],
            DIRECTIONS["RIGHT"]: DIRECTIONS["LEFT"],
        }

        if direction != opposite[self.direction]:
            self.direction = direction

    def grow(self, color):
        pos = self.body[-1].getPos()
        self.body.append(Food(pos, color))

    def move(self):
        if len(self.body) > 1:
            for i in range(len(self.body)-1, 0, -1):
                self.body[i].setPos(self.body[i-1].getPos())

        self.head.setPos([x + y for x, y in zip(self.head.getPos(), self.direction)])

        if len(self.body) > 1:
            for part in self.body[1:]:
                if self.head.getPos() == part.getPos():
                    self.alive = False
                    return

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

    def getHeadPos(self):
        return self.head.getPos()

    def getSnakeBody(self):
        return self.body

    def is_alive(self):
        return self.alive
