import hero_data
import rules
import facts
import time

TEAM =1
ENEMY =-1
RULES_HEAD = ['strong_against']
FACTS_HEAD = ['counter','ability','range','tier','difficulty']
VARIABLE_LIST = ['A','B','C','D','X']
def sortFunc(e):
  return e.tier

heroes = hero_data.generateList()
# heroes.sort(key = sortFunc)
fact_list = facts.generateList(heroes.values())

Enemy = []
Team = []
favorites = []
suggestions = {}
current_team = ENEMY



def query(resolvent,statement,pick):

	# While the resolvent is not emepty do:
	if len(resolvent) >0:
		# choose a goal from the resolvent

		goal = resolvent.pop()
		# choose a clause from rules
		if goal.predicate in RULES_HEAD or goal.predicate in rules.test_head:
			for rule in rules.rule_list:
				if rule.head.predicate == goal.predicate:
					for small_goal in rule.body:
						small_goal.substitude(rule.head.atoms,goal.atoms)
						
						resolvent.append(small_goal)

					
					query(resolvent,statement,pick)

		# or choose a clase from facts
		elif goal.predicate in FACTS_HEAD:

			# loop through each fact


			for fact in fact_list[goal.predicate]:
				
				variables = 0 
				unequal_terms = 0
				i = 0 
				while i < len(fact.atoms) :
					if goal.atoms[i] in VARIABLE_LIST:
						variables = variables + 1
						if goal.atoms[i] == 'X':
							pick = fact.atoms[i]
					elif goal.atoms[i] != fact.atoms[i]:
						break

					i = i+1

				if i == len(fact.atoms):

					
					
					new_resolvent = []
					for sgoal in resolvent:
						new_resolvent.append(sgoal.copy())
					

					new_statement = statement + ' ' +fact.__repr__()+ '.'
					if variables != 0:
						for j in range(0, len(new_resolvent)):
							

							new_resolvent[j].substitude(goal.atoms,fact.atoms)


					else:
						# if the resolvent is empty, a solution is found
						if len(resolvent)==0:

							suggestions[pick] = new_statement
							
					#Whenever we find an substitution, we recursively call the query with new resolvent.
					query(new_resolvent,new_statement,pick)
						
	else:
		if len(resolvent)==0:

			suggestions[pick] = statement
# for i in range(1,11):
# 	start = time.time()
# 	query([rules.Goal(str(i),['X'])],'explain: ','X')
# 	end = time.time()
# 	print end-start	


		
def deduce():

    for pick in Enemy:
    	query([rules.Clause('strong_against',['X',pick.name])],'explain: ','X')



def strong_against(heroA, heroB):
	return False
def weak_against(heroA, heroB):
	return strong_against(heroB, heroA)


def teamPick(heroname):
	if len(Team)<=5:
		if heroes[heroname] not in Team and heroes[heroname] not in Enemy:
			Team.append(heroes[heroname])

def enemyPick(heroname):
	if len(Enemy)<=5:
		if heroes[heroname] not in Enemy and heroes[heroname] not in Team :
			Enemy.append(heroes[heroname])

def redo():
	removePick()
	suggestions.clear()
def removePick():
	if current_team == ENEMY:
		if len(Enemy) >=1:
			Enemy.pop()
		elif len(Team) >=1:
			Team.pop()
	else:
		if len(Team) >=1:
			Team.pop()
		elif len(Enemy) >=1:
			Enemy.pop()
def redoSuggest():
	suggestions.clear()
