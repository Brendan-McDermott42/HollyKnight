from characters.character import Character
from player_creator import PlayerCreator


class Player(Character):
    def __init__(self, stat_points):
        super().__init__()
        self.stat_points = stat_points

    def speak(self, stat_points):
        print(f"I am the player {self.name}")


    def get_player_stats(self):
        return {
            "player_name": self.name,
            "health": self.health,
            "constitution": self.constitution,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
        }

    def _check_for_stat_points(self):
        if self.stat_points > 0:
            print("you have unassigned stats points")
            update = PlayerCreator.upsert_player(
                stat_points=self.stat_points,
                player_name=self.name,
                health=self.health,
                constitution=self.constitution,
                dexterity=self.dexterity,
                intelligence=self.intelligence,
                wisdom=self.wisdom
                )
            self.name = update["player_name"]
            self.stat_points = 0
            self.health = update["health"]
            self.constitution = update["constitution"]
            self.dexterity = update["dexterity"]
            self.intelligence = update["intelligence"]
            self.wisdom = update["wisdom"]
            print(self.get_player_stats())


    def play(self):
        self._check_for_stat_points()