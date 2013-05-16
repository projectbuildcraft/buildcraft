"""
    Copyright (C) 2013 Project Buildcraft
    License notice in buildcraft.py
"""
import copy
import string
from constants import *

def name(event_index):
    return events[event_index].get_name()

def get_requirements(event_index):
    return events[event_index].get_requirements()

class Instance:
    """
    Condition of player at a particular event in their build
    """
    def __init__(self, time = 1, units = None, occupied = None, production = None, minerals = 50, gas = 0, supply = 6, cap = 10, blue = 1, gold = 0, energy_units = None, base_larva = None, boosted_things = None):
        self.time = time
        if units == None:
            self.units = [0]*NUM_UNITS
        else:
            self.units = units # counts indexed by constants
        if occupied == None:
            self.occupied = [0]*NUM_UNITS
        else:
            self.occupied = occupied
        if production == None:
            self.production = []
        else:
            self.production = production # [[Event_Info], Time_Remaining, Order_Index]]
        self.minerals = minerals
        self.gas = gas
        self.supply = supply
        self.cap = cap
        self.blue = blue
        self.gold = gold
        if energy_units == None:
            self.energy_units = []
        else:
            self.energy_units = energy_units # tracks energy: [[Unit_Index, Energy]]
        if base_larva == None:
            self.base_larva = []
        else:
            self.base_larva = base_larva # tracks larva [larva_count]
        if boosted_things == None:
            self.boosted_things = [dict(),                      
                           {NEXUS: [],
                        GATEWAY: [],
                        FORGE: [],
                        CYBERNETICS_CORE: [],
                        ROBOTICS_FACILITY: [],
                        WARPGATE: [],
                        STARGATE: [],
                        TWILIGHT_COUNCIL: [],
                        ROBOTICS_BAY: [],
                        FLEET_BEACON: [],
                        TEMPLAR_ARCHIVES: []}]
        else:
            self.boosted_things = boosted_things # tracks Chrono Boosted events and structures: [{Order_Index: chrono_left}, {Unit_Index: [chrono_left]}]
        
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

    def larva_rate(self):
        """
        Returns the larva rate one would expect from perfect injections and spending in larva produced per Blizzard minute
        """
        zerg_bases = len(self.base_larva)
        producing_hatcheries = len([None for larva in self.base_larva if larva < 3])
        queens = self.units[QUEEN] + self.occupied[QUEEN]
        return 4*(producing_hatcheries) + 6*min(zerg_bases,queens)
            
    def increment(self, start_times, end_times):
        """
        Moves the instance forward one second
        """
        self.time += 1
        index = len(self.production)
        mineral_rate, gas_rate = self.resource_rate()
        if self.time > 4:
            self.minerals += mineral_rate / float(60)
            self.gas += gas_rate / float(60)
        while index > 0:
            index -= 1
            if self.production[index][2] in self.boosted_things[0].keys() and self.boosted_things[0][self.production[index][2]] > 0:
                self.production[index][1] -= .5 # boosted effect
            self.production[index][1] -= 1 # decrease remaining seconds
            if self.production[index][1] <= 0: # if done
                end_times[self.production[index][2]] = self.time
                event = events[self.production[index][0][0]]
                if events[self.production[index][0][0]].get_result() == boost: # has special parameters
                    boost(self.production[index][0][3], self)
                elif events[self.production[index][0][0]].get_result() == warp:
                    start_times[-self.production[index][2]] = self.time
                    warp(event.get_args(), self, self.production[index][2])
                else:
                    event.get_result()(event.get_args(), self)
                self.cap += event.capacity
                self.cap = min(self.cap, 200)
                for requirement in event.get_requirements():
                    unit, kind = requirement
                    if kind == O:
                        while(self.occupied[unit] == 0):
                            unit = can_be[unit] # if this fails it can be because of issues with available and calculate_times
                        self.occupied[unit] -= 1
                        self.units[unit] += 1
                if self.production[index][2] in self.boosted_things[0].keys():
                    for requirement in event.get_requirements():
                        unit, kind = requirement
                        if kind == O:
                            self.boosted_things[1][unit].append(self.boosted_things[0][self.production[index][2]])
                            del self.boosted_things[0][self.production[index][2]]
                del self.production[index]
        for energy_unit in self.energy_units:
            energy_unit[1] = min(energy_unit[1] + 0.5625, energy[energy_unit[0]])
        for boosted_event_index in self.boosted_things[0].iterkeys():
            self.boosted_things[0][boosted_event_index] -= 1
        for boosted_structure in self.boosted_things[1].iterkeys():
            i = len(self.boosted_things[1][boosted_structure])
            while i > 0:
                i -= 1
                self.boosted_things[1][boosted_structure][i] -= 1

    def active_worker_count(self, include_scouts = False, include_occupied = False):
        count = 0
        for i in [SCV_MINERAL, SCV_GAS, PROBE_MINERAL, PROBE_GAS, DRONE_MINERAL, DRONE_GAS]:
            count += self.units[i]
            if include_occupied:
                count += self.occupied[i]
        if include_scouts:
            for i in [SCV_SCOUT, PROBE_SCOUT, DRONE_SCOUT]:
                count += self.units[i]
        return count

    def worker_supply(self, include_production = True):
        count = self.active_worker_count(include_scouts = True, include_occupied = True)
        if include_production:
            for event_info, time, index in self.production:
                event = events[event_info[0]]
                if event.get_result() == add:
                    for unit in event.get_args():
                        if unit in [SCV_MINERAL, PROBE_MINERAL, DRONE_MINERAL, SCV_GAS, PROBE_GAS, DRONE_GAS, SCV_SCOUT, PROBE_SCOUT, DRONE_SCOUT]:
                            count += 1
        return count

    def army_value(self, include_defensive = False):
        """
        Returns [mineral,gas] of spending on army, optionally including defensive units
        """
        value = [0,0]
        army_counts = [[index, self.units[index]] for index in range(NUM_UNITS) if self.units[index] > 0 and index in army_units]
        for index,count in army_counts:
            value[0] += army_units[index][0] * count
            value[1] += army_units[index][1] * count
        if include_defensive:
            defensive_counts = [[index, self.units[index]] for index in range(NUM_UNITS) if self.units[index] > 0 and index in defensive_units]
            for index,count in defensive_counts:
                value[0] += defensive_units[index][0] * count
                value[1] += defensive_units[index][1] * count
        return value

    def larva_in_production(self):
        larva = 0
        for event_info,time in self.production:
            if event_info[0] == SPAWN_LARVA:
                larva += 4
            elif event_info[0] == AUTO_SPAWN_LARVA:
                larva += 1
        return larva

    def __deepcopy__(self, memo = None):
        return Instance(self.time, copy.deepcopy(self.units), copy.deepcopy(self.occupied), copy.deepcopy(self.production), self.minerals, self.gas, self.supply, self.cap, self.blue, self.gold, copy.deepcopy(self.energy_units), copy.deepcopy(self.base_larva), copy.deepcopy(self.boosted_things))

    def all_available(self, now = False, gas_trick = False):
        return [event_index for event_index in xrange(len(events)) if self.available(event_index, now, gas_trick)]

    def available(self, event_index, now = False, gas_trick = False, chrono_target = None):
        """
        Evaluates whether event is available from this instance
        Arguments:
        event_index - event desired (indexes events)
        now - whether to evaluate availability now or eventually
        gas_trick - whether this is a zerg player who will break supply barriers with gas tricks
        chrono_target - the target, indexing self.events, of the chrono boost, if this is a chrono boost; otherwise None
        """
        # supply, minerals, gas
        required_tricks = 0 # we only really care about this if now because it affects mineral cost
        if events[event_index].supply > 0: # requires supply
            if (self.supply) + (events[event_index].supply) > 200: # will max out supply
                if not gas_trick:
                    return False
            if (self.supply) + (events[event_index].supply) > self.cap:
                if now:
                    if gas_trick:
                        required_tricks += self.supply + events[event_index].supply - self.cap
                    else:
                        return False
                else:
                    difference = self.supply + events[event_index].supply - self.cap
                    for event,time, index in self.production:
                        difference -= events[event[0]].capacity
                    if difference > 0:
                        if not gas_trick:
                            return False
            if gas_trick and now and required_tricks > self.units[DRONE_MINERAL] + self.units[DRONE_SCOUT] + self.units[DRONE_SCOUT]:
                return False
        if gas_trick:
            gas_tricks = min(required_tricks, self.units[DRONE_SCOUT] + 2 * (self.units[HATCHERY] + self.units[LAIR] + self.units[HIVE]) - self.units[ASSIMILATOR])
            evo_tricks = required_tricks - gas_tricks # they either have to be faraway gasses or evo chambers; I think evo chambers are more realistic
            mineral_cost = events[event_index].cost[0] + events[MORPH_EXTRACTOR].cost[0] * gas_tricks + events[MORPH_EVOLUTION_CHAMBER].cost[0] * evo_tricks
        else:
            mineral_cost = events[event_index].cost[0]
        if self.minerals < mineral_cost: # requires minerals
            if now:
                return False
            else:
                if self.units[SCV_MINERAL] + self.units[PROBE_MINERAL] + self.units[DRONE_MINERAL] + self.units[MULE] + self.occupied[SCV_MINERAL] + self.occupied[PROBE_MINERAL] + self.occupied[DRONE_MINERAL] == 0:
                    return False
        if self.gas < events[event_index].cost[1]: # requires gas
            if now:
                return False
            else:
                if self.units[SCV_GAS] + self.units[PROBE_GAS] + self.units[DRONE_GAS] == 0:
                    for event_info,time, index in self.production:
                        if events[event_info[0]].get_result() == add: # necessarily means we just added a worker to gas
                            if PROBE_GAS in events[event_info[0]].get_args():
                                break
                            elif DRONE_GAS in events[event_info[0]].get_args():
                                break
                            elif SCV_GAS in events[event_info[0]].get_args():
                                break
                    else:
                        return False
        if now and event_index == SPAWN_LARVA: # then we need to make sure there is a free hatchery
            num_hatcheries = self.units[HATCHERY] + self.units[LAIR] + self.units[HIVE] + self.occupied[HATCHERY] + self.occupied[LAIR] + self.occupied[HIVE]
            num_injections = len([event_info[0] for event_info, time, index in self.production if event_info[0] == SPAWN_LARVA])
            if num_injections >= num_hatcheries:
                return False
        if now and events[event_index].get_result() == boost:
            for p in self.production:
                if p[0][0] == CHRONO_BOOST and p[0][3] == chrono_target:
                    return False
            if chrono_target in self.boosted_things[0]:
                if self.boosted_things[0][chrono_target] > 0:
                    return False
        # requirements
        requirements = list(events[event_index].get_requirements()) # our dirty copy
        for requirement in requirements:
            unit, kind = requirement
            if kind == ASSUMPTION:
                if now and unit in [EXTRACTOR, ASSIMILATOR, REFINERY]: # should we wait for another to finish?
                    gassers = self.units[PROBE_GAS] + self.units[SCV_GAS] + self.units[DRONE_GAS]
                    for event_info,time,index in self.production:
                        event_index = event_info[0]
                        if events[event_index].get_result() == add:
                            for arg in events[event_index].get_args():
                                if arg in [PROBE_GAS, SCV_GAS, DRONE_GAS]:
                                    gassers += 1 # gassers in production
                    gasses = self.units[EXTRACTOR] + self.units[ASSIMILATOR] + self.units[REFINERY]
                    if gassers >= 3 * gasses: # it certainly seems so
                        for event_info, time, index in self.production: # let's check
                            if events[event_info[0]].get_result() == add and events[event_info[0]].get_args()[0] in [EXTRACTOR, ASSIMILATOR, REFINERY]: # there is in fact another on the way
                                return False # I'll wait then
                if self.units[unit] > 0:
                    continue
                if self.occupied[unit] > 0:
                    continue
                if now:
                    if unit in can_be: # can be other value
                        requirements.append((can_be[unit],ASSUMPTION))
                        continue
                    else:
                        return False
                else:
                    for event_info,time, index in self.production:
                        if events[event_info[0]].get_result() == add or events[event_info[0]].get_result() == research:
                            if unit in events[event_info[0]].get_args():
                                break
                    else:
                        if unit in can_be:
                            requirements.append((can_be[unit],ASSUMPTION))
                            continue
                        else:
                            return False
                continue
            if kind == OCCUPATION or kind == CONSUMPTION:
                if self.units[unit] > 0:
                    continue
                if now:
                    if kind == OCCUPATION and unit in can_be: # can be other value
                        requirements.append((can_be[unit],OCCUPATION))
                        continue
                    else:
                        return False
                else:
                    if self.occupied[unit] > 0:
                        continue
                    for event_info,time, index in self.production:
                        if events[event_info[0]].get_result() == add or events[event_info[0]].get_result() == research:
                            if unit in events[event_info[0]].get_args():
                                break
                        elif unit == LARVA and events[event_info[0]].get_result() == spawn_larva:
                                break
                    else:
                        if kind == OCCUPATION and unit in can_be: # can be other value
                            requirements.append((can_be[unit],OCCUPATION))
                            continue
                        else:
                            return False
                    continue
            if kind == NOT:
                if self.units[unit] > 0 or self.occupied[unit] > 0:
                    return False
                for event,time, index in self.production:
                    event_index = event[0]
                    if events[event_index].get_result() == research or events[event_index].get_result() == add:
                        if unit in events[event_index].get_args():
                            return False
                continue
            # requirement must be energy
            cost = kind
            for energy_unit, energy_energy in self.energy_units:
                if unit == energy_unit:
                    if now:
                        if energy_energy < cost:
                            continue
                        else:
                            break
                    else:
                        break
            else: # must be in production
                if now:
                    return False
                for event_info,time, index in self.production:
                    if events[event_info[0]].get_result() == add:
                        if unit in events[event_info[0]].get_args():
                            break
                else:
                    return False
            continue
        return True
   

