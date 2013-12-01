from bcorder import Order, Instance
from bcevent import boost
from constants import *
import copy
import random
import heapq

contributes = {} # dynamicly generated dict from constraints tuple to dict of events according to how they contribute to that constraint

def genetic_optimization(race, constraints):
    """
    Returns the optimal build order for fitting the given constraints, having calculated it via a genetic algorithm
    Optimality is measured according to time required to meet constraints. A build is deemed optimal (perhaps improperly) if it remains king for many trials
    Constraints is an array of units required in the form [(UNIT_INDEX, UNIT_COUNT)]
    Race denotes the race: "Z", "P", or "T"
    """
    frozen_constraints = frozenset(constraints)
    orders = [randomly_fit(race, frozen_constraints)
    for x in xrange(10)]
    print "Randomly generated"
    king_count = 0
    king = 0
    while king_count < 30: # 30 or some other arbitrarily medium-high number
        # find best
        fitness = [(index,when_meets(order,constraints)) for index,order in enumerate(orders)]
        fitness = sorted(fitness, key = lambda item: -item[1]) # sort by fitness
        # reproduce (best six sexually and best asexually) with mutation, producing 4 new ones to replace 4 worst
        orders[fitness[0][0]] = reproduce(orders[fitness[9][0]], None, frozen_constraints)
        if king != fitness[9][0]:
            king = fitness[9][0]
            king_count = 1
        else:
            king_count += 1
        for order_index in range(1,4):
            orders[fitness[order_index][0]] = reproduce(orders[fitness[9 - 2*order_index][0]],orders[fitness[10 - 2*order_index][0]],frozen_constraints)
    return min(orders, key = lambda order: when_meets(order,constraints))
    
def a_star_optimization(race, constraints):
    """
    Returns the optimal build order for fitting the given constraints, having calculated it via an A* search
    Optimality is measured according to time required to meet constraints. This function necessarily returns a most optimal build
    Contraints is an array of units required in the form [(UNIT_INDEX, UNIT_COUNT)]
    Race denotes the race: "Z", "P", or "T"
    """
    frozen_cons = frozenset(constraints)
    set_up(frozen_cons,race)
    frontier = PriorityQueue() # no limit
    first_instance = Instance()
    first_instance.init_as_race(race)
    # The items in the queue should be a tuple, with the first element being a tuple of events, and the second element being the last instance of those events.
    frontier.push(tuple(), firstInstance), 1)
    while not frontier.isEmpty():
        events_so_far, current_instance = frontier.pop()
        if has_constraints(current_instance, constraints):
            best_order = Order(race = race, events_list = events_so_far)
            return best_order
        # Check all available event options
        for option in current_instance.all_available(): # somehow we need to handle gas tricks #HERE
            if helps(option, frozen_cons):
                extension = (events_so_far + (option,), )
                extension = Order(events_list=copy.copy(current_order.events), race = race)
                if events[option].get_result() == boost:
                    pass
                else:
                    extension.append([option,''], only_care_about_last=True) # need to make sure it has all of event_info
                    if extension.sanity_check(True): # if makes sense
                        frontier.push(extension, cost(extension) + heuristic(extension,constraints))
    raise Exception("a_star optimization shouldn't have exited without a solution.")

def when_meets(order, constraints):
    """
    Returns the time at which the build order meets the constraints, or 'inf' if it doesn't
    """
    upper = len(order.at_time) - 1
    if not has_constraints(order.at_time[upper],constraints):
        return float('inf')
    lower = 0
    while upper > lower:
        mid = int((upper - lower) / 2 + lower)
        if has_constraints(order.at_time[mid],constraints):
            upper = mid
        else:
            lower = mid + 1
    return order.at_time[upper].time

def has_constraints(instance, constraints):
    """
    Returns true if the instance meets the constraints
    Constraints is an iterable with elements (UNIT, COUNT)
    """
    for (index, count) in constraints:
        if instance.units[index] < count:
            return False
    return True

