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

	def _lt_(self, other):
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

class TransferStudent(MITPerson):
        pass

class Grad(MITPerson):
        pass

def isStudent(obj):
        return isinstance(obj, Student)
