
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons")
    print("3. Top 10 weakest pokemons")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        number = int(input("Show pokemon by index"))
        print(pokemons[number - 1])
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass
    elif choice == '2':
        # {'number': 15, 'name': 'BeedrillMega Beedrill', 'type_1': 'Bug', 'type_2': 'Poison', 'total': 495, 'hp': 65, 'attack': 150, 'defense': 40}
        def strongest_pokemon(pokemon):
            return int(pokemon['total'])
        pokemons.sort(key = strongest_pokemon,reverse = True)   
        print(pokemons[0:10])  
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        def weakest_pokemon(pokemon):
            return int(pokemon['total'])
        pokemons.sort(key = weakest_pokemon)
        print(pokemons[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        import random
        print(random.choice(pokemons))
        player_choice = int(input("Choose your pokemon"))
        print(pokemons[player_choice - 1])
        print("Battle starts")

        
        # Battle
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


