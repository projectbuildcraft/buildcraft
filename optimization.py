from bcorder import Order
import copy
def genetic_optimization(race, constraints):
	"""
	Returns the optimal build order for fitting the given constraints, having calculated it via a genetic algorithm
	Optimality is measured according to time required to meet constraints. A build is deemed optimal (perhaps improperly) if it remains king for many trials
	Constraints is an array of units required in the form [(UNIT_INDEX, UNIT_COUNT)]
	Race denotes the race: "Z", "P", or "T"
	"""
	orders = [randomly_fit(race, constraints)] * 10
	while we_should_continue(orders):
		# find best
		fitness = [(index,when_meets(order,constraints)) for index,order in enumerate(orders)]
		fitness = sorted(fitness, key = lambda item: item[1]) # sort by fitness
		# reproduce (best six sexually and best asexually) with mutation, producing 4 new ones to replace 4 worst
		orders[fitness[0][0]] = reproduce(orders[fitness[9][0]])
		for order_index in range(1,4):
			orders[fitness[order_index][0]] = reproduce(orders[fitness[9 - 2*order_index][0]],orders[fitness[10 - 2*order_index][0]])
	return max(orders, key = lambda order: when_meets(order,constraints))
	
def a_star_optimization(race, constraints):
	"""
	Returns the optimal build order for fitting the given constraints, having calculated it via an A* search
	Optimality is measured according to time required to meet constraints. This function necessarily returns a most optimal build
	Contraints is an array of units required in the form [(UNIT_INDEX, UNIT_COUNT)]
	Race denotes the race: "Z", "P", or "T"
	"""
	frontier = PriorityQueue(maxsize = -1) # no limit
	frontier.put((1,Order(race = race)))
	while not frontier.empty():
		current_order = frontier.get()
		for option in current_order.all_available(): # somehow we need to handle gas tricks
			extension = copy.deepcopy(current_order)
			extension.append([option]) # need to make sure it has all of event_info
			if extension.sanity_check(): # if makes sense
				if has_constraints(extension.at_time[-1]):
					return extension
				frontier.put((cost(extension) + heuristic(extension), extension))
	return None
	
	
def when_meets(order, constraints):
	"""
	Returns the time at which the build order meets the constraints, or 'inf' if it doesn't
	"""
	for instance in order.at_time:
		if has_constraints(instance):
			return instance.time
	return float('inf')

def has_constraints(instance, constraints):
	"""
	Returns true if the instance meets the constraints
	"""
	for index, count in constraints:
		if instance.units[index] < count:
			return False
	return True

def randomly_fit(race,constraints):
	"""
	Returns a random build order that fits the given constraints or fills supply
	"""
	order = bcorder.Order(race = race)
	while not has_constraints(order.at_time[-1]) and order.at_time[-1].supply <= 200 and order.at_time[-1].time < float('inf'):
		choices = my_order.all_available()
		choice = random.randint(0,len(choices) - 1)
		if events[choices[choice]].get_result() == boost:
			boostable = []
			for p in my_order.at[len(my_order.events)].production:
				for r in bcorder.get_requirements(p[0][0]):
					if r[1] == O and r[0] in {NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE,
								  STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES}:
						boostable.append([p[0][0], p[1]])
						break
			extra_choice = random.randint(0,len(boostable) - 1)
			my_order.append([choices[choice], '', boostable[extra_choice][0], boostable[extra_choice][1]])
		else:
			my_order.append([choices[choice],''])
	return order

def reproduce(order1, order2 = None):
	"""
	Returns a new organism with mutation
	"""
	if order2 == None:
		child = copy.deepcopy(order1)
		child = mutate(child)
	else:
		while True:
			events_list = []
			pass
			child = Order(race = order1.race,events_list = events_list)
			if child.sanity_check(): # not a monster
				break
		child = mutate(child)
	return child

def mutate(order):
	pass

def we_should_continue(orders, constraints):
	pass

def heuristic(order, constraints):
	pass

def cost(order, constraints):
	return order.at[-1].time # should be at because that's where we are in the build order right now
