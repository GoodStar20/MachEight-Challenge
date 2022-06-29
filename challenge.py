import json
import requests

def print_player(height_sum):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    data = json.loads(response.text)
    players = data["values"]
    key_maps = dict()  # will hold the height as key and it's index in the player list as value
    index = 0
    for key, player in enumerate(players):
        h_in = int(player['h_in'])
        if height_sum - h_in in key_maps.keys():  # the complementary value is in the key_maps!
            p1 = players[key_maps[height_sum - h_in]]  # the according player is resolved
            p2 = players[key]
            print(f"- {get_person_data(p1)}    {get_person_data(p2)}")
            index += 1
        key_maps[h_in] = key  # save the key of the player
    if index == 0:
        print("No matches found")

def get_person_data(player):
    return f"{player['first_name']} {player['last_name']}"

def main():
    height_sum = int(input("Insert a signle integer: ")) #input integer
    print_player(height_sum)

if __name__ == "__main__":
    main()