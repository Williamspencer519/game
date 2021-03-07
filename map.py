from water import Water
from tree import Tree
from building import Building
from dirt import Dirt



symbol_map = {"W":Water,"T":Tree, "B":Building, " ":Dirt}


f = open("map.txt", "r")

game_map = []

for line in f:
	game_row = []
	for char in line:
		if char == "\n":
			continue
		game_row.append(symbol_map[char]())
	game_map.append(game_row)

print(game_map)