racename = {
    "P" : "Protoss",
    "T" : "Terran",
    "Z" : "Zerg"
}

class Order:
    """
    Represents a calculated build order
    """
    def __init__(self,name = "", events_list = None, filename = None, race = "P", calc = True):
        """
        Creates a build order from a list of events or a filename
        """
        if (filename != None):
            self.default_location = filename
            f = open(filename, 'r')
            lines = f.readlines()
            self.name = lines.pop(0).rstrip()
            self.race = lines.pop(0).rstrip() # "Z" "T" or "P"
            self.events = [] # [[event_index, note, targeted_event, time_left]]
            for line in lines:
                line = line.rstrip()
                raw_info = string.split(line)
                events_info = [None,None]
                events_info[0] = int(raw_info.pop(0))
                if self.race == "Z":
                    events_info.append(int(raw_info.pop())) # whether or not to allow extractor trick on this event
                elif events[events_info[0]].get_result() == boost:
                    events_info.append(None) # dummy
                    events_info.append(int(raw_info.pop()))
                    events_info[2] = int(raw_info.pop())
                events_info[1] = string.join(raw_info)
                self.events.append(events_info)
            f.close()
        else:
            self.name = name
            self.default_location = False
            self.race = race
            if events_list == None:
                self.events = []
            else:
                self.events = events_list
        self.time_taken = []
        self.history = [] # [events]
        self.future = [] # [events]
        if calc:
            self.calculate_times()
            self.incorrect_times = False # times have been calculated
        else:
            self.incorrect_times = True # times have not been calculated

    def save(self, filename, purge_history = True):
        """
        Saves the build order to file specified by filename, or to default_location if filename is ""
        """
        if not filename:
            filename = self.default_location
        else:
            self.default_location = filename
        f = open(filename, 'w')
        f.write(self.name + "\n")
        f.write(self.race + "\n")
        for event_info in self.events:
            for i in xrange(len(event_info)):
                f.write(str(event_info[i]) + ("\n" if i == len(event_info) - 1 else " "))
        if purge_history:
            self.history = []

    def race_name(self):
        return racename[self.race]

    def print_out(self):
        """
        Prints the build order to std out
        """
        print self.name, self.race_name()
        for index, event_info in enumerate(self.events):
            print "{}/{} {}. ".format(self.at[index + 1].supply,self.at[index + 1].cap, index + 1), self.at[index + 1].time, name(event_info[0]), event_info[1]
            if self.can_trick(index):
                if self.uses_trick(index):
                    print "(uses supply trick)"
            for i in self.at[index + 1].production:
                print "\t{}: {}".format(i[1], events[i[0][0]].get_name())
                # should include chrono information

    def available(self, order_index, event_index, now = False, gas_trick = False):
        """
        Evaluates whether event is available at this order
        Arguments:
        order_index - location in build order (indexes self.at)
        event_index - event desired (indexes events)
        now - whether to evaluate availability now or eventually
        gas_trick - whether this is a zerg player who will break supply barriers with gas tricks
        """
        # supply, minerals, gas
        required_tricks = 0 # we only really care about this if now because it effects mineral cost
        current = self.at[order_index]
        chrono_target = None
        if events[event_index].get_result() == boost:
            chrono_target = self.events[order_index - 1][3]
        return self.at[order_index].available(event_index, now, gas_trick, chrono_target)
        
    def all_available(self, order_index = -1, gas_trick = False):
        return self.at[order_index].all_available(now = False, gas_trick = gas_trick)

    def sanity_check(self):
        """
        Concept: Rejects build orders that are illogical during optimization search
        Requires calculated times for each event in self.at
        Checks the build order for the following conditions:
            Worker change from gas to minerals and back and vice versa in same second
            Player does not send and receive the same resource in the same second
            Has more than 3 workers per gas
        Returns False if one is met
        """
        current_time = 0
        delta_workers = 0 # keeps track of changes in workers
        delta_minerals = 0
        delta_gas = 0
        for event_index, event in enumerate(self.events):
            at_index = event_index + 1
            if self.at[at_index].time > current_time:
                current_time = self.at[at_index].time
                delta_minerals = 0
                delta_gas = 0
            else:
                gassers = self.at[at_index].units[SCV_GAS] + self.at[at_index].units[PROBE_GAS] + self.at[at_index].units[DRONE_GAS]
                gasses = self.at[at_index].units[ASSIMILATOR] + self.at[at_index].units[EXTRACTOR] + self.at[at_index].units[REFINERY]
                if gassers > 3 * gasses:
                    return False
                if event_index in [SWITCH_DRONE_TO_GAS, SWITCH_PROBE_TO_GAS, SWITCH_SCV_TO_GAS]:
                    if delta_workers < 0:
                        return False
                    delta_workers = 1
                elif event_index in [SWITCH_DRONE_TO_MINERALS, SWITCH_PROBE_TO_MINERALS, SWITCH_SCV_TO_MINERALS]:
                    if delta_workers > 0:
                        return False
                    delta_workers = -1
                else:
                    delta_workers = 0
                    if event_index == GIVE_MINERALS:
                        if delta_minerals > 0:
                            return False
                        delta_minerals = -1
                    elif event_index == RECEIVE_MINERALS:
                        if delta_minerals < 0:
                            return False
                        delta_minerals = 1
                    elif event_index == GIVE_GAS:
                        if delta_gas > 0:
                            return False
                        delta_gas = -1
                    elif event_index == RECEIVE_GAS:
                        if delta_gas < 0:
                            return False
                        delta_gas = 1
        return True
        
    def append(self, event_info, recalc = True, remember = True, only_care_about_last = False):
        """
        Appends event to the build order
        """
        if remember:
            self.future = []
            self.history.append(copy.deepcopy(self.events))
        if self.race == "Z" and len(event_info) == 2: # backwards compatibility
            event_info.append(0)
        self.events.append(event_info)
        if recalc:
            self.calculate_times(only_care_about_last)
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def insert(self, event_info, index, recalc = True, remember = True):
        """
        Inserts event at index
        """
        if remember:
            self.future = []
            self.history.append(copy.deepcopy(self.events))
        if self.race == "Z" and len(event_info) == 2: # backwards compatibility
            event_info.append(0)
        self.events.insert(index, event_info)
        while index < len(self.events):
            if events[self.events[index][0]].get_result() == boost:
                self.events[index][3] += 1
            index += 1
        if recalc:
            self.calculate_times()
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def move(self, this_index, there_index, recalc = True, remember = True, only_care_about_last = False):
        """
        Moves event at this_index to there_index
        this_index indexes self.events
        that_index indexes self.events after removing event at this_index
        """
        if remember:
            self.future = []
            self.history.append(copy.deepcopy(self.events))
        moved = self.events.pop(this_index)
        self.events.insert(there_index, moved)
        while this_index < there_index:
            if events[self.events[this_index][0]].get_result() == boost:
                self.events[this_index][3] -= 1
            this_index += 1
        while this_index > there_index:
            if events[self.events[this_index][0]].get_result() == boost:
                self.events[this_index][3] += 1
            this_index -= 1
        if recalc:
            self.calculate_times(only_care_about_last)
            self.incorrect_times = False
        else:
            self.incorrect_times = True
        

    def insert_chrono(self, boosted_index, chrono_index, recalc = True, remember = True):
        """
        Adds a chrono boost in chrono_index for the event in the given boosted_index
        Because one does not simply insert a chrono
        """
        if remember:
            self.future = []
            self.history.append(copy.deepcopy(self.events))
        event_info = [CHRONO_BOOST, "", self.events[boosted_index][0], boosted_index]
        self.events.insert(chrono_index, event_info)
        while chrono_index < (len(self.events) - 1):
            chrono_index += 1
            if events[self.events[chrono_index][0]].get_result() == boost:
                self.events[chrono_index][3] += 1
        if recalc:
            self.calculate_times()
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def can_chrono(self, boosted_index, chrono_index):
        """
        Returns whether a chrono boost can be applied at chrono_index for an event at boosted_index
        """
        pass # this is a dummy function for now
        return True

    def delete(self, index, recalc = True, remember = True):
        """
        Deletes event at index
        """
        if remember:
            self.future = []
            self.history.append(copy.deepcopy(self.events))
        del self.events[index]
        while index < len(self.events):
            if events[self.events[index][0]].get_result() == boost:
                self.events[index][3] -= 1
            index += 1
        if recalc:
            self.calculate_times()
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def delete_many(self, indices, recalc = True, remember = True):
        """
        Deletes events at indices
        """
        if remember:
            self.future = []
            self.history.append(copy.deepcopy(self.events))
        for index in indices.sort().reverse():
            self.delete(index,False,False)
        if recalc:
            self.calculate_times()
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def calculate_times(self, only_care_about_last = False):
        """
        Evaluates the times at which all events occur
        only_care_about_last - should we avoid calculating things that don't help us with finding the properties of at_time[-1]
        """
        now = Instance()
        start_times = {}
        end_times = {}         
        self.time_taken = {} # event_index -> time_taken
        if self.race == "P":
            now.units[PROBE_MINERAL] = 6
            now.units[NEXUS] = 1
            now.energy_units.append([NEXUS,energy[NEXUS][0]])
        if self.race == "T":
            now.units[SCV_MINERAL] = 6
            now.units[COMMAND_CENTER] = 1
            now.cap = 11 # override default
        if self.race == "Z":
            now.units[DRONE_MINERAL] = 6
            now.units[HATCHERY] = 1
            now.units[LARVA] = 3
            now.units[OVERLORD] = 1
            now.base_larva = [3]
        now.blue = 1
        self.at = [now] # at[0] is initial state, at[1] is state at which can do first event, etc
        self.at_time = []
        impossible = False
        last_good_index = 0 # indexes at[] and keeps track of last legal instance of at
        for index, event_info in enumerate(self.events):
            order_index = index + 1
            last = self.at[index]
            now = copy.deepcopy(last)
            self.at.append(now)
            using_tricks = self.uses_trick(index)
            if (not impossible) and (self.available(order_index, event_info[0], False, using_tricks)):
                last_good_index = order_index
                while not self.available(order_index, event_info[0], True, using_tricks):
                    if not only_care_about_last:
                        self.at_time.append(copy.deepcopy(now))
                    now.increment(start_times, end_times)
                # now effect costs
                if event_info[0] == CHRONO_BOOST:
                    found = False
                    for i in xrange(len(now.production)):
                        if now.production[i][2] == event_info[3]:
                            found = True
                            if now.production[i][0][0] != event_info[2]:
                                for j in xrange(len(now.production)):
                                    if now.production[j][0][0] == event_info[2]:
                                        event_info[3] = now.production[j][2]
                                        break
                                    self.delete(index)
                                    return
                            break
                    if not found:
                        self.delete(index)
                        return
                mineral_cost = events[event_info[0]].cost[0]
                if using_tricks: 
                    required_tricks = max(now.supply + events[event_info[0]].supply - now.cap, 0)
                    gas_tricks = min(required_tricks, now.units[DRONE_SCOUT] + 2 * (now.units[HATCHERY] + now.units[LAIR] + now.units[HIVE]) - now.units[ASSIMILATOR])
                    evo_tricks = required_tricks - gas_tricks # they either have to be faraway gasses or evo chambers; I think evo chambers are more realistic
                    mineral_cost += 6 * gas_tricks + 18 * evo_tricks
                now.minerals -= mineral_cost
                now.gas -= events[event_info[0]].cost[1]
                now.supply += events[event_info[0]].supply
                for requirement in get_requirements(event_info[0]):
                    unit, kind = requirement
                    if kind == O:
                        while(now.units[unit] == 0):
                            unit = can_be[unit] # if this is an error then there is a problem with available
                        now.units[unit] -= 1
                        now.occupied[unit] += 1
                        if unit in now.boosted_things[1].keys():
                            if len(now.boosted_things[1][unit]) > 0:
                                now.boosted_things[0][index] = now.boosted_things[1][unit][0] 
                                del now.boosted_things[1][unit][0]
                    if kind == C:
                        now.units[unit] -= 1
                        if unit == LARVA:
                            # assume larva from base with most larva
                            max_index = 0
                            max_larva = now.base_larva[max_index]
                            for curr_index, larva in enumerate(now.base_larva):
                                if larva > max_larva:
                                    max_index = curr_index
                                    max_larva = larva
                            if max_larva == 3:
                                now.production.append([[AUTO_SPAWN_LARVA,''], events[AUTO_SPAWN_LARVA].time, -1])
                            now.base_larva[max_index] -= 1
                    if kind > 20: # energy
                        greatest_index = 0
                        greatest_energy = 0
                        for energy_index, [energy_unit, energy_energy] in enumerate(now.energy_units):
                            if energy_unit == unit:
                                if energy_energy > greatest_energy:
                                    greatest_energy == energy_energy
                                    greatest_index = energy_index # these are ENERGY INDICES http://www.youtube.com/watch?v=qRuNxHqwazs
                        now.energy_units[greatest_index][1] -= kind
                start_times[index] = now.time
                now.production.append([event_info,events[event_info[0]].time, index])
            else:
                impossible = True
                self.at[order_index] = copy.deepcopy(last)
                self.at[order_index].time = float('inf')
                start_times[index] = float('inf')
                end_times[index] = float('inf')
        self.at_time.append(self.at[last_good_index])
        while len(self.at_time[-1].production) > 0: # simulate through remaining production
            last = copy.deepcopy(self.at_time[-1])
            last.increment(start_times, end_times)
            self.at_time.append(last)
        if not only_care_about_last:
            for i in start_times.iterkeys():
                self.time_taken[i] = end_times[i] - start_times[i]

    def evaluate(self):
        """
        If times have been calculated for this configuration, does nothing
        Otherwise, places final state (except resources) in self.at_time[-1]
        """
        if self.incorrect_times:
            now = Instance()
            if self.race == "P":
                now.units[PROBE_MINERAL] = 6
                now.units[NEXUS] = 1
                now.energy_units.append([NEXUS,energy[NEXUS][0]])
            if self.race == "T":
                now.units[SCV_MINERAL] = 6
                now.units[COMMAND_CENTER] = 1
                now.cap = 11 # override default
            if self.race == "Z":
                now.units[DRONE_MINERAL] = 6
                now.units[HATCHERY] = 1
                now.units[LARVA] = 3
                now.units[OVERLORD] = 1
                now.base_larva = [3]
            now.energy_units = []
            for index, event_info in enumerate(self.events):
                # now effect costs
                now.supply += events[event_info[0]].supply
                for requirement in get_requirements(event_info[0]):
                    unit, kind = requirement
                    if kind == C:
                        if unit != LARVA:
                              now.units[unit] -= 1 # we'll handle larva last
                now.production.append([event_info,0,index])
            while len(now.production) > 0: # simulate through production
                event_info,time,index = now.production.pop()
                event = events[event_info[0]]
                event.get_result()(event.get_args(),now)
            self.at_time = [now]

    def get_note(self,index):
        """
        index: index in self.events, not self.at
        """
        return self.events[index][1]

    def set_note(self,index,note,remember = True):
        """
        index: index in self.events, not self.at
        """
        if remember:
            self.future = []
            self.history.append(copy.deepcopy(self.events))
        self.events[index][1] = note

    def can_trick(self,index):
        """
        index: index in self.events, not self.at
        """
        return self.race == "Z" and events[self.events[index][0]].supply > 0

    def uses_trick(self,index):
        """
        index: index in self.events, not self.at
        """
        if len(self.events[index]) > 2:
            return self.events[index][2] == 1
        else:
            return False

    def toggle_trick(self,index,recalc = True):
        """
        Assumes can_trick(index); otherwise will result in unexpected behavior
        index: index in self.events, not self.at
        """
        if len(self.events[index]) == 2:
            self.events[index].append(1)
        elif self.events[index][2] == 0:
            self.events[index][2] = 1
        else:
            self.events[index][2] = 0
        if recalc:
            self.calculate_times()
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def event_length(self, index):
        """
        Returns how long the event at the index will take, factoring in chrono boosts
        index: index in self.events, not self.at
        """
        return self.time_taken[index]

    def get_warp_cooldown(self, index):
        """
        Returns the length of the cooldown associated with the warp in the given index
        index: index in self.events, not self.at
        """
        if -index in self.time_taken.keys():
            return self.time_taken[-index]
        return 0

    def undo(self, recalc = True):
        """
        Undoes the last change remembered
        """
        self.future.append(copy.deepcopy(self.events))
        self.events = self.history.pop()
        if recalc:
            self.calculate_times()
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def redo(self, recalc = True):
        """
        Redoes the last change undone
        """
        self.history.append(copy.deepcopy(self.events))
        self.events = self.future.pop()
        if recalc:
            self.calculate_times()
            self.incorrect_times = False
        else:
            self.incorrect_times = True

    def can_undo(self):
        return len(self.history) > 0

    def can_redo(self):
        return len(self.future) > 0


