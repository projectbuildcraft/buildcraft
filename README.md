buildcraft
==========

A build order calculator for Starcraft II: Heart of the Swarm

Goal Features:
Build order calculator accurate to 5 seconds for the first ten minutes of the game
Load, save, compare build orders
Support team build orders for an effectively unbounded number of players
Searchable build orders
Build Order generation: being able to find the earliest possible time to have a given array of units and printing that build order.

Potential issues with the current design:

- We need a way to find out what we have at any given point.
- We need to find a way to figure out if a unit or building is occupied. This might be handled in requirements, but such requirements aren't consumed

Development Schedule:

0.0 Event

- The Event data structure exists. Its instances are enumerated with their names.
- A main method loops through the events and can name them all.

0.1 Requirements

- The Requirements data structure exists. Every enumerated Event object has defined requirements.
- A main method loops through the events and their requirements, listing them out.

0.2 BuildOrder

- The BuildOrder data structure exists. It can save and load all of the known build orders into the same file, using minimal time and space.
- A main method prompts the user to modify and view defined builds.

0.3 Legality

- A main method restricts events appended to a build order to requirements that can be accomplished.

0.4 Calculation

- The main method additionally calculates the times at which each event occurs.

1.0 GUI

- All of the above functionality is in place in a GUI.

1.1 Aesthetics

- The GUI is aesthetically pleasing.

