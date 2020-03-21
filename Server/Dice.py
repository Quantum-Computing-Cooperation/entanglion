from random import randrange


class Dice:
    def __init__(self, faces):
        self.faces = faces

    def generate(self):
        return randrange(self.faces)
