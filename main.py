from game import Game
from title_screen import get_title_screen
if __name__ == '__main__':
    print(get_title_screen())
    playing = True
    print("ready to venture forth? (enter to begin or type exit to quit)")
    game = Game()
    while playing:
        inp = input()
        if inp == "exit":
            playing = False
            break
        game.play()

