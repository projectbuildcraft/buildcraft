buildcraft
==========

A build order calculator and optimizer for Starcraft II: Heart of the Swarm (HOTS). The current release is 0.5.3-4 and is available for Windows and Linux from http://projectbuildcraft.github.io/buildcraft/ 

An OS X release isn't expected soon, but a Mac with python and Tkinter installed should be able to run it from source.

Goal Features:
----------------

- Build order calculator accurate to 5 seconds for the first ten minutes of the game

- Load, save, compare build orders

- Support team build orders for an effectively unbounded number of players

- Searchable build orders

- Build order generation: being able to find the earliest possible time to have a given array of units and printing that build order.

- Battle calculation: being able to guess who would win in a fight and when

Potential issues with the current design should be added to List of Oddities

Development Schedule:
--------------

0.5 Beta - 

- Build order calculation is valuable for planning the first ten minutes of the
game

1.0  - May 2014

- The GUI is aesthetically pleasing, user-friendly, and supports team build
orders

2.0 Optimization - July 2014

- The program calculates the build order with the earliest time at which an
array of units can be produced
