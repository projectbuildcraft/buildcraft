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
from constants import events
from bcevent import boost
import gui

my_order = bcorder.Order()
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
		choices = [i for i in range(len(events)) if my_order.available(order_index = index, event_index = i)]
		for choice_index,event_index in enumerate(choices):
			print choice_index,bcorder.name(event_index)
		choice = int(raw_input("=> "))
		if events[choices[choice]].get_result() == boost:
			pass
		else:
			my_order.insert([choices[choice],''],index)
		pass
	elif menu_choice == 3:
		choices = [i for i in range(len(events)) if my_order.available(order_index = len(my_order.events), event_index = i)]
		for choice_index,event_index in enumerate(choices):
			print choice_index,bcorder.name(event_index)
		choice = int(raw_input("=> "))
		if events[choices[choice]].get_result() == boost:
			pass
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
		
