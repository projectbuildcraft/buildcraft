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

class Instance:
	def __init__(self, time, units, production, minerals, gas, blue, gold):
		self.time = time
		self.units = units
		self.production = production
		self.minerals = minerals
		self.gas = gas
		self.blue = blue
		self.gold = gold

	def resource_rate(self): # (mineralRate, gasRate) per minute
		# assume optimal workers
		# add MULE
		workers = self.units[SCV_MINERAL] + self.units[PROBE_MINERAL] + self.units[DRONE_MINERAL]
		workers_on_gold = min(self.gold * 12, workers)
		workers -= workers_on_gold
		workers_on_blue = min(self.blue * 16, workers)
		workers -= workers_on_blue
		saturated_on_gold = min(self.gold * 6, workers)
		workers -= saturated_on_gold
		saturated_on_blue = min(self.blue * 8, workers)
		mules = self.units[MULE]
		gassers = self.units[SCV_GAS] + self.units[PROBE_GAS] + self.units[DRONE_GAS]
		gasses = self.units[ASSIMILATOR] + self.units[EXTRACTOR] + self.units[REFINERY]
		gassers = min(gassers, 3 * gasses)
		# http://www.teamliquid.net/forum/viewmessage.php?topic_id=140055
		return (59 * workers_on_gold + 42 * workers_on_blue + 25 * saturated_on_gold + 18 * saturated_on_blue + 170 * mules, gassers * 38)
			

	def increment(self):
		index = len(self.production)
		self.minerals,self.gas += float(self.resource_rate()) / float(60)
		while index >= 0:
			self.production[index][1] -= 1
			if self.production[index][1] == 0:
				event = self.production[index][0]
				event.get_result()(event.get_args(), self)
				del self.production[index]
			index -= 1

class Order:

	def __init__(self,name,events = None,filename = None):
		if (events == None):
			f = open(filename, 'r')
			lines = f.readlines()
			self.name = lines.pop(0)
			self.events = []
			for line in lines:
				self.events.append(int(line))
			f.close()
		else:
			self.name = name
			self.events = events
		self.calculate_times()

	def save(self,filename):
		f = open(filename, 'w')	
		for index in self.events:
			f.write(str(index) + "\n");

	def printOut(self):
		print self.name
		for index, eventIndex in enumerate(self.events):
			print self.at[index].time, name(eventIndex)

	def available(self, OrderIndex, EventIndex, now = False):
		# concern for minerals, gas
		if self.at[OrderIndex].minerals < events[EventIndex].cost[0]: # requires minerals
			if now:
				return False
			else:
				if self.at[OrderIndex].units[SCV_MINERAL] + self.at[OrderIndex].units[PROBE_MINERAL] + self.at[OrderIndex].units[DRONE_MINERAL] + self.at[OrderIndex].units[MULE]
				+ self.at[OrderIndex].occupied[SCV_MINERAL] + self.at[OrderIndex].occupied[PROBE_MINERAL] + self.at[OrderIndex].occupied[DRONE_MINERAL] == 0:
					return False
		if self.at[OrderIndex].gas < events[EventIndex].cost[1]: # requires gas
			if now:
				return False
			else:
				if self.at[OrderIndex].units[SCV_GAS] + self.at[OrderIndex].units[PROBE_GAS] + self.at[OrderIndex].units[DRONE_GAS] == 0:
					return False
		for requirement in get_requirements(EventIndex):
			if requirement.kind() == ASSUMPTION or requirement.kind() == OCCUPATION or requirement.kind() == CONSUMPTION:
				if self.at[OrderIndex].units[requirement.unit()] > 0:
					continue
				if (requirement.unit() in self.at[OrderIndex].production) and not now: # production
					continue
				return False
			if requirement.kind() == NOT:
				if self.at[OrderIndex].units[requirement.unit()] > 0:
					return False
				if requirement.unit() in self.at[OrderIndex].production:
					return False
		return True

	def append(self, event):
		self.events.append(event)
		self.calculate_times()

	def insert(self, event, index):
		self.events.insert(index, event)
		self.calculate_times()

	def delete(self, index):
		del self.events[index]
		self.calculate_times()

	def deleteMany(self, indices):
		for index in indices.sort().reverse():
			self.delete(index)
		self.calculate_times()

	def calculate_times(self):
		self.at = []
		impossible = False
		for index, event in enumerate(self.events):
			if index == 0:
				now = Instance(0,[],[],50,0)
			else:
				last = self.at[index - 1]
				now = Instance(last.time, copy.deepcopy(last.units), copy.deepcopy(last.production), last.minerals, last.gas)
			self.at.append(now)
			if (not impossible) and (self.available(index, event)):
				while not self.available(index, event, True):
					now.increment()
			else:
				impossible = True
				now = Instance(float('inf'), self.at[index-1].units.deepcopy(), self.at[index-1].production.deepcopy())

