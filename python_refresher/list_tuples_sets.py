my_variable = "hello"

# list
grades = [77, 80, 90]

#tuple - immutable - can't increase size
tuples_grades = (77, 80, 90)


set_grades = {77, 80, 90} # unique & unordered

#print(len(grades))

# inserts after the last
# grades.append(50)

# adds another tupple
# comma needed for 1 element
# tuples_grades = tuples_grades + (100,)
# print(tuples_grades)

# print (grades[0])

# grades[0] = 60
# print(grades[0])

# error -- because of immutability
# tuples_grades[0] = 60
# print(tuples_grades)

# error -- because it is unordered
# set_grades[0] = 60
# print(set_grades)

# adds and prints 60
# set_grades.add(60)
# set_grades.add(60)
# print(set_grades)



# set operations -- unique and unordered

# your_lotter_numbers = {1, 2, 3, 4, 5}
# winning_numbers = {1, 3, 5, 7, 9, 11}

# prints the same values
# print(your_lotter_numbers.intersection(winning_numbers))

# prints both values in the lists -- add sets together
# print(your_lotter_numbers.union(winning_numbers))

# eliminates same values and prints remaining
# print({1, 2, 3, 4}.difference({1,2}))



