import datalog


TEAM = 1
ENEMY =-1
infinity =999

def minimax(teamPicks, enemyPicks, depth, player):
    """
    Minimax function that choice the best pick
    :param teamPicks and enemyPicks: current state of the drafting
    :param depth: node index in the tree (0 <= depth <= 9) accoridng to the empty team positions
    :param player: who is the maximizer
    :return: a list with [the best pick, best score]
    """
    if player == TEAM:
        best = [-1, -infinity]
    else:
        best = [-1, +infinity]

    if depth == 0 :
        score = evaluate(teamPicks, enemyPicks)
        return [-1, score]

    for hero in datalog.heroes.values():
        if hero not in teamPicks and hero not in enemyPicks:

            if player == ENEMY:
        	   enemyPicks.append(hero)
            if player == TEAM:
        	   teamPicks.append(hero)

            score = minimax(teamPicks, enemyPicks, depth - 1, -player)

            if player == ENEMY :
        	   enemyPicks.pop()
            if player == TEAM :
        	   teamPicks.pop()


            score[0] = hero.name

            if player == TEAM:
                if score[1] > best[1]:
                    best = score  # max value
            else:
                if score[1] < best[1]:
                    best = score  # min value

    return best

def evaluate(teamPicks, enemyPicks):
	score = 0
	for teamPick in teamPicks:
		for enemyPick in enemyPicks:
			if datalog.strong_against(teamPick,enemyPick):
				score += 1
			if datalog.weak_against(teamPick,enemyPick):
				score -= 1
        for otherPick in teamPicks:
            if otherPick != teamPicks:
                if datalog.synergy(teamPick,otherPick):
                    score += 1
	return score



