from random import random


class Dice:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides

    def roll(self):
        return random.randint(1,self.no_of_sides)