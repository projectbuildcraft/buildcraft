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
	Returns a random build order that fits the given constraints
	"""
	pass
