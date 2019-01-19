import random

from classes.game import Person, bcolors
from classes.inventory import Item
from classes.magic import Spell

# Creating Black Magics
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 60, 1400, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create Some items
potion = Item("Potion", "potion", "Heals 50 HP", 250)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 500)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 1000)
elixer = Item("Elixer", "elixer", "fully restores HP/MP of one party", 99999)
hielixer = Item("Mega-Elixer", "elixer", "fully restores Party's HP/MP", 99999)
granade = Item("Granade", "attack", "Deals 500 damage", 2000)

spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
items = [{"item":potion,"quantity":5},
		 {"item":hipotion,"quantity":5},
		 {"item":superpotion,"quantity":2},
		 {"item":elixer,"quantity":5},
		 {"item":hielixer,"quantity":4},
		 {"item":granade,"quantity":5},]


def create_players():
	player_name = input("Player name : ")
	player_hp = random.randrange(2000, 5000)
	print("     Hp awarded      : "+bcolors.OKGREEN+str(player_hp)+bcolors.ENDC)
	player_mp = random.randrange(100, 500)
	print("     Mp awarded      : "+bcolors.OKBLUE+str(player_mp)+bcolors.ENDC)
	player_atk = random.randrange(200, 400)
	print("Player attack power  : "+bcolors.FAIL+str(player_atk)+bcolors.ENDC)
	player_df = random.randrange(100, 250)
	print("Player defence power : "+bcolors.HEADER+str(player_df)+bcolors.ENDC)
	player_magic_choice = 4
	player_item_choice = 3
	player_spell_choices = spells[:]
	player_item_choices = items[:]
	player_spells = []
	player_items = []
	print("\nChoose Spells for ",player_name)

	while player_magic_choice > 0:
		i = 1
		for magic in player_spell_choices:
			print("    " + str(i) + " . " + magic.name, "(cost : ", str(magic.cost) + ")")
			i += 1
		player_choice = int(input("Choice : "))
		player_spells.append(player_spell_choices[player_choice - 1])
		player_spell_choices.remove(player_spell_choices[player_choice - 1])
		player_magic_choice -= 1

	print("Player has spells : ")
	i=1
	for magic in player_spells:
		print("    " + str(i) + " . " +bcolors.OKBLUE+ magic.name+bcolors.ENDC)
		i += 1


	print("\nChoose items for ", player_name)
	while player_item_choice >0:
		i = 1
		for magic in player_item_choices:
			print("    " + str(i) + " . " + magic["item"].name)
			i += 1
		player_choice = int(input("Choice : "))
		player_items.append(player_item_choices[player_choice-1])
		player_item_choices.remove(player_item_choices[player_choice-1])
		player_item_choice-=1

	print("Player has items : ")
	i = 1
	for magic in player_items:
		print("    " + str(i) + " . " +bcolors.WARNING+ magic["item"].name+bcolors.ENDC)
		i += 1

	player = Person(player_name,player_hp,player_mp,player_atk,player_df,player_spells,player_items)


	return player

def create_enemy(player_name):
	player_hp = random.randrange(15000, 25000)
	print("     Hp awarded      : "+bcolors.OKGREEN+str(player_hp)+bcolors.ENDC)
	player_mp = random.randrange(500, 1000)
	print("     Mp awarded      : "+bcolors.OKBLUE+str(player_mp)+bcolors.ENDC)
	player_atk = random.randrange(500, 800)
	print(" Enemy attack power  : "+bcolors.FAIL+str(player_atk)+bcolors.ENDC)
	player_df = random.randrange(100, 250)
	print(" Enemy defence power : "+bcolors.HEADER+str(player_df)+bcolors.ENDC)
	player_magic_choice = 4
	player_item_choice = 3
	print(spells)
	player_spell_choices = spells[:]
	player_item_choices = items[:]
	player_spells = []
	player_items = []
	x=len(spells)
	print("x=",x)
	while player_magic_choice > 0:
		player_choice = random.randint(0, x-1)
		x-=1
		player_spells.append(player_spell_choices[player_choice])
		player_spell_choices.remove(player_spell_choices[player_choice])
		player_magic_choice -= 1

	print(" Enemy has spells : ")
	i=1
	for magic in player_spells:
		print("    " + str(i) + " . " +bcolors.OKBLUE+ magic.name+bcolors.ENDC)
		i += 1
	x=len(items)

	while player_item_choice >0:
		# print("Item Choices left : ")
		player_choice = random.randrange(0,x)
		x-=1
		player_items.append(player_item_choices[player_choice])
		player_item_choices.remove(player_item_choices[player_choice])
		player_item_choice-=1

	print(" Enemy has items : ")
	i = 1
	for magic in player_items:
		print("    " + str(i) + " . " +bcolors.WARNING+ magic["item"].name+bcolors.ENDC)
		i += 1

	player = Person(player_name,player_hp,player_mp,player_atk,player_df,player_spells,player_items)


	return player

#
# player1 = Person("Anish",3260, 132, 60, 34, player_spells, player_items)
# player2 = Person("Yash ",4160, 188, 60, 34, player_spells, player_items)
# player3 = Person("Harsh",2080, 221, 60, 34, player_spells, player_items)
#
# players = [player1,player2,player3]
#


running = True
players = []

while running:
	print("Create Players : ")
	player_created = create_players()
	players.append(player_created)
	player_created.get_stats()
	print("No of players created : ", len(players))
	print("Do you want to create another player? [1 for yes | 2 for no \n]")
	player_choice = input("Choice : ")
	if player_choice == "1":
		running = True
	else:
		running = False


