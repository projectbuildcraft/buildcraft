from bcorder import Order
from bcevent import boost
from constants import *
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
	frozen_constraints = frozenset(constraints)
	orders = [randomly_fit(race, frozen_constraints) for x in xrange(10)]
	print "Randomly generated"
	king_count = 0
	king = 0
	while king_count < 30: # 30 or some other arbitrarily medium-high number
		# find best
		fitness = [(index,when_meets(order,constraints)) for index,order in enumerate(orders)]
		fitness = sorted(fitness, key = lambda item: -item[1]) # sort by fitness
		print fitness
		# reproduce (best six sexually and best asexually) with mutation, producing 4 new ones to replace 4 worst
		orders[fitness[0][0]] = reproduce(orders[fitness[9][0]], None, frozen_constraints)
		if king != fitness[9][0]:
			king = fitness[9][0]
			king_count = 1
		else:
			king_count += 1
		for order_index in range(1,4):
			orders[fitness[order_index][0]] = reproduce(orders[fitness[9 - 2*order_index][0]],orders[fitness[10 - 2*order_index][0]],frozen_constraints)
	return min(orders, key = lambda order: when_meets(order,constraints))
	
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
				if has_constraints(extension.at_time[-1],constraints):
					return extension
				frontier.put((cost(extension) + heuristic(extension), extension))
	return None
	
	
def when_meets(order, constraints):
	"""
	Returns the time at which the build order meets the constraints, or 'inf' if it doesn't
	"""
	upper = len(order.at_time) - 1
	if not has_constraints(order.at_time[upper],constraints):
		return float('inf')
	lower = 0
	while upper > lower:
		mid = int((upper - lower) / 2 + lower)
		if has_constraints(order.at_time[mid],constraints):
			upper = mid
		else:
			lower = mid + 1
	return order.at_time[upper].time

def has_constraints(instance, constraints):
	"""
	Returns true if the instance meets the constraints
	Constraints is an iterable with elements (UNIT, COUNT)
	"""
	for (index, count) in constraints:
		if instance.units[index] < count:
			return False
	return True

def randomly_fit(race,constraints):
	"""
	Returns a random build order that fits the given constraints or fills supply
	Constraints is a frozen set with elements (UNIT, COUNT)
	"""
	set_up(constraints)
	order = Order(race = race)
	while not has_constraints(order.at_time[-1],constraints) and order.at_time[-1].supply < 200 and order.at_time[-1].time < float('inf'):
		choices = [i for i in order.all_available() if helps(i,constraints)]
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

def reproduce(order1, order2, constraints):
	"""
	Returns a new organism with mutation
	For asexual, pass None for order2
	Constraints - a frozen set of tuples representing guidelines (UNIT, COUNT)
	"""
	if order2 == None:
		child = copy.deepcopy(order1)
		mutate(child,constraints)
	else:
		while True:
			events_list = []
			for index in xrange(max(len(order1.events),len(order2.events))):
				options = []
				if index < len(order1.events):
					options.append(order1.events[index])
				if index < len(order2.events):
					options.append(order2.events[index])
				events_list.append(random.choice(options))
			child = Order(race = order1.race,events_list = events_list)
			if child.sanity_check(): # not a monster
				break
		mutate(child,constraints)
	return child

def mutate(order, constraints):
	"""
	Produces a mutated build order attempting to still meet the constraints given
	Constraints - a frozen set of constraints formatted (UNIT, COUNT)
	"""
	index = 0 # will index order.events
	while index <= len(order.events):
		mutation = random.randint(0,15)
		if mutation < 8: # do nothing
			index += 1
		elif mutation == 9: # insert
			if index < len(order.events):
				order.calculate_times() # we shouldn't have to calculate all though
				choices = [event for event in xrange(len(events)) if helps(event, constraints)]
				choices = [choice for choice in choices if order.available(index,choice,False,False)]
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
			if index > 0 and index < len(order.events):
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
				choices = [event for event in xrange(len(events)) if helps(event, constraints)]
				choices = [choice for choice in choices if order.available(index,choice,False,False)]
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
					try:
						order.events[index] = [choices[choice], '']
					except IndexError:
						print "IndexError in subsitution",index,"in",len(order.events),"or",choice,"in",len(choices)
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
	Assumes contributes dictionary initialized at constraints; this can be done with set_up
	Arguments- constraints, a frozen set of constraint tuples: (UNIT, COUNT)
	"""
	return contributes[constraints][event_index]

def set_up(constraints):
	"""
	Ensures the contributes dictionary has an entry for constraints
	Arguments- constraints, a frozen set of constraints tuples
	"""
	if constraints not in contributes:
		needed_units = set(constraints)
		need_minerals = True
		pass # actually see if we benefit from minerals
		if need_minerals:
			needed_units |= set([PROBE_MINERAL,SCV_MINERAL,DRONE_MINERAL])
		need_gas = True
		pass # actually see if we benefit from gas
		if need_gas:
			needed_units |= set([PROBE_GAS,SCV_GAS,DRONE_GAS])
		need_supply = True
		pass # actually see if we benefit from supply
		if need_supply:
			needed_units |= set([SUPPLY_DEPOT,SUPPLY_DEPOT_EXTRA,PYLON,OVERLORD])
		needed_events = set()
		old_length = 0
		for event_index in xrange(len(events)): # initialize
			if events[event_index].get_result() in [add,research,warp]:
				if len([element for element in events[event_index].get_args() if element in needed_units]):
					needed_events.add(event_index)
					needed_units |= set([req for req,kind in events[event_index].get_requirements() if kind in [O,C,A]])
			elif events[event_index].get_result() == mule and need_minerals:
				needed_events.add(event_index)
			elif events[event_index].get_result() == boost:
				needed_events.add(event_index)
		new_length = len(needed_events)
		while old_length != new_length:
			old_length = new_length
			for event_index in xrange(len(events)): # continue
				if events[event_index].get_result() in [add,research,warp]:
					if len([element for element in events[event_index].get_args() if element in needed_units]):
						needed_events.add(event_index)
						needed_units |= set([req for req,kind in events[event_index].get_requirements() if kind in [O,C,A]])
			new_length = len(needed_events)
		contributes[constraints] = {i: (i in needed_events) for i in xrange(len(events))}
	print [key for key in contributes[constraints].iterkeys() if contributes[constraints][key]]
