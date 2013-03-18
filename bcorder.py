import copy
from constants import *

def name(index):
	return events[index].get_name()

def get_requirements(index):
	return events[index].get_requirements()

class Instance:
	"""
	Condition of player at a particular event in their build
	"""
	def __init__(self, time = 1, units = [0]*NUM_UNITS, occupied = [0]*NUM_UNITS, production = [], minerals = 50, gas = 0, supply = 6, cap = 10, blue = 1, gold = 0, energy_units = []):
		self.time = time
		self.units = units # counts indexed by constants
		self.occupied = occupied
		self.production = production # [[Event_Index, Time_Remaining]]
		self.minerals = minerals
		self.gas = gas
		self.supply = supply
		self.cap = cap
		self.blue = blue
		self.gold = gold
		self.energy_units = energy_units # tracks energy: [[Unit_Index, Energy]]

	def resource_rate(self):
		"""
		Calculates the resource collection rate
		Returns a tuple (mineral_rate, gas_rate) per minute
		"""
		# assume optimal workers
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
		"""
		Moves the insteance forward one second
		"""
		self.time += 1
		index = len(self.production)
		mineral_rate, gas_rate = self.resource_rate()
		self.minerals += mineral_rate / float(60)
		self.gas += gas_rate / float(60)
		while index > 0:
			index -= 1
			self.production[index][1] -= 1 # decrease remaining seconds
			if self.production[index][1] <= 0: # if done
				event = events[self.production[index][0]]
				event.get_result()(event.get_args(), self)
				for requirement in event.get_requirements():
					unit, kind = requirement
					if kind == O:
						self.occupied[unit] -= 1
						self.units[unit] += 1
				del self.production[index]
		for energy_unit in self.energy_units:
			energy_unit[1] = min(energy_unit[1] + 0.5625, energy[energy_unit[0]])

	def active_worker_count(self, include_scouts = False):
		count = 0
		for i in [SCV_MINERAL, SCV_GAS, PROBE_MINERAL, PROBE_GAS, DRONE_MINERAL, DRONE_GAS]:
			count += self.units[i]
		if include_scouts:
			for i in [SCV_SCOUT, PROBE_SCOUT, DRONE_SCOUT]:
				count += self.units[i]
		return count

	def army_value(self, include_defensive = False):
		pass

racename = {
	"P" : "Protoss",
	"T" : "Terran",
	"Z" : "Zerg"
}

