my_list = [0, 1, 2, 3, 4]

# creates array size 5 (iterates). 2nd x is index, 1st x is the value 
# put 1st x in the list
an_equal_list = [x for x in range(5)]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

print([n for n in range(10) if n % 2 == 0]) 

people_you_know = ["Rolf", " John", "anna", "GREG"]
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)