def randomly_fit(race,constraints):
    """
    Returns a random build order that fits the given constraints or fills supply
    Constraints is a frozen set with elements (UNIT, COUNT)
    """
    set_up(constraints, race)
    order = Order(race = race, calc = False)
    order.evaluate()
    while not has_constraints(order.at_time[-1],constraints) and order.at_time[-1].supply < 200:
        choice = random.choice([i for i in order.at_time[-1].all_available() if helps(i,constraints)])
        if events[choice].get_result() == boost:
            pass # caring to allow for chrono boost during random fit would require even more calculation
        else:
            order.append([choice,''],recalc = False,remember = False)
            order.evaluate() # not verified
    return order

def reproduce(order1, order2, constraints):
    """
    Returns a new organism with mutation
    For asexual, pass None for order2
    Constraints - a frozen set of tuples representing guidelines (UNIT, COUNT)
    """
    if order2 == None:
        child = Order(events_list = copy.deepcopy(order1.events), race = order1.race, calc = False)
        mutate(child, constraints)
    else:
        while True:
            events_list = []
            for index in xrange(max(len(order1.events),len(order2.events))):
                options = []
                if index < len(order1.events):
                    options.append(order1.events[index])
                if index < len(order2.events):
                    options.append(order2.events[index])
                events_list.append(random.choice(options))
            child = Order(race = order1.race,events_list = events_list)
            if child.sanity_check(): # not a monster
                break
        mutate(child,constraints)
    return child

def mutate(order, constraints):
    """
    Produces a mutated build order attempting to still meet the constraints given
    Constraints - a frozen set of constraints formatted (UNIT, COUNT)
    """
    index = 0 # will index order.events
    while index <= len(order.events):
        mutation = random.randint(0,15)
        if mutation < 8: # do nothing
            index += 1
        elif mutation == 9: # insert
            if index < len(order.events):
                order.calculate_times() # we shouldn't have to calculate all though
                choices = [event for event in xrange(len(events)) if helps(event, constraints)]
                choice = random.choice([choice for choice in choices if order.available(index,choice,False,False)])
                if events[choice].get_result() == boost:
                    boostable = []
                    for p in order.at[index].production:
                        for r in events[p[0][0]].get_requirements():
                            if r[1] == O and r[0] in {NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE,
                                          STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES}:
                                boostable.append([p[0][0], p[1]])
                                break
                    if len(boostable) > 0:
                        extra_choice = random.randint(0,len(boostable) - 1)
                        event_info = [choice, '', boostable[extra_choice][0], boostable[extra_choice][1]]
                        if index == len(order.events):
                            order.append(event_info, False, False)
                        else:
                            order.insert(event_info, index, False, False)
                else:
                    event_info = [choice, '']
                    if index == len(order.events):
                        order.append(event_info, False, False)
                    else:
                        order.insert(event_info, index, False, False)
                index += 1
        elif mutation == 10: # delete
            if index < len(order.events):
                order.delete(index,False, False)
        elif mutation == 11: # swap before
            if index > 0 and index < len(order.events):
                order.events[index], order.events[index - 1] = order.events[index - 1], order.events[index]
        elif mutation == 12: # race-specific tweaks
            if order.race == "P":
                pass # modify chrono boost
            if order.race == "Z":
                pass # toggle gas trick
            if order.race == "T":
                pass # idk
        elif mutation == 13: # swap after
            if index < len(order.events) - 1:
                order.events[index], order.events[index + 1] = order.events[index + 1], order.events[index]
        else: # substitution
            if index < len(order.events):
                order.calculate_times()
                choices = [event for event in xrange(len(events)) if helps(event, constraints)]
                choices = [choice for choice in choices if order.available(index,choice,False,False)]
                choice = random.randint(0,len(choices) - 1)
                if events[choices[choice]].get_result() == boost:
                    boostable = []
                    for p in order.at[index].production:
                        for r in events[p[0][0]].get_requirements():
                            if r[1] == O and r[0] in {NEXUS, GATEWAY, FORGE, CYBERNETICS_CORE, ROBOTICS_FACILITY, WARPGATE,
                                          STARGATE, TWILIGHT_COUNCIL, ROBOTICS_BAY, FLEET_BEACON, TEMPLAR_ARCHIVES}:
                                boostable.append([p[0][0], p[1]])
                                break
                    if len(boostable) > 0:
                        extra_choice = random.randint(0,len(boostable) - 1)
                        order.events[index] = [choices[choice], '', boostable[extra_choice][0], boostable[extra_choice][1]]
                else:
                    try:
                        order.events[index] = [choices[choice], '']
                    except IndexError:
                        print "IndexError in subsitution",index,"in",len(order.events),"or",choice,"in",len(choices)
            index += 1
    order.calculate_times()


