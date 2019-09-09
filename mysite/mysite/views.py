from django.shortcuts import render_to_response
import datalog
import predict
from django.views.decorators.csrf import csrf_exempt


def dota(request):
	Team  = datalog.Team
	Enemy = datalog.Enemy
	current_hero = 'suggestions'
	print 'dota run'
	return render_to_response('Heroes.html', locals())


def deduce(request):
	datalog.redoSuggest()
	Team  = datalog.Team
	Enemy = datalog.Enemy

	datalog.deduce()
	# minim = predict.minimax(Team,Enemy,2,1)
	# print (minim)
	print (datalog.suggestions)
	if len(datalog.suggestions)>=1:
		best = datalog.suggestions.popitem()
		current_hero = best[0]
		roles = datalog.heroes[best[0]].ability
		attack_range = datalog.heroes[best[0]].range
		explanation = best[1]
		print 'deduce run'
		print explanation
	else:
		current_hero = 'suggestions'

	return render_to_response('Heroes.html', locals())

def nextS(request):
	Team  = datalog.Team
	Enemy = datalog.Enemy
	if len(datalog.suggestions)>=1:
		best = datalog.suggestions.popitem()
		current_hero = best[0]
		roles = datalog.heroes[best[0]].ability
		attack_range = datalog.heroes[best[0]].range
		explanation = best[1]
	else:
		current_hero = 'suggestions'

	return render_to_response('Heroes.html', locals())
def team(request):
	Team  = datalog.Team
	Enemy = datalog.Enemy
	datalog.current_team = 1
	current_hero = 'suggestions'

	return render_to_response('Heroes.html', locals())
def enemy(request):
	Team  = datalog.Team
	Enemy = datalog.Enemy
	datalog.current_team = -1
	current_hero = 'suggestions'

	return render_to_response('Heroes.html', locals())
def redo(request):
	datalog.redo()
	Team  = datalog.Team
	Enemy = datalog.Enemy
	current_hero = 'suggestions'
	return render_to_response('Heroes.html', locals())

@csrf_exempt
def pick(request):
	if request.method == 'POST':
		Team  = datalog.Team
		Enemy = datalog.Enemy
		heroname = str(request.POST.get("hero"))
		if datalog.current_team == -1:
			datalog.enemyPick(heroname)
		else:
			datalog.teamPick(heroname)
		current_hero = 'suggestions'
		return render_to_response('Heroes.html', locals())