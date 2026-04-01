class Food:
    def __init__(self, pos, color):
        self.__pos = pos
        self.__color = color

    def setPos(self, pos):
        self.__pos = pos

    def getPos(self):
        return self.__pos

    def getColor(self):
        return self.__color