def heuristic(order, constraints):
    heuristics = [0, mining_heuristic(order.at[-1], constraints)]
    return max(heuristics)

def cost(order):
    return order.at[-1].time # should be at because that's where we are in the build order right now

def mining_heuristic(instance, goals):
    """
    TODO
    A lower bound on the time to finish the goals using mining rates
    """
    cost = 0
    for item, count in goals:
        # TODO find lower bound on costs
        pass
    minerals, gas = instance.resource_rate()
    minerals /= 60
    gas /= 60
    # TODO find lower bound on time to reach costs
    pass
    return 0
    

def helps(event_index, constraints):
    """
    Returns whether the event at event_index will help an order meet the constraints
    Assumes contributes dictionary initialized at constraints; this can be done with set_up
    Arguments- constraints, a frozen set of constraint tuples: (UNIT, COUNT)
    """
    return contributes[constraints][event_index]

def set_up(constraints, race):
    """
    Ensures the contributes dictionary has an entry for constraints
    Arguments- constraints, a frozen set of constraints tuples
             - race, "P" for Protoss, "T" for Terran, "Z" for Zerg
    """
    if race == "P":
        r = 0
    elif race == "T":
        r = 1
    elif race == "Z":
        r = 2
    if constraints not in contributes:
        needed_units = set()
        for unit, count in constraints:
            needed_units.add(unit)
        need_minerals = True
        pass # actually see if we benefit from minerals
        if need_minerals:
            needed_units.add([PROBE_MINERAL,SCV_MINERAL,DRONE_MINERAL][r])
        need_gas = gas_helps(constraints,race)
        if need_gas:
            needed_units.add([PROBE_GAS,SCV_GAS,DRONE_GAS][r])
        need_supply = True
        pass # actually see if we benefit from supply
        if need_supply:
            needed_units |= set([[PYLON],[SUPPLY_DEPOT,SUPPLY_DEPOT_EXTRA],[OVERLORD]][r])
        need_scouts = False
        for unit, count in constraints:
            if unit in [PROBE_SCOUT,DRONE_SCOUT,SCV_SCOUT]:
                need_scouts = True
                break
        if need_scouts:
            needed_units |= set([[PROBE_SCOUT],[SCV_SCOUT],[DRONE_SCOUT]][r])
        need_techlab = False
        for unit, count in constraints:
            if unit in techlab_units:
                need_techlab = True
                break
        need_reactor = False
        rax_count = 0
        fac_count = 0
        port_count = 0
        for unit, count in constraints:
            # TODO do not hard code this
            if unit in [REACTOR, BARRACKS_REACTOR, FACTORY_REACTOR, STARPORT_REACTOR]:
                need_reactor = True
                break
            elif unit in [MARINE, REAPER]:
                rax_count += count
                if (rax_count > 1):
                    need_reactor = True
                    break
            elif unit in [HELLION, WIDOW_MINE, HELLBAT]:
                fac_count += count
                if (fac_count > 1):
                    need_reactor = True
                    break
            elif unit in [MEDIVAC, VIKING]:
                port_count += count
                if (port_count > 1):
                    need_reactor = True
                    break
        needed_events = set()
        old_length = 0
        for event_index in xrange(len(events)): # initialize
            if events[event_index].get_result() in [add,research,warp]:
                # if it makes something we need
                if len([1 for element in events[event_index].get_args() if element in needed_units]):
                    needed_events.add(event_index)
                    needed_units |= set([req for req,kind in events[event_index].get_requirements() if kind in [O,C,A]])
            elif race == "T" and events[event_index].get_result() == mule and need_minerals:
                needed_events.add(event_index)
                needed_units.add(MULE)
            elif race == "P" and events[event_index].get_result() == boost:
                needed_events.add(event_index)
            if not need_techlab:
                needed_units -= techlab_units
            if not need_reactor:
                needed_units -= set([REACTOR, BARRACKS_REACTOR, FACTORY_REACTOR, STARPORT_REACTOR])
        new_length = len(needed_events)
        while old_length != new_length:
            old_length = new_length
            for event_index in xrange(len(events)): # continue
                event = events[event_index]
                if event.get_result() in [add,research]:
                    if len([element for element in event.get_args() if element in needed_units]):
                        needed_events.add(event_index)
                        needed_units |= set([req for req,kind in event.get_requirements()])
                elif event.get_result() ==  warp:
                    if event.get_args()[0] in needed_units:
                        needed_events.add(event_index)
                        needed_units |= set([req for req,kind in event.get_requirements()])
                elif event.get_result() == spawn_larva:
                    if LARVA in needed_units and False in event.get_args():
                        # queen larva spawn
                        needed_events.add(event_index)
                        needed_units |= set([req for req,kind in event.get_requirements()])
                if not need_techlab:
                    needed_units -= techlab_units
                if not need_reactor:
                    needed_units -= set([REACTOR, BARRACKS_REACTOR, FACTORY_REACTOR, STARPORT_REACTOR])
            new_length = len(needed_events)
        # now remove unneeded
        if not need_scouts:
            needed_events -= set([SEND_SCV_TO_SCOUT,BRING_BACK_SCV_SCOUT,SEND_PROBE_TO_SCOUT,BRING_BACK_PROBE_SCOUT,SEND_DRONE_TO_SCOUT,BRING_BACK_DRONE_SCOUT])
        if not need_gas:
            needed_events -= set([SWITCH_SCV_TO_MINERALS, BUILD_REFINERY,SWITCH_PROBE_TO_MINERALS,SWITCH_PROBE_TO_GAS,WARP_ASSIMILATOR,SWITCH_DRONE_TO_GAS,SWITCH_DRONE_TO_MINERALS,MORPH_EXTRACTOR])
        contributes[constraints] = {i: (i in needed_events) for i in xrange(len(events))}
        print [key for key in contributes[constraints].iterkeys() if contributes[constraints][key]]

