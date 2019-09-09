# Each rule contains a single clause as conclusion(head) and a body contains several clauses as premises
class Rule():
    def __init__(self, head, body):
        	self.head = head
        	self.body = body


    def __repr__(self):  # specifies how to display
        return  self.head

# Each Clause is a clause with specified predicate and atoms
class Clause():
	def __init__(self, predicate, atoms):
		self.predicate = predicate
		self.atoms = atoms

	def substitude(self,atoms,mag_atoms):

		for j in range(0,len(self.atoms)):
			for i in range(0 ,len(atoms)):
				if self.atoms[j] == atoms[i]:
					self.atoms[j]= mag_atoms[i]
	def copy(self):
		return Clause(self.predicate,self.atoms[:])


	def __repr__(self):  # specifies how to display
		if len(self.atoms) == 2:
			return  self.atoms[0] + ' '+self.predicate+ ' '+ self.atoms[1]
		if len(self.atoms) ==1:

			return  self.predicate + self.atoms[0]

class Strong_against(Clause):
	def __init__(self, atoms):
		Clause.__init__(self, 'strong_against', atoms)

class Counter(Clause):
	def __init__(self, atoms):
		Clause.__init__(self, 'counter', atoms)
class Synergy(Clause):
	def __init__(self, atoms):
		Clause.__init__(self, 'synergy', atoms)

class Ability(Clause):
	def __init__(self, atoms):
		Clause.__init__(self, 'ability', atoms)
class Weak_against(Clause):
	def __init__(self, atoms):
		Clause.__init__(self, 'weak_against', atoms)
class Strong_ally(Clause):
	def __init__(self, atoms):
		Clause.__init__(self, 'strong_ally', atoms)




rule_list = [
Rule(Strong_against(['A','B']), [Counter(['C','D']),Ability(['A','C']),Ability(['B','D'])]),
Rule(Weak_against(['A','B']), [Strong_against(['B','A'])]),
Rule(Strong_ally(['A','B']), [Synergy(['B','A']), Ability(['A','C']),Ability(['B','D'])]),
]

rule_list2  =[]
test_head =['1']
for i in range (1,99):
	test_head.append(str(100-i))
	rule_list2.append(Rule(Clause(str(100-i),['A']),[Clause(str(99-i),['A']),Clause(str(99-i),['A'])]))


rule_list2.append(Rule(Clause('1',['A']),[Ability(['A','Healing'])]))



