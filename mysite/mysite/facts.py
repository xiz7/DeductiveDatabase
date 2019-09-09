class Fact():
    def __init__(self, predicate, atoms):
        self.predicate = predicate
        self.atoms = atoms
		

    def __repr__(self):  # specifies how to display
    	return  self.atoms[0] + ' '+self.predicate+ ' '+ self.atoms[1]



def generateList(heroes):
	fact_list = {'range':[],'ability':[],'difficulty':[],'tier':[]}
	for hero in heroes:
		fact_list['range'].append(Fact('range',[hero.name,hero.range]))
		for atom in hero.ability:
			fact_list['ability'].append(Fact('ability',[hero.name,atom]))
		fact_list['difficulty'].append(Fact('difficulty',[hero.name,hero.difficulty]))
		fact_list['tier'].append(Fact('tier',[hero.name,hero.tier]))


	fact_list['counter'] = [
	Fact('counter',['Burst','Squishy']),
	Fact('counter',['Nuker','Squishy']),
	Fact('counter',['Anti-healing','Healing']),
	Fact('counter',['Phantom','Continued-Stun']),
	Fact('counter',['Continued-Stun','Split']),
	Fact('counter',['Debuff','Attribute-dependent']),
	Fact('counter',['Silencer','Transform']),
	Fact('counter',['Vision','Invisable']),
	Fact('counter',['Goal-directed','Escape']),
	Fact('counter',['Goal-directed','Squishy']),
	Fact('counter',['Suppress','Late']),
	Fact('counter',['AOE','Phantom']),
	Fact('counter',['Split','Phantom']),
	Fact('counter',['Anti-dispel','Dispel']),
	Fact('counter',['Dispel','Disabler']),
	Fact('counter',['Lost_mana','Burst']),
	Fact('counter',['Steal_strength','Strength']),
	Fact('counter',['Escape','Continued-DPS']),


	Fact('counter_non',['Pusher','AOE']),
	Fact('counter_non',['Phantom','AOE']),
	Fact('counter_non',['Continued-DPS','Escape']),

	Fact('synergy',['Nasty','Grave'])

	]
	return fact_list



def generateTest(heroes):
	fact_list = {'ability':[]}


	fact_list['ability'] = [Fact('ability',['morphling','Healing']),Fact('ability',['haha','haha']),Fact('ability',['haha','haha']),Fact('ability',['haha','haha'])]
	return fact_list


