import random
from .magic import Spell


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class Person:
	def __init__(self, name, hp, mp, atk, df, magic, items):
		self.max_hp = hp
		self.name = name
		self.hp = hp
		self.max_mp = mp
		self.mp = mp
		self.atkl = atk - 10
		self.atkh = atk + 10
		self.df = df
		self.magic = magic
		self.items = items
		self.actions = ["ATTACK", "MAGIC", "Items"]

	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)

	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def get_name(self):
		return self.name

	def heal(self, dmg):
		self.hp += dmg
		if self.hp > self.max_hp:
			self.hp = self.max_hp

	def get_hp(self):
		return self.hp

	def get_max_hp(self):
		return self.max_hp

	def get_mp(self):
		return self.mp

	def get_max_mp(self):
		return self.max_mp

	def reduce_mp(self, cost):
		self.mp -= cost

	def choose_action(self):
		i = 1
		print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS : " + bcolors.ENDC)
		for item in self.actions:
			print("    " + str(i) + "." + item)
			i += 1

	def choose_target(self,enemies):
		i =1
		print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET : " + bcolors.ENDC)
		for enemy in enemies:
			print("    "+str(i)+"."+enemy.name)
			i+=1
		choice = int(input("Choose Target : ")) -1
		return choice


	def choose_magic(self):
		i = 1
		print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC : " + bcolors.ENDC)
		for spell in self.magic:
			print("    " + str(i) + " . " + spell.name, "(cost : ", str(spell.cost) + ")")
			i += 1

	def choose_items(self):
		i = 1
		print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ITEMS : " + bcolors.ENDC)
		for item in self.items:
			print("    " + str(i) + " . " + item["item"].name, " : ", item["item"].desp,
			      "(x" + str(item["quantity"]) + ")")
			i += 1

	def get_enemy_stats(self):
		bar = ""
		hp = (self.hp / self.max_hp) * 50
		while len(bar) < 50:
			if hp > 0:
				bar += "█"
				hp -= 1
			else:
				bar += " "

		comp = ""

		if (self.hp > 999):
			comp = ""
		elif self.hp < 1000 and self.hp > 99:
			comp = " "
		elif self.hp < 100 and self.hp > 9:
			comp = "  "
		else:
			comp = "   "

		print("                              __________________________________________________")
		print(bcolors.BOLD + self.name + " :     " + comp +
		      str(self.hp) + " /" + str(
			self.max_hp) + "   |" + bcolors.FAIL + bar + bcolors.ENDC + bcolors.BOLD + "|    " + bcolors.ENDC)

	def get_stats(self):

		name_come = ""

		if len(self.name) == 7:
			name_come = ""
		elif len(self.name) == 6:
			name_come = " "
		elif len(self.name) == 5:
			name_come = "  "
		elif len(self.name) == 4:
			name_come = "   "
		elif len(self.name) == 3:
			name_come = "    "
		elif len(self.name) == 2:
			name_come = "     "
		elif len(self.name) == 1:
			name_come = "      "
		elif len(self.name) ==0:
			name_come = "       "


		bar = ""
		hp = (self.hp / self.max_hp) * 25
		while len(bar) < 25:
			if hp > 0:
				bar += "█"
				hp -= 1
			else:
				bar += " "

		comp = ""

		if (self.hp > 999):
			comp = ""
		elif self.hp < 1000 and self.hp > 99:
			comp = " "
		elif self.hp < 100 and self.hp > 9:
			comp = "  "
		else:
			comp = "   "

		mp_bar = ""
		mp = (self.mp / self.max_mp) * 10
		while len(mp_bar) < 10:
			if mp > 0:
				mp_bar += "█"
				mp -= 1
			else:
				mp_bar += " "
		comp_mp = ""
		if self.mp > 99:
			comp_mp = ""
		elif (self.mp > 9 and self.mp < 100):
			comp_mp = ""
		else:
			comp_mp = " "

		print("                              _________________________               __________")
		print(bcolors.BOLD + name_come+self.name + " :     " + comp +"  "+
		      str(self.hp) + " /" + str(
			self.max_hp) + "   |" + bcolors.OKGREEN + bar + bcolors.ENDC + bcolors.BOLD + "|    " + comp_mp +
		      str(self.mp) + "/" + str(self.max_mp) + "  |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
