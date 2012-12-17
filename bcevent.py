class Event:
	def __init__(self,name,production_unit,cost,requirements,time,result,args):
		self.name = name
		self.cost = cost #(minerals,gas)
		self.requirements = requirements # set of requirements in addition to cost
		self.time = time
		self.result = result # a function to be called that modifies the player's overall state after the event
		self.args = args # args for result function
	
	def add_unit(player,unit): # player of a class that stores the player's current state
		player.units[unit] += 1
	
	build_drone = Event("Build Drone",(50,0),None,17,add_unit,'drone')
	build_scv = Event("Build SCV",(50,0),None,17,add_unit,'scv')
	build_probe = Event("Build Probe",(50,0),None,17,add_unit,'probe')
	build_hatchery = Event("Build Hatchery",(300,0),None,100,expand,'hatchery')
	build_command_center = Event("Build Command Center",(400,0),None,100,expand,'command center')
	build_nexus = Event("Build Nexus",(400,0),None,100,expand,'nexus')

