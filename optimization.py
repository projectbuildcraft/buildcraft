import bcorder
def genetic_optimization(race, constraints):
	"""
	Returns the optimal build order for fitting the given constraints, having calculated it via a genetic algorithm
	Optimality is measured according to time required to meet constraints. A build is deemed optimal (perhaps improperly) if it remains king for many trials
	Constraints is an array of units required in the form [(UNIT_INDEX, UNIT_COUNT)]
	Race denotes the race: "Z", "P", or "T"
	"""
	orders = [randomly_fit(race, constraints)]
	
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