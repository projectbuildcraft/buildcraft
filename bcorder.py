import copy
from constants import *
class Instance:
	"""
	Condition of player at a particular event in their build
	"""
	def __init__(self, time = 0, units = [0]*NUM_UNITS, production = [], minerals = 50, gas = 0, blue = 1, gold = 0):
		self.time = time
		self.units = units # counts indexed by constants in bcevent
		self.production = production
		self.minerals = minerals
		self.gas = gas
		self.blue = blue
		self.gold = gold

	def resource_rate(self):
		"""
		Calculates the resource collection rate
		Returns a tuple (mineralRate, gasRate) per minute
		"""
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
		# assume optimal workers
		# http://www.teamliquid.net/forum/viewmessage.php?topic_id=140055
		return (59 * workers_on_gold + 42 * workers_on_blue + 25 * saturated_on_gold + 18 * saturated_on_blue + 170 * mules, gassers * 38)
			

	def increment(self):
		"""
		Moves the insteance forward one second
		"""
		index = len(self.production)
		mineral_rate, gas_rate = self.resource_rate()
		self.minerals += mineral_rate / float(60)
		self.gas += gas_rate / float(60)
		while index >= 0:
			self.production[index][1] -= 1 # decrease remaining seconds
			if self.production[index][1] == 0: # if done
				event = self.production[index][0]
				event.get_result()(event.get_args(), self)
				del self.production[index]
			index -= 1

racename = {
	"P" : "Protoss",
	"T" : "Terran",
	"Z" : "Zerg"
}

class Order:
	"""
	Represents a calculated build order
	"""
	def __init__(self,name,events = None,filename = None):
		"""
		Creates a build order from a list of events or a filename
		"""
		if (events == None):
			f = open(filename, 'r')
			lines = f.readlines()
			self.name = lines.pop(0)
			self.race = lines.pop(0)
			self.events = []
			for line in lines:
				self.events.append(int(line))
			f.close()
		else:
			self.name = name
			self.events = events
		self.calculate_times()

	def save(self,filename):
		"""
		Saves the build order to file specified by filename
		"""
		f = open(filename, 'w')	
		f.write(self.name)
		f.write(self.race)
		for index in self.events:
			f.write(str(index) + "\n");

	def printOut(self):
		"""
		Prints the build order to std out
		"""
		print self.name, ":\t", racename[self.race]
		for index, eventIndex in enumerate(self.events):
			print self.at[index].time, name(eventIndex)

	def available(self, OrderIndex, EventIndex, now = False):
		"""
		Evaluates whether event is available at this order
		Arguments:
		OrderIndex - location in build order
		EventIndex - event desired
		now - whether to evaluate availability now or eventually
		"""
		# concern for minerals, gas
		if self.at[OrderIndex].minerals < events[EventIndex].cost[0]: # requires minerals
			if now:
				return False
			else:
				if self.at[OrderIndex].units[SCV_MINERAL] + self.at[OrderIndex].units[PROBE_MINERAL] + self.at[OrderIndex].units[DRONE_MINERAL] + self.at[OrderIndex].units[MULE]	+ self.at[OrderIndex].occupied[SCV_MINERAL] + self.at[OrderIndex].occupied[PROBE_MINERAL] + self.at[OrderIndex].occupied[DRONE_MINERAL] == 0:
					return False
		if self.at[OrderIndex].gas < events[EventIndex].cost[1]: # requires gas
			if now:
				return False
			else:
				if self.at[OrderIndex].units[SCV_GAS] + self.at[OrderIndex].units[PROBE_GAS] + self.at[OrderIndex].units[DRONE_GAS] == 0:
					return False
		for requirement in events[EventIndex].get_requirements():
			if requirement[1] == ASSUMPTION or requirement[1] == OCCUPATION or requirement[1] == CONSUMPTION:
				if self.at[OrderIndex].units[requirement[0]] > 0:
					continue
				if (requirement[0] in self.at[OrderIndex].production) and not now: # production
					continue
				return False
			if requirement[1] == NOT:
				if self.at[OrderIndex].units[requirement[0]] > 0:
					return False
				if requirement[0] in self.at[OrderIndex].production:
					return False
		return True

	def append(self, event):
		"""
		Appends event to the build order
		"""
		self.events.append(event)
		self.calculate_times()

	def insert(self, event, index):
		"""
		Inserts event at index
		"""
		self.events.insert(index, event)
		self.calculate_times()

	def delete(self, index):
		"""
		Deletes event at index
		"""
		del self.events[index]
		self.calculate_times()

	def deleteMany(self, indices):
		"""
		Deletes events at indices
		"""
		for index in indices.sort().reverse():
			self.delete(index)
		self.calculate_times()

	def calculate_times(self):
		"""
		Evaluates the times at which all events occur
		"""
		self.at = []
		impossible = False
		for index, event in enumerate(self.events):
			if index == 0:
				now = Instance()
				if self.race == "P":
					now.units[PROBE_MINERAL] = 6
					now.units[NEXUS] = 1
					pass
				if self.race == "T":
					now.units[SCV_MINERAL] = 6
					now.units[COMMAND_CENTER] = 1
					pass
				if self.race == "Z":
					now.units[DRONE_MINERAL] = 6
					now.units[HATCHERY] = 1
					pass
				now.blue = 1
			else:
				last = self.at[index - 1]
				now = Instance(last.time, copy.deepcopy(last.units), copy.deepcopy(last.production), last.minerals, last.gas, last.blue, last.gold)
			self.at.append(now)
			if (not impossible) and (self.available(index, event)):
				while not self.available(index, event, True):
					now.increment()
			else:
				impossible = True
				now = Instance(float('inf'), self.at[index-1].units.deepcopy(), self.at[index-1].production.deepcopy(), last.minerals, last.gas, last.blue, last.gold)

