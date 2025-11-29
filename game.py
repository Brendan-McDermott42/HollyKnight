from player import Player
from story_elements.story_start import StoryStart

# Configuration values for the game
PLAYER_STAT_POINTS = 20

class Game:
    def __init__(self):
        self.player = Player(PLAYER_STAT_POINTS)

    def play(self):
        print("---------- new round ----------")
        self.player.play()
        story = StoryStart()
        story.play()
