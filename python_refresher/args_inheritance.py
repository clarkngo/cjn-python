class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	@classmethod
	# def friend(cls, origin, friend_name, *args):
	# 	return cls(friend_name, origin.school, *args)
	# def friend(cls, origin, friend_name, **kwargs):
	# 	return cls(friend_name, origin.school, **kwargs)
	def friend(cls, origin, friend_name, *args, **kwargs):
		return cls(friend_name, origin.school, *args, **kwargs)
##

class WorkingStudent(Student):
	def __init__(self, name, school, salary, job_title):
			super().__init__(name,school)
			self.salary = salary
			self.job_title = job_title



anna = WorkingStudent("Anna", "Oxford", 20.00, "Software Developer")
print(anna.salary)

# friend = anna.friend("Greg")
friend = WorkingStudent.friend(anna, "Greg", salary=17.50, job_title="Software Developer")

print(friend.name)
print(friend.school)
print(friend.salary) 


