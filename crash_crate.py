class Crash_crate:
    def __init__(self, name, xPos=800, yPos=260, lifeplus=5):
        self.name = name
        self.xPos = xPos
        self.yPos = yPos
        self.lifeplus = lifeplus

    def _getname(self):
        return self.name

    def _getxposition(self):
        if self.xPos < 0:
            return "la valeur de la position {} est negative ".format(self.xPos)
        else:
            return self.xPos

    def _setxposition(self, position):
        if position < 0:
            self.position = 0
            self.xPos += position
        else:
            self.xPos = position

    def __del__(self):
        if self.lifeplus == 0:
            print("objet detruit ! ")

    names = property(_getname)
    xposition = property(_getxposition, _setxposition)
