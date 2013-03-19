#!/usr/bin/python
import bcorder
from constants import events
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
	print "[7] Supply Graph"
	menu_choice = int(raw_input("=>\t"))
	if menu_choice == 0:
		filename = str(raw_input("Load file: "))
		my_order = bcorder.Order(filename = filename)
	if menu_choice == 1:
		filename = str(raw_input("Save to: "))
		my_order.save(filename)
		print "Saved to ",filename
	if menu_choice == 2:
		index = int(raw_input("Insert at:"))
		choices = [i for i in range(len(events)) if my_order.available(order_index = index, event_index = i)]
		for choice_index,event_index in enumerate(choices):
			print choice_index,bcorder.name(event_index)
		choice = int(raw_input("=> "))
		my_order.insert(choices[choice],index)
		pass
	if menu_choice == 3:
		choices = [i for i in range(len(events)) if my_order.available(order_index = len(my_order.events), event_index = i)]
		for choice_index,event_index in enumerate(choices):
			print choice_index,bcorder.name(event_index)
		choice = int(raw_input("=> "))
		my_order.append(choices[choice])
	if menu_choice == 4:
		name, race = gui.new_order()
		my_order = bcorder.Order(name=name,race=race)
##		name = str(raw_input("Name: "))
##		print "[0] Protoss"
##		print "[1] Terran"
##		print "[2] Zerg"
##		race = int(raw_input("Race: "))
##		my_order = bcorder.Order(name = name,race = racemap[race])
	if menu_choice == 5:
		run = False
	if menu_choice == 6:
		gui.instance_analysis(my_order)
	if menu_choice == 7:
		gui.supply_graph(my_order)
