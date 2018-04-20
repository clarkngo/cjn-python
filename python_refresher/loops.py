# my_variable = "hello"

# "h" gets printed
# print(my_variable[0])

# my_string = "hello"

# iterables are strings, lists, sets, tuples and more
# for character in my_string:
#	print(character)

# my_list = [1, 3, 5, 7, 9]

# for number in my_list:
#	print(number ** 2)

user_wants_number = True
while user_wants_number == True:
	print(10)

	# works on python3.5 only
	user_input = input("Should we print again?(y/n) ")
	if user_input == 'n':
		user_wants_number = False