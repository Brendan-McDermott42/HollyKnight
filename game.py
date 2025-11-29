from player import Player

# Configuration values for the game
PLAYER_STAT_POINTS = 20

class Game:
    def __init__(self):
        self.player = Player(PLAYER_STAT_POINTS)

    def play(self, inp):
        print("---------- new round ----------")
        self.player.play()