running = True
print("\n\n")


print(bcolors.FAIL+"Creating Enemies"+bcolors.ENDC)
i=1
x=0
enemies = []
while running:
	enemy_name = "Enemy " + str(x+1)
	enemy_created = create_enemy(enemy_name)
	enemies.append(enemy_created)
	enemy_created.get_enemy_stats()
	if(len(players)==1 or len(enemies)+2>len(players)):
		break
	x+=1


print("\n")
running = True

print("Press any key to initiate game!")
input()


print(bcolors.BOLD + bcolors.FAIL + "THE ENEMY ATTACKS !" + bcolors.ENDC)


def check_battle_over():
	global defeated_enemies, defeated_players, enemy, player, running
	defeated_enemies = 0
	defeated_players = 0
	for enemy in enemies:
		if enemy.get_hp() == 0:
			print(bcolors.WARNING + bcolors.BOLD + "Enemy defeated : ", enemy.name + bcolors.ENDC)
			defeated_enemies += 1
	for player in players:
		if player.get_hp() == 0:
			print(bcolors.FAIL + bcolors.BOLD + "Players lost : ", player.name + bcolors.ENDC)
			defeated_players += 1
	if defeated_enemies == len(enemies):
		print(bcolors.OKGREEN + bcolors.BOLD + "You Win ! Game Over ! " + bcolors.ENDC)
		running = False

	elif defeated_players == len(players):
		print(bcolors.FAIL + bcolors.BOLD + "Enemies Won!  Game Over !" + bcolors.ENDC)
		running = False


def enemy_magic_attack():
	global magic_choice, spell, magic_dmg
	if (enemy.get_hp()/enemy.get_max_hp()) <0.2:
		for spell in enemy.magic:
			if spell.type == "white" and enemy.mp <spell.cost:
				break
	else:
		for spell in enemy.magic:
			if spell.type == "black" and enemy.mp <spell.cost:
				break
	magic_dmg = spell.generate_damage()
	enemy.reduce_mp(spell.cost)

	flag = 0
	if enemy.mp < spell.cost:
		for spell in enemy.magic:
			if(enemy.mp > spell.cost):
				flag = 1
				break
		if flag == 0:
			spell=-1
			magic_dmg=-1
			return spell, magic_dmg
		enemy_magic_attack()

	else:
		return spell,magic_dmg




while running:

	print("  Name                        HP                                      MP")

	for player in players:
		player.get_stats()
	for enemy in enemies:
		enemy.get_enemy_stats()

	print("============================================================================")

	for player in players:
		check_battle_over()
		print("\n")
		print("Name                        HP                                      MP")
		player.get_stats()

		player.choose_action()
		choice = input("Your action : ")
		if choice == "q":
			exit(0)
		choice = int(choice) - 1


		if choice == 0:
			dmg = player.generate_damage()
			enemy=player.choose_target(enemies)
			enemies[enemy].take_damage(dmg)
			print(bcolors.OKGREEN + "\n"+player.get_name()+" attacked "+enemies[enemy].name+" for", dmg, "points of damage." + bcolors.ENDC)

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
				enemy = player.choose_target(enemies)
				enemies[enemy].take_damage(magic_dmg)
				print(bcolors.OKBLUE + "\n" +player.get_name()+" used "+ spell.name + " deals " + str(magic_dmg), "points of damage to " +enemies[enemy].name+ bcolors.ENDC)

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
				if item.name == "Mega-Elixer":
					for i in players:
						i.hp = i.max_hp
						i.mp = i.max_mp
				else:
					player.hp = player.max_hp
					player.mp = player.max_mp
				print(bcolors.OKGREEN + "\n" + item.name + " FULLY RESTORES HP/MP" + bcolors.ENDC)
			elif item.type == "attack":
				enemy = player.choose_target(enemies)
				enemies[enemy].take_damage(item.prop)
				print(bcolors.WARNING + "\n" + item.name + " deals " + str(item.prop) + " points of damage to " +enemies[enemy].name+ bcolors.ENDC)

	check_battle_over()


	for enemy in enemies:
		check_battle_over()
		enemy_choice = random.randrange(0,2)

		target = random.randrange(0, len(players))

		if enemy_choice == 0:
			enemy_dmg = enemy.generate_damage()
			players[target].take_damage(enemy_dmg)
			print(bcolors.FAIL + "\n"+enemy.name+" attacked for", enemy_dmg, "points of damage to "+players[target].name + bcolors.ENDC)
		elif enemy_choice == 1:
			spell,magic_dmg = enemy_magic_attack()

			if spell == -1:
				print(bcolors.FAIL+"\n"+enemy.get_name()+"tried to use Magic but didnt have enough magic points"+bcolors.ENDC)
				continue

			if spell.type == "white":
				enemy.heal(magic_dmg)
				print(bcolors.FAIL + "\n" +enemy.get_name()+" used "+ spell.name + " heals for " + str(magic_dmg), "HP" + bcolors.ENDC)
			elif spell.type == "black":

				players[target].take_damage(magic_dmg)
				print(bcolors.OKBLUE + "\n" +enemy.get_name()+" used "+ spell.name + " deals " + str(magic_dmg), "points of damage to " +players[target].name+ bcolors.ENDC)

	print("""-------------------------------------------------------- 
	
			""")
	# print("Enemy HP  : " + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

	check_battle_over()

