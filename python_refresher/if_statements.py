# should_continue = True
# if should_continue:
# 	print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
# 	print("You know this person!")

# # if person not in known_people:
# # 	print("You don't know this person!")

# else:
# 	print("You don't know this person!")

# if person in known_people:
# 	print("You know {}!".format(person))

# else:
# 	print("You don't know {}!".format(person))

# def who_do_you_know():
# 	# ask the user the list of people they know
# 	# split the string into a list
# 	# return that list

# 	people = input("Enter the names of the people you know, separated by commas: ")
# 	people_list = people.split(",") # ["John", "Rolf", "Anna", "Greg"]
# 	return people_list

# def ask_user():
# 	# ask user for their name
# 	# see if their name is in the list of people they know
# 	# print out that they know the person
# 	person = input("Enter a name of someone you know: ")

# 	# solution 1
# 	# people = who_do_you_know()
# 	# if person in people:
# 	# 	print("You know {}!".format(person))

# 	# solution 2
# 	if person in who_do_you_know():
# 		print("You know {}!".format(person))

# ask_user()


def who_do_you_know():
	people = input("Enter the names of the people you know, separated by commas: ")
	people_list = people.split(",") 

	# people_without_spaces = []
	# for person in people_list:
	# 	people_without_spaces.append(person.strip()) # strips white spaces
	# return people_without_spaces

	people_without_spaces = [person.strip() for person in people_list]
	return people_without_spaces


def ask_user():
	person = input("Enter a name of someone you know: ")
	if person in who_do_you_know():
		print("You know {}!".format(person))

ask_user()