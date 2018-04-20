lottery_player_dict = {
	'name': 'Rolf',
	'numbers': (5, 9, 12, 3, 1, 21)
}

# class LotteryPlayer:
# 	def __init__(self):
# 		self.name = "Rolf"
# 		self.numbers = (5, 9, 12, 3, 1, 21)


# 	def total(self):
# 		return sum(self.numbers)	
# player = LotteryPlayer()
# print(player.name)
# print(player.numbers)
# print(player.total())

# player_one = LotteryPlayer()
# player_two = LotteryPlayer()

# two different entities that share the same signature
# print(player_one == player_two) # False
# print(player_one.name == player_two.name) # True

##

class LotteryPlayer:
	def __init__(self, name):
		self.name = name
		self.numbers = (5, 9, 12, 3, 1, 21)

player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")
# print(player_one.name == player_two.name) # False

player_one.numbers = (1, 2, 3, 6, 7, 8)

# print(player_one.numbers == player_two.numbers) #False


##

class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len (self.marks)

	# def go_to_school(self):
	# 	print("I'm going to {}.".format(self.school))

	# def go_to_school() # this is not going to work. 'self' in automatically passed in.
	#	print("I'm going to school")

	# @classmethod # removes the need for 'self'
	# def go_to_school(cls):
	# 	print("I'm going to school")
	# 	print("I'm a {}".format(cls))

	@staticmethod	#no longer matters who is calling it.
	def go_to_school():
		print("I'm going to school")

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
# print(anna.marks)
anna.marks.append(71)
# print(anna.average())
anna.go_to_school()
rolf.go_to_school()
Student.go_to_school()
