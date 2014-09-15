import pulp
import csv

class Armor:
	def __init__(self, row):
		self.name = row[0]
		self.ar = float(row[1])
		self.w = float(row[15])
		self.var = pulp.LpVariable(self, 0, 1, pulp.LpInteger)

	def __repr__(self):
		return "Armor(%s, %f, %f)" % (self.name, self.ar, self.w)

	def getAr(self):
		return self.var * self.ar

	def getW(self):
		return self.var * self.w


def getObj(armors):
	return [a.getAr() for a in armors]

def getRestr(armors):
	return [a.getW() for a in armors]

def readarmors(filename):
	with open(filename, 'r') as csvfile:
		armorreader = csv.reader(csvfile)
		return [Armor(row) for row in list(armorreader)[1:]]
	return []





arms = readarmors("Dark Souls 2 Armor - Arms.csv")
chests = readarmors("Dark Souls 2 Armor - Chest.csv")
heads = readarmors("Dark Souls 2 Armor - Head.csv")
legs = readarmors("Dark Souls 2 Armor - Legs.csv")

armors = arms + chests + heads + legs

def solveProblemWithRestr(weigthLimit):
	prob = pulp.LpProblem("myProblem", pulp.LpMaximize)
	
	# Only one of each piece
	prob += sum([a.var for a in arms]) <= 1.0
	prob += sum([a.var for a in chests]) <= 1.0
	prob += sum([a.var for a in heads]) <= 1.0
	prob += sum([a.var for a in legs]) <= 1.0

	# Maximum Weigth
	restr = sum(getRestr(armors))
	prob += restr <= weigthLimit

	obj = sum(getObj(armors))
	prob += obj


	status = prob.solve()
	
	print("| Name | Armor Rating |  Weigth |")
	print("|:-----|------:|------:|")
	
	for a in armors:
		if pulp.value(a.var) > 0:
			print("|", a.name, "|", a.ar, "|", a.w, "|")

	print("| Total | ", pulp.value(obj), "|", pulp.value(restr), "|")


for r in [x * 5.0 for x in range(12)[1:]]:
	print("Limit: %f" % r)
	print("")
	solveProblemWithRestr(r)
	print("")
	
