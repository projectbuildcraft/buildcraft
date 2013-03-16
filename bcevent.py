import copy
class Event:

	def __init__(self,name,cost,requirements,time,result,args):
		self.name = name
		self.cost = cost #(minerals,gas)
		self.requirements = requirements # list of requirements in addition to cost; has to be a list because archons
		self.time = time
		self.result = result # a function to be called that modifies the player's overall state after the event
		self.args = args # args for result function

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

DRONE = 0
SCV = 1
PROBE = 2
HATCHERY = 3
COMMAND_CENTER = 4
NEXUS = 5

events = [
	Event("Build Drone",(50,0),[],17,add_unit,DRONE),
	Event("Build SCV",(50,0),[],17,add_unit,SCV),
	Event("Build Probe",(50,0),[],17,add_unit,PROBE),
	Event("Build Hatchery",(300,0),[],100,add_unit,HATCHERY),
	Event("Build Command Center",(400,0),[],100,add_unit,COMMAND_CENTER),
	Event("Build Nexus",(400,0),[],100,add_unit,NEXUS)
]

class Requirement:

	def __init__(self,unit,kind):
		self.unit = unit
		self.kind = kind # Occupation, Assumption, Consumption, Not

	def unit(self):
		return self.unit

	def kind(self):
		return self.kind

