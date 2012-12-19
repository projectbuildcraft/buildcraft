class Event:
	def __init__(self,name,production_unit,cost,requirements,time,result,args):
		self.name = name
		self.cost = cost #(minerals,gas)
		self.requirements = requirements # list of requirements in addition to cost; has to be a list because archons
		self.time = time
		self.result = result # a function to be called that modifies the player's overall state after the event
		self.args = args # args for result function
	
	def add_unit(player,unit): # player of a class that stores the player's current state
		player.units[unit] += 1
	
	def add_units(player,units): # like add_unit but takes a list
		for unit in units:
			add_unit(player,unit)

	build_drone = Event("Build Drone",(50,0),None,17,add_unit,'drone')
	build_scv = Event("Build SCV",(50,0),None,17,add_unit,'scv')
	build_probe = Event("Build Probe",(50,0),None,17,add_unit,'probe')
	build_hatchery = Event("Build Hatchery",(300,0),None,100,add_unit,'hatchery')
	build_command_center = Event("Build Command Center",(400,0),None,100,add_unit,'command center')
	build_nexus = Event("Build Nexus",(400,0),None,100,add_unit,'nexus')

class Requirement:
	def __init__(self,unit,kind):
		pass # to be implemented for 0.1

class Order:
	def __init__(self,name,events):
		pass # to be implemented for 0.2
	def print(self):
		pass # to be implemented for 0.2
	def calculate_times(self):
		pass # to be implemented for 0.4


