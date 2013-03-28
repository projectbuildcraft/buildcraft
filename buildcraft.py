#!/usr/bin/python
"""
    Buildcraft: A Build Order Calculator for Starcraft II: Heart of the Swarm
    Copyright (C) 2013 Project Buildcraft

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import bcorder
from constants import * 
from bcevent import boost
import gui


my_order = bcorder.Order(filename = "orders/OC Opening.bo")
run = True
racemap = {
	0 : "P",
	1 : "T",
	2 : "Z",
}
while run:

	my_order.print_out()
	print "[0] Load"
	print "[1] Save"
	print "[2] Insert"
	print "[3] Append"
	print "[4] New"
	print "[5] Quit"
	print "[6] Anaylsis"
	print "[7] Graph"
	print "[8] Set note"
	if my_order.race == "Z":
		print "[9] Toggle gas trick"
	menu_choice = int(raw_input("=>\t"))
	if menu_choice == 0:
		filename = str(raw_input("Load file: "))
		my_order = bcorder.Order(filename = filename)
	elif menu_choice == 1:
		filename = str(raw_input("Save to: "))
		my_order.save(filename)
		if (filename == ""):
			print "Saved to", my_order.default_location
		else:
			print "Saved to", filename
	elif menu_choice == 2:
		index = int(raw_input("Insert at: "))
		choices = my_order.all_available(index)
		for choice_index,event_index in enumerate(choices):
			print choice_index,bcorder.name(event_index)
		choice = int(raw_input("=> "))
		if events[choices[choice]].get_result() == boost:
			pass
		else:
			my_order.insert([choices[choice],''],index)
	elif menu_choice == 3:
		choices = my_order.all_available()
		for choice_index,event_index in enumerate(choices):
			print choice_index,bcorder.name(event_index)
		choice = int(raw_input("=> "))
		if events[choices[choice]].get_result() == boost:
			boostable = []
			for p in my_order.at[len(my_order.events)].production:
				for r in bcorder.get_requirements(p[0][0]):
					if r[1] == O and r[0] in {NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE,
								  STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES}:
						boostable.append([p[0][0], p[1]])
						break
			for boostable_index, boost_info in enumerate(boostable):
				print boostable_index, events[boost_info[0]].get_name(), "with", boost_info[1], "sec remaining"
			extra_choice = int(raw_input("=> "))
			my_order.append([choices[choice], '', boostable[extra_choice][0], boostable[extra_choice][1]])
		else:
			my_order.append([choices[choice],''])
	elif menu_choice == 4:
		name = str(raw_input("Name: "))
		print "[0] Protoss"
		print "[1] Terran"
		print "[2] Zerg"
		race = int(raw_input("Race: "))
		my_order = bcorder.Order(name = name,race = racemap[race])
	elif menu_choice == 5:
		run = False
	elif menu_choice == 6:
		gui.instance_analysis(my_order)
	elif menu_choice == 7:
		print "[0] Supply Graph"
		print "[1] Army Value Graph"
		print "[2] Resource Collection Rate"
		print "[3] Resources on Hand"
		menu_choice_2 = int(raw_input("=>\t"))
		if menu_choice_2 == 0:
			gui.supply_graph(my_order)
		elif menu_choice_2 == 1:
			gui.army_value_graph(my_order)
		elif menu_choice_2 == 2:
			gui.resource_collection_rate_graph(my_order)
		elif menu_choice_2 == 3:
			gui.resource_graph(my_order)
	elif menu_choice == 8:
		choice = int(raw_input("Index: "))
		print "Note was", my_order.get_note(choice)
		my_order.set_note(choice,str(raw_input("Set note to: ")))
	elif menu_choice == 9:
		index = int(raw_input("Index: "))
		if my_order.can_trick(index):
			my_order.toggle_trick(index)
			print "Toggled"
		else:
			print "Can't trick there"
