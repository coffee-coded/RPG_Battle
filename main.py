from classes.game import Person, bcolors
from classes.inventory import Item
from classes.magic import Spell
import random






# Creating Black Magics
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "fully restores HP/MP of one party", 9999)
hielixer = Item("Mega-Elixer", "elixer", "fully restores Party's HP/MP", 9999)
granade = Item("Granade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": superpotion, "quantity": 5},
                {"item": hipotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": granade, "quantity": 5}]




player1 = Person("Anish",3260, 132, 60, 34, player_spells, player_items)
player2 = Person("Yash ",4160, 188, 60, 34, player_spells, player_items)
player3 = Person("Harsh",2080, 221, 60, 34, player_spells, player_items)

players = [player1,player2,player3]

enemy = Person("Enemy",1200, 325, 45, 25, [], [])

running = True

print(bcolors.BOLD + bcolors.FAIL + "THE ENEMY ATTACKS !" + bcolors.ENDC)

while running:

	print("Name                      HP                                      MP")

	for player in players:
		player.get_stats()
	enemy.get_enemy_stats()

	print("============================================================================")

	for player in players:
		print("\n")
		print("Name                      HP                                      MP")
		player.get_stats()

		player.choose_action()
		choice = input("Your action : ")
		if choice == "q":
			exit(0)
		choice = int(choice) - 1

		if choice == 0:
			dmg = player.generate_damage()
			enemy.take_damage(dmg)
			print(bcolors.OKGREEN + "\n"+player.get_name()+" attacked for", dmg, "points of damage." + bcolors.ENDC)

		elif choice == 1:
			player.choose_magic()
			magic_choice = int(input("Choose Magic : ")) - 1

			if magic_choice == -1:
				continue

			spell = player.magic[magic_choice]
			magic_dmg = spell.generate_damage()
			cost = spell.cost

			current_mp = player.get_mp()
			if cost > current_mp:
				print(bcolors.FAIL + "\n NOT ENOUGH MP ! \n" + bcolors.ENDC)
				continue

			player.reduce_mp(cost)

			if spell.type == "white":
				player.heal(magic_dmg)
				print(bcolors.OKBLUE + "\n" +player.get_name()+" used "+ spell.name + " heals for " + str(magic_dmg), "HP" + bcolors.ENDC)
			elif spell.type == "black":
				enemy.take_damage(magic_dmg)
				print(bcolors.OKBLUE + "\n" +player.get_name()+"used "+ spell.name + " deals " + str(magic_dmg), "points of damage" + bcolors.ENDC)

		elif choice == 2:
			player.choose_items()
			item_choice = int(input("Choose Item : ")) - 1

			if item_choice == -1:
				continue

			item = player.items[item_choice]["item"]
			if player.items[item_choice]["quantity"] == 0:
				print(bcolors.FAIL + "\nNone Left... \n" + bcolors.ENDC)
				continue

			player.items[item_choice]["quantity"] -= 1

			if item.type == "potion":
				player.heal(item.prop)
				print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop) + " HP" + bcolors.ENDC)
			elif item.type == "elixer":
				player.hp = player.max_hp
				player.mp = player.max_mp
				print(bcolors.OKGREEN + "\n" + item.name + " FULLY RESTORES HP/MP" + bcolors.ENDC)
			elif item.type == "attack":
				enemy.take_damage(item.prop)
				print(bcolors.WARNING + "\n" + item.name + " deals " + str(item.prop) + " points of damage" + bcolors.ENDC)

	enemy_choice = 1
	enemy_dmg = enemy.generate_damage()
	player1.take_damage(enemy_dmg)
	print(bcolors.FAIL + "\nEnemy attacked for", enemy_dmg, "points of damage." + bcolors.ENDC)

	print("""-------------------------------------------------------- 
	
			""")
	print("Enemy HP  : " + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

	if enemy.get_hp() == 0:
		print(bcolors.OKGREEN + bcolors.BOLD + "You Win ! Game Over ! " + bcolors.ENDC)
		running = False

	elif player.get_hp() == 0:
		print(bcolors.FAIL + bcolors.BOLD + "You Lost. Enemy Won ! Game Over !" + bcolors.ENDC)
		running = False
