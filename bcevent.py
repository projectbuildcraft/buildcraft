class Event:
	def __init__(self,data):
		self.data = data
	names = ["Build SCV",
		"Build Supply Depot",
		"Build Barracks",
		"Build Marine"]
	def name(self):
		return Event.names[self.data]
		
class Event2:
	def __init__(self,name,production_unit,cost,requirements,time,result,args):
		self.name = name
		self.production_unit = production_unit # occupied by event; building, larvae, etc.
		self.cost = cost #(minerals,gas)
		self.requirements = requirements # set of requirements in addition to p_unit and cost
		self.time = time
		self.result = result # a function to be called that modifies the player's overall state
		self.args = args # args for result function
	
	def add_unit(player,unit): # player of a class that stores the player's current state
		player.units[unit] += 1
	
	build_drone = Event2("Build Drone",'larvae',(50,0),None,17,add_unit,'drone')
	build_scv = Event2("Build SCV",'command center',(50,0),None,17,add_unit,'scv')
	build_probe = Event2("Build Probe",'nexus',(50,0),None,17,add_unit,'probe')
	build_hatchery = Event2("Build Hatchery",'drone',(300,0),None,100,expand,'hatchery')
	build_command_center = Event2("Build Command Center",'scv',(400,0),None,100,expand,'command center')
	build_nexus = Event2("Build Nexus",'probe',(400,0),None,100,expand,'nexus')

