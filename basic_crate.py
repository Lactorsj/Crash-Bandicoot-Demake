import pygame


class Basic_crate:
    def __init__(self, name, xPos=800, yPos=260, wumpafruit=10):
        self.name = name
        self.basiccrate = pygame.image.load("Basic_crate.png")
        self.xPos = xPos
        self.yPos = yPos
        self.wumpafruit = wumpafruit

    def _getname(self):
        return self.name

    def _getxposition(self):
        if self.xPos < 0:
            return "the value of the position {} est negative ".format(self.xPos)
        else:
            return self.xPos

    def _setxposition(self, position):
        if position < 0:
            self.position = 0
            self.xPos += position
        else:
            self.xPos = position

    """
        def clear_list(self,objet):
        if self.list.Colliderect(objet):
            self.list.clear()
    """
    names = property(_getname)
    xposition = property(_getxposition, _setxposition)