class Team:
    """
    Tracks and manages a team of players
    """
    def __init__(self, filename = None, builds = None, number = 0):
        """
        Initializes a team based on a file or a set of Orders or a number of players
        """
        if filename:
            self.default_location = filename
            self.builds = []
            f = open(filename, 'r')
            lines = f.readlines()
            self.name = lines.pop(0).rstrip()
            for line in lines:
                line = line.rstrip()
                if line in ["Z","T","P"]:
                    self.builds.append(Order(race=line))
                else:
                    raw_info = string.split(line)
                    events_info = [None,None]
                    events_info[0] = int(raw_info.pop(0))
                    build = self.builds[-1]
                    if build.race == "Z":
                        events_info.append(int(raw_info.pop())) # whether or not to allow extractor trick on this event
                    elif events[events_info[0]].get_result() == boost:
                        events_info.append(None) # dummy so we can do it backwards
                        events_info.append(int(raw_info.pop()))
                        events_info[2] = int(raw_info.pop())
                    events_info[1] = string.join(raw_info)
                    build.events.append(events_info)
            f.close()
        else:
            if builds == None:
                self.builds = [Order()]*number # count of builds
            else:
                self.builds = builds
                while (len(self.builds) < number):
                    self.builds.append(Order())
        self.history = []
        self.future = []

    def save(self, filename, purge_history = True):
        if not filename:
            filename = self.default_location
        else:
            self.default_location = filename
        f = open(filename, 'w')
        f.write(self.name + "\n")
        for build in self.builds:
            f.write(build.race + "\n")
            for event_info in self.events:
                for i in xrange(len(event_info)):
                    f.write(str(event_info[i]) + ("\n" if i == len(event_info) - 1 else " "))
        if purge_history:
            self.history = []
            self.future = []

    def add_player(self, new_race = 'P', order = None, remember = True):
        """
        Adds a player with the specified order and/or race
        """
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        if order == None:
            self.builds.append(Order(race = new_race))
        else:
            self.builds.append(order)

    def remove_player(self, player = 0, remember = True):
        if remember:
            self.history.append(self.deepcopy(self.builds))
            self.future = []
        del self.builds[player]

    def reset(self, player = 0, race = 'P', remember = True):
        """
        Resets specified player as specified race
        """
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        self.builds[player] = Order(race = race)

    def append(self, event_info, player = 0, remember = True):
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        self.builds[player].append(event_info, remember = False)

    def insert(self, event_info, player = 0, index = 0, remember = True):
        """
        Insert event_info at specified index in specified player's build order
        """
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        self.builds[player].insert(event_info, index, remember = False)

    def delete(self, index, player = 0, remember = True):
        """
        Deletes event at specified index for specified player
        """
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        self.builds[player].delete(index, remember = False)

    def delete_manay(self, indices, player = 0, remember = True):
        """
        Deletes events at specified indices for specified player
        """
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        self.builds[player].delete_many(indices, remember = False)

    def sanity_check(self, check_individual = False):
        """
        Returns whether the builds on the team make sense in a team context, specifically, that they:
            - give and receive minerals at the same time, in the same amounts
        Optionally, also checks for the individual build conditions in Order
        Returns True if the builds make sense, false otherwise
        """
        if check_individual:
            for order in self.builds:
                if not order.sanity_check():
                    return False
        delta_minerals = 0
        delta_gas = 0
        current_time = 0
        event_indices = [0]*len(self.builds)
        pass
        return True

    def add_mineral_gift(self, giver = 0, receiever = 1, time = 360, remember = True):
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        if time < 360:
            pass
        else:
            pass

    def add_gas_gift(self, giver = 0, receiver = 1, time = 360, remember = True):
        if remember:
            self.history.append(copy.deepcopy(self.builds))
            self.future = []
        if time < 360:
            pass
        else:
            pass
            # find index at which to insert gift

    def undo(self):
        self.future.append(copy.deepcopy(self.builds))
        self.builds = self.history.pop()

    def can_undo(self):
        return len(self.history) > 0

    def redo(self):
        self.history.append(copy.deepcopy(self.builds))
        self.builds = self.future.pop()

    def can_redo(self):
        return len(self.future) > 0
