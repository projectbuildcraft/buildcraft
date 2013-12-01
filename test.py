#!/usr/bin/env python
#
#
#
from constants import *
from optimization import genetic_optimization, a_star_optimization
order = a_star_optimization("T",[(SCV_MINERAL,13)])
order.print_out()
