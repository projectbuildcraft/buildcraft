import copy
class Event:

	def __init__(self,name,minerals,gas,supply,capacity,time,result,args,requirements):
		self.name = name
		self.cost = (minerals,gas)
		self.supply = supply
		self.capacity = capacity
		self.time = time
		self.result = result # a function to be called that modifies the player's overall state after the event
		self.args = args # args for result function
		self.requirements = requirements # list of requirements in addition to cost, a set of tuples (req, type)

	def get_name(self):
		return self.name

	def get_requirements(self):
		return self.requirements
	
	def get_result(self):
		return self.result

	def get_args(self):
		return self.args

def add_unit(unit, instance): # player of a class that stores the player's current state
	instance.units[unit] += 1
	from constants import energy
	if unit in energy:
		if energy[unit][2] != None and instance.units[energy[unit][2]] > 0: # energy upgrade
			instance.energy_units.append([unit,energy[unit][0] + 25])
		else:
			instance.energy_units.append([unit,energy[unit][0] + 25])

def add_units(units,instance): # like add_unit but takes a list
	for unit in units:
		add_unit(unit,instance)

add = add_units

def mule(nonsense,instance):
	from constants import MULE
	instance.units[MULE] += 1
	# mule dies
	pass

def mule_dies(nonsense,instance):
	from constants import MULE
	instance.units[MULE] -= 1

def idle(unit,instance):
	pass

def salvage(resources,instance):
	instance.minerals += resources[0]

def research(topics,instance):
	for topic in topics:
		instance.units[topic] = 1

def boost(event_index, time_remaining, instance):
        if event_index not in instance.boosted_things[0]:
                instance.boosted_things[0][event_index] = []
        instance.boosted_things[0][event_index].append([time_remaining, 20])

def warp(result,instance):
	from constants import WARPGATE_ON_COOLDOWN, WARPGATE
	unit, cooldown = result
	add_unit(unit,instance)
	instance.production.append(WARPGATE_ON_COOLDOWN,cooldown)
	# negate effect of removing warpgate
	instance.units[WARPGATE] -= 1
	instance.occupied[WARPGATE] += 1

def spawn_larva(auto,instance):
	from constants import LARVA, AUTO_SPAWN_LARVA, events
	if auto:
		instance.units[LARVA] += 1
		# assume added to least
		min_index = 0
		min_larva = instance.base_larva[min_index]
		for index, larva in enumerate(instance.base_larva):
			if larva < min_larva:
				min_larva = larva
				min_index = index
		instance.base_larva[min_index] += 1
		if min_larva >= 3:
			print "ERROR: Larva fault"
		if min_larva < 2:
			instance.production.append([AUTO_SPAWN_LARVA, events[AUTO_SPAWN_LARVA].time])
		# test for additional spawn
	else:
		instance.units[LARVA] += 4
		# assume added to least
		min_index = 0
		min_larva = instance.base_larva[min_index]
		for index, larva in enumerate(instance.base_larva):
			if larva < min_larva:
				min_larva = larva
				min_index = index
		instance.base_larva[min_index] += 4
		if min_larva < 3:
			# find most recent AUTO_SPAWN_LARVA and stop it
			spawn_index = None
			max_time = 0
			for index, (event_index, time_remaining) in instance.production:
				if event_index == AUTO_SPAWN_LARVA:
					if time > max_time:
						spawn_index = index
						max_time = time
			if max_time > 0: # if found one
				del instance.production[spawn_index]
        
        
        

# class Requirement:

	# def __init__(self,unit,kind):
		# self.unit = unit
		# self.kind = kind # Occupation, Assumption, Consumption, Not

	# def unit(self):
		# return self.unit

	# def kind(self):
		# return self.kind