class PriorityQueue:
  """
    Implements a priority queue data structure. Each inserted item
    has a priority associated with it and the client is usually interested
    in quick retrieval of the lowest-priority item in the queue. This
    data structure allows O(1) access to the lowest-priority item.
    
    Note that this PriorityQueue does not allow you to change the priority
    of an item.  However, you may insert the same item multiple times with
    different priorities.

    This code from John DiNero and Dan Klein's util.py 
  """  
  def  __init__(self):  
    self.heap = []
    
  def push(self, item, priority):
      pair = (priority,item)
      heapq.heappush(self.heap,pair)

  def pop(self):
      (priority,item) = heapq.heappop(self.heap)
      #print "Out:", priority, [event_info[0] for event_info in item.events]
      return item
  
  def isEmpty(self):
    return len(self.heap) == 0

def gas_helps(constraints, race):
    for unit, count in constraints:
        # reactor build time 50s, marine 25s
        if unit == MARINE and count > 3:
            return True
        # cycore time 50
        # warp gate time 160
        # zealot time 38 -> 28 with warpgate
        if unit == ZEALOT and count > 5:
            return True
    instance = Instance()
    instance.init_as_race(race)
    can_reach = set([i for i in xrange(NUM_UNITS) if instance.units[i] > 0])
    old_size = 0
    new_size = len(can_reach)
    gasless_events = filter(lambda event: event.cost[1] == 0, events)
    while old_size < new_size:
        old_size = new_size
        for event in gasless_events:
            for req, kind in event.requirements:
                if kind is not NOT and req not in can_reach:
                    break
            else:
                if event.result in [add, warp, research, warp]:
                    can_reach |= set([product for product in event.args])
        new_size = len(can_reach)
    required = set([i for unit, count in constraints])
    return required.issubset(can_reach)
