class Person:

	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

   def __init__(self, firstName, lastName, id, scores):
    Person.__init__(self, firstName, lastName, id)
    self.scores=scores

   def calculate(self):
    av=0
    grade=''
    for i in range(len(self.scores)):
      av=av+self.scores[i]
    av=av/len(self.scores)
    if (av <= 100) and (av>=90) : grade='O'
    elif (av < 90) and (av>=80) : grade='E'
    elif (av < 80) and (av>=70) : grade='A'
    elif (av < 70) and (av>=55) : grade='P'
    elif (av < 55) and (av>=40) : grade='D'
    else : grade='T'
    return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
