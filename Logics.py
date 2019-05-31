# logics.py

class Logics:


    def __init__(self):
        # self.posList = ['dl', 'dm', 'dr', 'ml', 'mm', 'mr', 'ul', 'um', 'ur']
        self.posList = []
        self.xposList = []
        self.yposList = []
        self.pos = ""

    def appendPos(self, pos):
        self.posList.append(pos)

    def printPos(self):
        return self.posList

    def isWinner(self):
        if ('dl' in self.posList and 'dm' in self.posList and 'dr' in self.posList) \
                or ('ul' in self.posList and 'um' in self.posList and 'ur' in self.posList) \
                or ('ml' in self.posList and 'mm' in self.posList and 'mr' in self.posList) \
                or ('ld' in self.posList and 'lm' in self.posList and 'lu' in self.posList) \
                or ('md' in self.posList and 'mm' in self.posList and 'mu' in self.posList) \
                or ('rd' in self.posList and 'rm' in self.posList and 'ru' in self.posList) \
                or ('lu' in self.posList and 'mm' in self.posList and 'rd' in self.posList) \
                or ('ru' in self.posList and 'mm' in self.posList and 'ld' in self.posList):
            return 'winner!'
        else:
            return 'not yet'

    def isOccupied(self):
        pass