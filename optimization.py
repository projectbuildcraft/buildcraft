from bcorder import Order
from bcevent import boost
from constants import events, O, NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE, STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES
import copy
import random

contributes = {} # dynamicly generated dict from constraints tuple to dict of events according to how they contribute to that constraint

def genetic_optimization(race, constraints):
	"""
	Returns the optimal build order for fitting the given constraints, having calculated it via a genetic algorithm
	Optimality is measured according to time required to meet constraints. A build is deemed optimal (perhaps improperly) if it remains king for many trials
	Constraints is an array of units required in the form [(UNIT_INDEX, UNIT_COUNT)]
	Race denotes the race: "Z", "P", or "T"
	"""
	orders = [randomly_fit(race, constraints) for x in xrange(10)]
	print "Randomly generated"
	king_count = 0
	king = 0
	while king_count < 30: # 30 or some other arbitrarily medium-high number
		# find best
		fitness = [(index,when_meets(order,constraints)) for index,order in enumerate(orders)]
		fitness = sorted(fitness, key = lambda item: item[1]) # sort by fitness
		# reproduce (best six sexually and best asexually) with mutation, producing 4 new ones to replace 4 worst
		orders[fitness[0][0]] = reproduce(orders[fitness[9][0]])
		if king != fitness[9][0]:
			king = fitness[9][0]
			king_count = 1
		else:
			king_count += 1
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
		if has_constraints(instance,constraints):
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
	set_up(constraints)
	order = Order(race = race)
	constraints_set = frozenset(constraints)
	while not has_constraints(order.at_time[-1],constraints) and order.at_time[-1].supply < 200 and order.at_time[-1].time < float('inf'):
		choices = [i for i in order.all_available() if helps(i,constraints_set)]
		choice = random.randint(0,len(choices) - 1)
		if events[choices[choice]].get_result() == boost:
			boostable = []
			for p in order.at[len(order.events)].production:
				for r in events[p[0][0]].get_requirements():
					if r[1] == O and r[0] in {NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE,
								  STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES}:
						boostable.append([p[0][0], p[1]])
						break
			if len(boostable) > 0: # we shouldn't really need this, but apparently we do
				extra_choice = random.randint(0,len(boostable) - 1)
				order.append([choices[choice], '', boostable[extra_choice][0], boostable[extra_choice][1]],True,False,True)
		else:
			order.append([choices[choice],''],True,False,True)
	return order

def reproduce(order1, order2 = None):
	"""
	Returns a new organism with mutation
	"""
	if order2 == None:
		child = copy.deepcopy(order1)
		mutate(child)
	else:
		while True:
			events_list = []
			pass
			child = Order(race = order1.race,events_list = events_list)
			if child.sanity_check(): # not a monster
				break
		mutate(child)
	return child

def mutate(order):
	"""
	produces
	"""
	index = 0 # will index order.events
	while index <= len(order.events):
		mutation = random.randint(0,15)
		if mutation < 8: # do nothing
			index += 1
		elif mutation == 9: # insert
			order.calculate_times() # we shouldn't have to calculate all though
			choices = order.all_available(index)
			choice = random.randint(0,len(choices) - 1)
			if events[choices[choice]].get_result() == boost:
				boostable = []
				for p in order.at[index].production:
					for r in events[p[0][0]].get_requirements():
						if r[1] == O and r[0] in {NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE,
									  STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES}:
							boostable.append([p[0][0], p[1]])
							break
				if len(boostable) > 0:
					extra_choice = random.randint(0,len(boostable) - 1)
					event_info = [choices[choice], '', boostable[extra_choice][0], boostable[extra_choice][1]]
					if index == len(order.events):
						order.append(event_info, False, False)
					else:
						order.insert(event_info, index, False, False)
			else:
				event_info = [choices[choice], '']
				if index == len(order.events):
					order.append(event_info, False, False)
				else:
					order.insert(event_info, index, False, False)
			index += 1
		elif mutation == 10: # delete
			if index < len(order.events):
				order.delete(index,False, False)
		elif mutation == 11: # swap before
			if index > 0:
				order.events[index], order.events[index - 1] = order.events[index - 1], order.events[index]
		elif mutation == 12: # race-specific tweaks
			if order.race == "P":
				pass # modify chrono boost
			if order.race == "Z":
				pass # toggle gas trick 
			if order.race == "T":
				pass # idk
		elif mutation == 13: # swap after
			if index < len(order.events) - 1:
				order.events[index], order.events[index + 1] = order.events[index + 1], order.events[index]
		else: # substitution
			if index < len(order.events):
				order.calculate_times()
				choices = order.all_available(index)
				choice = random.randint(0,len(choices) - 1)
				if events[choices[choice]].get_result() == boost:
					boostable = []
					for p in order.at[index].production:
						for r in events[p[0][0]].get_requirements():
							if r[1] == O and r[0] in {NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE,
										  STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES}:
								boostable.append([p[0][0], p[1]])
								break
					if len(boostable) > 0:
						extra_choice = random.randint(0,len(boostable) - 1)
						order.events[index] = [choices[choice], '', boostable[extra_choice][0], boostable[extra_choice][1]]
				else:
					order.events[index] = [choices[choice], '']
			index += 1
	order.calculate_times()


def heuristic(order, constraints):
	pass
	return 0

def cost(order, constraints):
	return order.at[-1].time # should be at because that's where we are in the build order right now

def helps(event_index, constraints):
	"""
	Returns whether the event at event_index will help an order meet the constraints
	Assumes contributes dictionary initialized at constraints
	Arguments- constraints, a frozen set of constraint tuples: (UNIT, COUNT)
	"""
	return contributes[constraints][event_index]

def set_up(constraints):
	"""
	Ensures the contributes dictionary has an entry for constraints
	Arguments- constraints, an iterable of constraints tuples
	"""
	constraints_index = frozenset(constraints)
	if constraints_index not in contributes:
		needed_units = [unit for unit,count in constraints]
		need_minerals = True
		pass # actually see if we benefit from minerals
		if need_minerals:
			needed_units.extend([PROBE_MINERAL,SCV_MINERAL,DRONE_MINERAL])
		need_gas = True
		pass # actually see if we benefit from gas
		if need_gas:
			needed_units.extend([PROBE_GAS,SCV_GAS,DRONE_GAS])
		need_supply = True
		pass # actually see if we benefit from supply
		if need_supply:
			needed_units.extend([SUPPLY_DEPOT,PYLON,OVERLORD])
		needed_events = set()
		old_length = 0
		for event_index in xrange(len(events)): # initialize
			if events[event_index].get_result() in [add,research,warp]:
				if len([intersecting_element for element in events[event_index].get_args() if element in needed_units]):
					needed_events.add(event_index)
					needed_units.intersect(set([req for req,kind in events[event_index].get_requirements() if kind in [O,C,A]]))
			elif events[event_index].get_result() == mule and need_minerals:
				needed_events.add(event_index)
			elif events[event_index].get_result() == boost:
				needed_events.add(event_index)
		new_length = len(needed_events)
		while old_length != new_length:
			old_length = new_length
			for event_index in xrange(len(events)): # continue
				if events[event_index].get_result() in [add,research,warp]:
					if len([intersecting_element for element in events[event_index].get_args() if element in needed_units]):
						needed_events.add(event_index)
						needed_units.intersect(set([req for req,kind in events[event_index].get_requirements() if kind in [O,C,A]]))
			new_length = len(needed_events)
		contributes[constraints_index] = {i: (i in needed_events) for i in xrange(len(events))}
