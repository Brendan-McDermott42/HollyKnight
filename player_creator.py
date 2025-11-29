
class PlayerCreator:

    @staticmethod
    def _check_input(target, stat_points):
        result = 0
        print(f"you have {stat_points} points left. how many would you like to assign to {target}")
        inp = input()
        number = 0
        if inp.isnumeric():
            number = int(inp)
        if number > 0 and number <= stat_points:

            result += number
        return [result, stat_points - number]

    @staticmethod
    def upsert_player(stat_points, player_name, health, constitution, dexterity, intelligence, wisdom):
        player = {
            "player_name": player_name,
            "health": health,
            "constitution": constitution,
            "dexterity": dexterity,
            "intelligence": intelligence,
            "wisdom": wisdom,
        }
        if player_name == "unknown":
            print("What... is your name?")
            inp = input()
            player["player_name"] = inp
            player["has_changed"] = True
            print(f"your name is {inp} (y or n)")
            inp = input()
            print("tough" if inp == 'n' else f"cool {inp}, nice to meet you")

        # do player stats
        if stat_points > 0:
            print("you must assign your stat points to your character.")
            print(f"you currently have {stat_points} points.")
            print("you should decide what you would like to assign to health, constitution, dexterity, intelligence, wisdom.")
            print("type which stat you would like to assign first")
            while stat_points > 0:
                inp = input()
                if inp == "health":
                    result = PlayerCreator._check_input(inp, stat_points)
                    player["health"] = player["health"] + result[0]
                    stat_points = (
                        result)[1]
                    if stat_points > 0:
                        print(player)
                        print(f"{stat_points} points remaining.")
                if inp == "constitution":
                    result = PlayerCreator._check_input(inp, stat_points)
                    player["constitution"] = player["constitution"] + result[0]
                    stat_points = result[1]
                    if stat_points > 0:
                        print(player)
                        print(f"{stat_points} points remaining.")
                if inp == "dexterity":
                    result = PlayerCreator._check_input(inp, stat_points)
                    player["dexterity"] = player["dexterity"] + result[0]
                    stat_points = result[1]
                    if stat_points > 0:
                        print(player)
                        print(f"{stat_points} points remaining.")
                if inp == "intelligence":
                    result = PlayerCreator._check_input(inp, stat_points)
                    player["intelligence"] = player["intelligence"] + result[0]
                    stat_points = result[1]
                    if stat_points > 0:
                        print(player)
                        print(f"{stat_points} points remaining.")
                if inp == "wisdom":
                    result = PlayerCreator._check_input(inp, stat_points)
                    player["wisdom"] = player["wisdom"] +  result[0]
                    stat_points = result[1]
                    if stat_points > 0:
                        print(player)
                        print(f"{stat_points} points remaining.")

        return player