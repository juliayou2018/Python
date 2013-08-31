class intSet(object):
	
	def __init__(self):
		self.vals = []

	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)

	def member(self, e):
		return e in self.vals

	def remove(self, e):
		try:
			self.vals.remove(e)
		except:
			raise ValueError(srt(e) + ' not found')

	def __str__(self):
		self.vals.sort()
		return '(' + ','.join([str(e) for e in self.vals]) + ')'

import datetime

class Person(object):

	def __init__(self, name):
		self.name = name
		self.birthday = None
		self.lastName = name.split(' ')[-1]

	def getLastName(self):
		return self.lastName

	def setBirthday(self, month, day, year):
		self.birthday = datetime.date(year, month, day)

	def getAge(self):
		if self.birthday == None:
			raise ValueError
		return (datetime.date.today() - self.birthday).days

	def __lt__(self, other):
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName

	def __str__(self):
		return self.name

class MITPerson(Person):
	nextIdNum = 0

	def __init__(self, name):
		Person.__init__(self, name)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1

	def getIdNum(self):
		return self.idNum

	def __lt__(self, other):
		return self.idNum < other.idNum

class UG(MITPerson):

	def __init__(self, name, classYear):
		MITPerson.__init__(self, name)
		self.year = classYear

	def getClass(self):
		return self.year()

class Grad(MITPerson):
	pass

def isStudent(obj):
	return isinstance(obj, UG) or isinstance(obj, Grad)
		
