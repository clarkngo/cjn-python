def methodception(another):
	return another()

def add_two_numbers():
	return 35 + 77

print(methodception(add_two_numbers))


print(methodception(lambda: 35 + 77)) # anonymous function

my_list = [13, 56, 77, 484]
# my_list.remove(13) 
# my_list.remove(56)

print(list(filter(lambda x: x !=13, my_list)))

# (lambda x: x * 3)(5)

# def f(x):
# 	return x * 3

# f(5)

##

def not_thirteen(x):
	return x != 13

print(list(filter(not_thirteen, my_list)))

print([x for x in my_list if x!= 13])
