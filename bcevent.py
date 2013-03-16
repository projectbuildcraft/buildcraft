import copy

class Event:

	def __init__(self,name,minerals,gas,supply,capacity,time,result,args,requirementss):
		self.name = name
		self.cost = (minerals,gas)
        self.supply = supply
        self.capacity = capacity
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

def add_units(units,instance): # like add_unit but takes a list
	for unit in units:
		add_unit(unit,instance)

def name(index):
	return events[index].get_name()

def get_requirements(index):
	return events[index].get_requirements()

# class Requirement:

	# def __init__(self,unit,kind):
		# self.unit = unit
		# self.kind = kind # Occupation, Assumption, Consumption, Not

	# def unit(self):
		# return self.unit

	# def kind(self):
		# return self.kind