class Order:
	"""
	Represents a calculated build order
	"""
	def __init__(self,name = "",events = [],filename = None, race = "P"):
		"""
		Creates a build order from a list of events or a filename
		"""
		if (filename != None):
			f = open(filename, 'r')
			lines = f.readlines()
			self.name = lines.pop(0).rstrip()
			self.race = lines.pop(0).rstrip()
			self.events = []
			for line in lines:
				self.events.append(int(line))
			f.close()
		else:
			self.name = name
			self.race = race
			self.events = events
		self.calculate_times()

	def save(self,filename = None):
		"""
		Saves the build order to file specified by filename
		"""
		if filename == None:
			filename = "orders/"+self.name+".bo"
		f = open(filename, 'w')	
		f.write(self.name + "\n")
		f.write(self.race + "\n")
		for index in self.events:
			f.write(str(index) + "\n");

	def print_out(self):
		"""
		Prints the build order to std out
		"""
		print self.name, racename[self.race]
		for index, eventIndex in enumerate(self.events):
			print "{}".format(index), self.at[index + 1].time, name(eventIndex)

	def available(self, order_index, event_index, now = False):
		"""
		Evaluates whether event is available at this order
		Arguments:
		order_index - location in build order
		event_index - event desired
		now - whether to evaluate availability now or eventually
		"""
		# minerals, gas, supply
		if self.at[order_index].minerals < events[event_index].cost[0]: # requires minerals
			if now:
				return False
			else:
				if self.at[order_index].units[SCV_MINERAL] + self.at[order_index].units[PROBE_MINERAL] + self.at[order_index].units[DRONE_MINERAL] + self.at[order_index].units[MULE] + self.at[order_index].occupied[SCV_MINERAL] + self.at[order_index].occupied[PROBE_MINERAL] + self.at[order_index].occupied[DRONE_MINERAL] == 0:
					return False
		if self.at[order_index].gas < events[event_index].cost[1]: # requires gas
			if now:
				return False
			else:
				if self.at[order_index].units[SCV_GAS] + self.at[order_index].units[PROBE_GAS] + self.at[order_index].units[DRONE_GAS] == 0:
					return False
		if events[event_index].supply > 0: # requires supply
			if self.at[order_index].supply + events[event_index].supply > self.at[order_index].cap:
				if now:
					return False
				difference = self.at[order_index].supply + events[event_index].supply - self.at[order_index].cap
				for event,time in self.at[order_index].production:
					difference -= events[event].capacity
				if difference > 0:
					return False
		# requirements
		for requirement in events[event_index].get_requirements():
			unit, kind = requirement
			if kind == ASSUMPTION:
				if self.at[order_index].units[unit] > 0:
					continue
				if self.at[order_index].occupied[unit] > 0:
					continue
				if now:
					return False
				else:
					for event,time in self.at[order_index].production:
						if events[event].get_result() == add:
							if unit in events[event].get_args():
								break
					else:
						return False
				continue
			if kind == OCCUPATION or kind == CONSUMPTION:
				if self.at[order_index].units[unit] > 0:
					continue
				if now:
					return False
				else:
					if self.at[order_index].occupied[unit] > 0:
						continue
					for event,time in self.at[order_index].production:
						if events[event].get_result() == add:
							if unit in events[event].get_args():
								break
					else:
						return False
					continue
			if kind == NOT:
				if self.at[order_index].units[unit] > 0:
					return False
				for event,time in self.at[order_index].production:
					if event.get_result() == research:
						if unit in event.get_args:
							return False
				continue
			# requirement must be energy
			cost = kind
			for energy_unit, energy_energy in self.at[order_index].energy_units:
				if unit == energy_unit:
					if now:
						return energy_energy > cost
					else:
						break
			else:
				return False
			continue
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
		now = Instance()
		if self.race == "P":
			now.units[PROBE_MINERAL] = 6
			now.units[NEXUS] = 1
			now.energy_units.append([NEXUS,energy(NEXUS)[0]])
			pass
		if self.race == "T":
			now.units[SCV_MINERAL] = 6
			now.units[COMMAND_CENTER] = 1
			pass
		if self.race == "Z":
			now.units[DRONE_MINERAL] = 6
			now.units[HATCHERY] = 1
			now.units[LARVA] = 3
			pass
		now.blue = 1
		self.at = [now] # at[0] is initial state, at[1] is state at which can do first event, etc
		impossible = False
		for index, event in enumerate(self.events):
			index += 1
			last = self.at[index - 1]
			now = Instance(last.time, copy.deepcopy(last.units), copy.deepcopy(last.occupied), copy.deepcopy(last.production), last.minerals, last.gas, last.blue, last.gold)
			self.at.append(now)
			if (not impossible) and (self.available(index, event, False)):
				while not self.available(index, event, True):
					now.increment()
				now.minerals -= events[event].cost[0]
				now.gas -= events[event].cost[1]
				now.supply += events[event].supply
				now.cap += events[event].capacity
				for requirement in get_requirements(event):
					unit, kind = requirement
					if kind == O:
						now.units[unit] -= 1
						now.occupied[unit] += 1
					if kind == C:
						now.units[unit] -= 1
					if kind > 20: # energy
						greatest_index = 0
						greatest_energy = 0
						for energy_index, [energy_unit, energy_energy] in enumerate(now.energy_units):
							if energy_unit == unit:
								if energy_energy > greatest_energy:
									greatest_energy == energy_energy
									greatest_index = energy_index # these are ENERGY INDICES http://www.youtube.com/watch?v=qRuNxHqwazs
						energy_units[greatest_index] -= kind
				now.production.append([event,events[event].time])
			else:
				impossible = True
				self.at[index] = Instance(float('inf'), copy.deepcopy(last.units), copy.deepcopy(last.occupied), copy.deepcopy(last.production), last.minerals, last.gas, last.blue, last.gold)

