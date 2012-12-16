class Event:
	def __init__(self,data):
		self.data = data
	names = ["Build SCV",
		"Build Supply Depot",
		"Build Barracks",
		"Build Marine"]
	def name(self):
		return Event.names[self.data]

