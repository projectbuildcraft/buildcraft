"""
    Copyright (C) 2013 Project Buildcraft
    License notice in buildcraft.py
"""
from bcevent import add, mule, idle, salvage, research, warp, boost, spawn_larva, Event

O = 1
OCCUPATION = O
A = 2
ASSUMPTION = A
C = 3
CONSUMPTION = C
N = 4
NOT = N

SCV_MINERAL = 0
SCV_GAS = 1
SCV_SCOUT = 2
MARINE = 3
MARAUDER = 4
REAPER = 5
GHOST = 6
HELLION = 7
SIEGE_TANK = 8
THOR = 9
VIKING = 10
MEDIVAC = 11
RAVEN = 12
BANSHEE = 13
BATTLECRUISER = 14
HELLBAT = 15
WIDOW_MINE = 16
COMMAND_CENTER = 17
ORBITAL_COMMAND = 18
PLANETARY_FORTRESS = 19
MULE = 20
SUPPLY_DEPOT = 21
SUPPLY_DEPOT_EXTRA = 22
REFINERY = 23
BARRACKS = 24
ENGINEERING_BAY = 25
BUNKER = 26
MISSILE_TURRET = 27
SENSOR_TOWER = 28
FACTORY = 29
GHOST_ACADEMY = 30
GHOST_ACADEMY_ARMED = 31
ARMORY = 32
STARPORT = 33
FUSION_CORE = 34
TECH_LAB = 35
REACTOR = 36
BARRACKS_REACTOR = 37
BARRACKS_TECH_LAB = 38
FACTORY_REACTOR = 39
FACTORY_TECH_LAB = 40
STARPORT_REACTOR = 41
STARPORT_TECH_LAB = 42
REACTOR_BARRACKS = 43
REACTOR_FACTORY = 44
REACTOR_STARPORT = 45
TECH_LAB_BARRACKS = 46
TECH_LAB_FACTORY = 47
TECH_LAB_STARPORT = 48
INFANTRY_WEAPONS_LEVEL_1 = 49
INFANTRY_WEAPONS_LEVEL_2 = 50
INFANTRY_WEAPONS_LEVEL_3 = 51
VEHICLE_WEAPONS_LEVEL_1 = 52
VEHICLE_WEAPONS_LEVEL_2 = 53
VEHICLE_WEAPONS_LEVEL_3 = 54
SHIP_WEAPONS_LEVEL_1 = 55
SHIP_WEAPONS_LEVEL_2 = 56
SHIP_WEAPONS_LEVEL_3 = 57
INFANTRY_ARMOR_LEVEL_1 = 58
INFANTRY_ARMOR_LEVEL_2 = 59
INFANTRY_ARMOR_LEVEL_3 = 60
VEHICLE_PLATING_LEVEL_1 = 61
VEHICLE_PLATING_LEVEL_2 = 62
VEHICLE_PLATING_LEVEL_3 = 63
SHIP_PLATING_LEVEL_1 = 64
SHIP_PLATING_LEVEL_2 = 65
SHIP_PLATING_LEVEL_3 = 66
NITRO_PACKS = 67
HI_SEC_AUTO_TRACKING = 68
CLOAKING_FIELD = 69
CONCUSSIVE_SHELLS = 70
PERSONAL_CLOAKING = 71
STIMPACK = 72
WEAPON_REFIT = 73
BEHEMOTH_REACTOR = 74
CADUCEUS_REACTOR = 75
CORVID_REACTOR = 76
MOEBIUS_REACTOR = 77
BUILDING_ARMOR = 78
COMBAT_SHIELD = 79
DURABLE_MATERIALS = 80
INFERNAL_PRE_IGNITER = 81
NEOSTEEL_FRAME = 82
TRANSFORMATION_SERVOS = 83
DRILLING_CLAWS = 84
LARVA = 85
DRONE_MINERAL = 86
DRONE_GAS = 87
DRONE_SCOUT = 88
OVERLORD = 89
ZERGLING = 90
QUEEN = 91
HYDRALISK = 92
BANELING = 93
OVERSEER = 94
ROACH = 95
INFESTOR = 96
MUTALISK = 97
CORRUPTOR = 98
NYDUS_WORM = 99
ULTRALISK = 100
BROOD_LORD = 101
SWARM_HOST = 102
VIPER = 103
HATCHERY = 104
EXTRACTOR = 105
SPAWNING_POOL = 106
EVOLUTION_CHAMBER = 107
SPINE_CRAWLER = 108
SPORE_CRAWLER = 109
ROACH_WARREN = 110
BANELING_NEST = 111
LAIR = 112
HYDRALISK_DEN = 113
INFESTATION_PIT = 114
SPIRE = 115
NYDUS_NETWORK = 116
HIVE = 117
ULTRALISK_CAVERN = 118
GREATER_SPIRE = 119
CREEP_TUMOR = 120
CREEP_TUMOR_USED = 121
MELEE_ATTACKS_LEVEL_1 = 122
MELEE_ATTACKS_LEVEL_2 = 123
MELEE_ATTACKS_LEVEL_3 = 124
MISSILE_ATTACKS_LEVEL_1 = 125
MISSILE_ATTACKS_LEVEL_2 = 126
MISSILE_ATTACKS_LEVEL_3 = 127
FLYER_ATTACKS_LEVEL_1 = 128
FLYER_ATTACKS_LEVEL_2 = 129
FLYER_ATTACKS_LEVEL_3 = 130
GROUND_CARAPACE_LEVEL_1 = 131
GROUND_CARAPACE_LEVEL_2 = 132
GROUND_CARAPACE_LEVEL_3 = 133
FLYER_CARAPACE_LEVEL_1 = 134
FLYER_CARAPACE_LEVEL_2 = 135
FLYER_CARAPACE_LEVEL_3 = 136
CHITINOUS_PLATING = 137
CENTRIFUGAL_HOOKS = 138
GLIAL_RECONSTRUCTION = 139
METABOLIC_BOOST = 140
PNEUMATIZED_CARAPACE = 141
GROOVED_SPINES = 142
BURROW = 143
NEURAL_PARASITE = 144
PATHOGEN_GLANDS = 145
ADRENAL_GLANDS = 146
TUNNELING_CLAWS = 147
VENTRAL_SACS = 148
MUSCULAR_AUGMENTS = 149
INCREASED_LOCUST_LIFETIME = 150
PROBE_MINERAL = 151
PROBE_GAS = 152
PROBE_SCOUT = 153
ZEALOT = 154
STALKER = 155
SENTRY = 156
OBSERVER = 157
IMMORTAL = 158
WARP_PRISM = 159
COLOSSUS = 160
PHOENIX = 161
VOID_RAY = 162
HIGH_TEMPLAR = 163
DARK_TEMPLAR = 164
ARCHON = 165
CARRIER = 166
MOTHERSHIP = 167
MOTHERSHIP_CORE = 168
ORACLE = 169
TEMPEST = 170
NEXUS = 171
PYLON = 172
ASSIMILATOR = 173
GATEWAY = 174
FORGE = 175
PHOTON_CANNON = 176
WARPGATE = 177
CYBERNETICS_CORE = 178
TWILIGHT_COUNCIL = 179
ROBOTICS_FACILITY = 180
STARGATE = 181
TEMPLAR_ARCHIVES = 182
DARK_SHRINE = 183
ROBOTICS_BAY = 184
FLEET_BEACON = 185
GROUND_WEAPONS_LEVEL_1 = 186
GROUND_WEAPONS_LEVEL_2 = 187
GROUND_WEAPONS_LEVEL_3 = 188
AIR_WEAPONS_LEVEL_1 = 189
AIR_WEAPONS_LEVEL_2 = 190
AIR_WEAPONS_LEVEL_3 = 191
GROUND_ARMOR_LEVEL_1 = 192
GROUND_ARMOR_LEVEL_2 = 193
GROUND_ARMOR_LEVEL_3 = 194
AIR_ARMOR_LEVEL_1 = 195
AIR_ARMOR_LEVEL_2 = 196
AIR_ARMOR_LEVEL_3 = 197
SHIELDS_LEVEL_1 = 198
SHIELDS_LEVEL_2 = 199
SHIELDS_LEVEL_3 = 200
CHARGE = 201
GRAVITIC_BOOSTERS = 202
GRAVITIC_DRIVE = 203
ANION_PULSE_CRYSTALS = 204
EXTENDED_THERMAL_LANCE = 205
PSIONIC_STORM = 206
HALLUCINATION = 207
BLINK = 208
GRAVITON_CATAPULT = 209
WARP_GATE = 210
NUM_UNITS = 211

BUILD_SCV = 0
SWITCH_SCV_TO_GAS = 1
SWITCH_SCV_TO_MINERALS = 2
SEND_SCV_TO_SCOUT = 3
BRING_BACK_SCV_SCOUT = 4
TRAIN_MARINE = 5
TRAIN_MARAUDER = 6
TRAIN_REAPER = 7
TRAIN_GHOST = 8
BUILD_HELLION = 9
BUILD_SIEGE_TANK = 10
BUILD_THOR = 11
BUILD_VIKING = 12
BUILD_MEDIVAC = 13
BUILD_RAVEN = 14
BUILD_BANSHEE = 15
BUILD_BATTLECRUISER = 16
BUILD_HELLBAT = 17
BUILD_WIDOW_MINE = 18
BUILD_COMMAND_CENTER = 19
UPGRADE_TO_ORBITAL_COMMAND = 20
CALL_DOWN_MULE = 21
SCANNER_SWEEP = 22
UPGRADE_TO_PLANETARY_FORTRESS = 23
BUILD_SUPPLY_DEPOT = 24
UPGRADE_SUPPLY_DEPOT = 25
BUILD_REFINERY = 26
BUILD_BARRACKS = 27
BUILD_ENGINEERING_BAY = 28
BUILD_BUNKER = 29
SALVAGE_BUNKER = 30
BUILD_MISSILE_TURRET = 31
BUILD_SENSOR_TOWER = 32
BUILD_FACTORY = 33
BUILD_GHOST_ACADEMY = 34
ARM_SILO_WITH_NUKE = 35
FIRE_NUKE = 36
BUILD_ARMORY = 37
BUILD_STARPORT = 38
BUILD_FUSION_CORE = 39
BUILD_REACTOR_ONTO_BARRACKS = 40
BUILD_TECH_LAB_ONTO_BARRACKS = 41
BUILD_REACTOR_ONTO_FACTORY = 42
BUILD_TECH_LAB_ONTO_FACTORY = 43
BUILD_REACTOR_ONTO_STARPORT = 44
BUILD_TECH_LAB_ONTO_STARPORT = 45
SEPARATE_REACTOR_FROM_BARRACKS = 46
ATTACH_REACTOR_TO_BARRACKS = 47
SEPARATE_TECH_LAB_FROM_BARRACKS = 48
ATTACH_TECH_LAB_TO_BARRACKS = 49
SEPARATE_REACTOR_FROM_FACTORY = 50
ATTACH_REACTOR_TO_FACTORY = 51
SEPARATE_TECH_LAB_FROM_FACTORY = 52
ATTACH_TECH_LAB_TO_FACTORY = 53
SEPARATE_REACTOR_FROM_STARPORT = 54
ATTACH_REACTOR_TO_STARPORT = 55
SEPARATE_TECH_LAB_FROM_STARPORT = 56
ATTACH_TECH_LAB_TO_STARPORT = 57
RESEARCH_INFANTRY_WEAPONS_LEVEL_1 = 58
RESEARCH_INFANTRY_WEAPONS_LEVEL_2 = 59
RESEARCH_INFANTRY_WEAPONS_LEVEL_3 = 60
RESEARCH_VEHICLE_WEAPONS_LEVEL_1 = 61
RESEARCH_VEHICLE_WEAPONS_LEVEL_2 = 62
RESEARCH_VEHICLE_WEAPONS_LEVEL_3 = 63
RESEARCH_SHIP_WEAPONS_LEVEL_1 = 64
RESEARCH_SHIP_WEAPONS_LEVEL_2 = 65
RESEARCH_SHIP_WEAPONS_LEVEL_3 = 66
RESEARCH_INFANTRY_ARMOR_LEVEL_1 = 67
RESEARCH_INFANTRY_ARMOR_LEVEL_2 = 68
RESEARCH_INFANTRY_ARMOR_LEVEL_3 = 69
RESEARCH_VEHICLE_PLATING_LEVEL_1 = 70
RESEARCH_VEHICLE_PLATING_LEVEL_2 = 71
RESEARCH_VEHICLE_PLATING_LEVEL_3 = 72
RESEARCH_SHIP_PLATING_LEVEL_1 = 73
RESEARCH_SHIP_PLATING_LEVEL_2 = 74
RESEARCH_SHIP_PLATING_LEVEL_3 = 75
RESEARCH_NITRO_PACKS = 76
RESEARCH_HI_SEC_AUTO_TRACKING = 77
RESEARCH_CLOAKING_FIELD = 78
RESEARCH_CONCUSSIVE_SHELLS = 79
RESEARCH_PERSONAL_CLOAKING = 80
RESEARCH_STIMPACK = 81
RESEARCH_WEAPON_REFIT = 82
RESEARCH_BEHEMOTH_REACTOR = 83
RESEARCH_CADUCEUS_REACTOR = 84
RESEARCH_CORVID_REACTOR = 85
RESEARCH_MOEBIUS_REACTOR = 86
RESEARCH_BUILDING_ARMOR = 87
RESEARCH_COMBAT_SHIELD = 88
RESEARCH_DURABLE_MATERIALS = 89
RESEARCH_INFERNAL_PRE_IGNITER = 90
RESEARCH_NEOSTEEL_FRAME = 91
RESEARCH_TRANSFORMATION_SERVOS = 92
RESEARCH_DRILLING_CLAWS = 93
AUTO_SPAWN_LARVA = 94
SPAWN_LARVA = 95
SPAWN_DRONE = 96
SWITCH_DRONE_TO_GAS = 97
SWITCH_DRONE_TO_MINERALS = 98
SEND_DRONE_TO_SCOUT = 99
BRING_BACK_DRONE_SCOUT = 100
SPAWN_OVERLORD = 101
SACRIFICE_OVERLORD = 102
SPAWN_ZERGLING = 103
SPAWN_QUEEN = 104
SPAWN_HYDRALISK = 105
MORPH_BANELING = 106
MORPH_OVERSEER = 107
SPAWN_ROACH = 108
SPAWN_INFESTOR = 109
SPAWN_MUTALISK = 110
SPAWN_CORRUPTOR = 111
SPAWN_NYDUS_WORM = 112
SPAWN_ULTRALISK = 113
MORPH_BROOD_LORD = 114
SPAWN_SWARM_HOST = 115
SPAWN_VIPER = 116
MORPH_HATCHERY = 117
MORPH_EXTRACTOR = 118
MORPH_SPAWNING_POOL = 119
MORPH_EVOLUTION_CHAMBER = 120
MORPH_SPINE_CRAWLER = 121
MORPH_SPORE_CRAWLER = 122
MORPH_ROACH_WARREN = 123
MORPH_BANELING_NEST = 124
MORPH_LAIR = 125
MORPH_HYDRALISK_DEN = 126
MORPH_INFESTATION_PIT = 127
MORPH_SPIRE = 128
MORPH_NYDUS_NETWORK = 129
MORPH_HIVE = 130
MORPH_ULTRALISK_CAVERN = 131
MORPH_GREATER_SPIRE = 132
SPAWN_CREEP_TUMOR = 133
RESPAWN_CREEP_TUMOR = 134
RESEARCH_MELEE_ATTACKS_LEVEL_1 = 135
RESEARCH_MELEE_ATTACKS_LEVEL_2 = 136
RESEARCH_MELEE_ATTACKS_LEVEL_3 = 137
RESEARCH_MISSILE_ATTACKS_LEVEL_1 = 138
RESEARCH_MISSILE_ATTACKS_LEVEL_2 = 139
RESEARCH_MISSILE_ATTACKS_LEVEL_3 = 140
RESEARCH_FLYER_ATTACKS_LEVEL_1 = 141
RESEARCH_FLYER_ATTACKS_LEVEL_2 = 142
RESEARCH_FLYER_ATTACKS_LEVEL_3 = 143
RESEARCH_GROUND_CARAPACE_LEVEL_1 = 144
RESEARCH_GROUND_CARAPACE_LEVEL_2 = 145
RESEARCH_GROUND_CARAPACE_LEVEL_3 = 146
RESEARCH_FLYER_CARAPACE_LEVEL_1 = 147
RESEARCH_FLYER_CARAPACE_LEVEL_2 = 148
RESEARCH_FLYER_CARAPACE_LEVEL_3 = 149
RESEARCH_CHITINOUS_PLATING = 150
RESEARCH_CENTRIFUGAL_HOOKS = 151
RESEARCH_GLIAL_RECONSTRUCTION = 152
RESEARCH_METABOLIC_BOOST = 153
RESEARCH_PNEUMATIZED_CARAPACE = 154
RESEARCH_GROOVED_SPINES = 155
RESEARCH_BURROW = 156
RESEARCH_NEURAL_PARASITE = 157
RESEARCH_PATHOGEN_GLANDS = 158
RESEARCH_ADRENAL_GLANDS = 159
RESEARCH_TUNNELING_CLAWS = 160
RESEARCH_VENTRAL_SACS = 161
RESEARCH_MUSCULAR_AUGMENTS = 162
RESEARCH_INCREASED_LOCUST_LIFETIME = 163
CREATE_PROBE = 164
SWITCH_PROBE_TO_GAS = 165
SWITCH_PROBE_TO_MINERALS = 166
SEND_PROBE_TO_SCOUT = 167
BRING_BACK_PROBE_SCOUT = 168
CREATE_ZEALOT = 169
WARP_IN_ZEALOT = 170
CREATE_STALKER = 171
WARP_IN_STALKER = 172
CREATE_SENTRY = 173
WARP_IN_SENTRY = 174
CREATE_OBSERVER = 175
CREATE_IMMORTAL = 176
CREATE_WARP_PRISM = 177
CREATE_COLOSSUS = 178
CREATE_PHOENIX = 179
CREATE_VOID_RAY = 180
CREATE_HIGH_TEMPLAR = 181
WARP_IN_HIGH_TEMPLAR = 182
CREATE_DARK_TEMPLAR = 183
WARP_IN_DARK_TEMPLAR = 184
FUSE_ARCHON_MIX = 185
FUSE_ARCHON_HIGH = 186
FUSE_ARCHON_DARK = 187
CREATE_CARRIER = 188
CREATE_MOTHERSHIP = 189
CREATE_MOTHERSHIP_CORE = 190
CREATE_ORACLE = 191
CREATE_TEMPEST = 192
WARP_NEXUS = 193
CHRONO_BOOST = 194
WARP_PYLON = 195
WARP_ASSIMILATOR = 196
WARP_GATEWAY = 197
WARP_FORGE = 198
WARP_PHOTON_CANNON = 199
TRANSFORM_INTO_WARPGATE = 200
TRANSFORM_INTO_GATEWAY = 201
WARPGATE_ON_COOLDOWN = 202
WARP_CYBERNETICS_CORE = 203
WARP_TWILIGHT_COUNCIL = 204
WARP_ROBOTICS_FACILITY = 205
WARP_STARGATE = 206
WARP_TEMPLAR_ARCHIVES = 207
WARP_DARK_SHRINE = 208
WARP_ROBOTICS_BAY = 209
WARP_FLEET_BEACON = 210
RESEARCH_GROUND_WEAPONS_LEVEL_1 = 211
RESEARCH_GROUND_WEAPONS_LEVEL_2 = 212
RESEARCH_GROUND_WEAPONS_LEVEL_3 = 213
RESEARCH_AIR_WEAPONS_LEVEL_1 = 214
RESEARCH_AIR_WEAPONS_LEVEL_2 = 215
RESEARCH_AIR_WEAPONS_LEVEL_3 = 216
RESEARCH_GROUND_ARMOR_LEVEL_1 = 217
RESEARCH_GROUND_ARMOR_LEVEL_2 = 218
RESEARCH_GROUND_ARMOR_LEVEL_3 = 219
RESEARCH_AIR_ARMOR_LEVEL_1 = 220
RESEARCH_AIR_ARMOR_LEVEL_2 = 221
RESEARCH_AIR_ARMOR_LEVEL_3 = 222
RESEARCH_SHIELDS_LEVEL_1 = 223
RESEARCH_SHIELDS_LEVEL_2 = 224
RESEARCH_SHIELDS_LEVEL_3 = 225
RESEARCH_CHARGE = 226
RESEARCH_GRAVITIC_BOOSTERS = 227
RESEARCH_GRAVITIC_DRIVE = 228
RESEARCH_ANION_PULSE_CRYSTALS = 229
RESEARCH_EXTENDED_THERMAL_LANCE = 230
RESEARCH_PSIONIC_STORM = 231
RESEARCH_HALLUCINATION = 232
RESEARCH_BLINK = 233
RESEARCH_GRAVITON_CATAPULT = 234
RESEARCH_WARP_GATE = 235

events = [
        (COMMAND_CENTER,O),
        (SCV_MINERAL,C),(REFINERY,A)
        (SCV_GAS,C),
        (SCV_MINERAL,C),
        (SCV_SCOUT,C),
        (BARRACKS,O),
        (BARRACKS_TECH_LAB,O),
        (BARRACKS,O),
        (BARRACKS_TECH_LAB,O),
        (FACTORY,O),
        (FACTORY_TECH_LAB,O),
        (FACTORY_TECH_LAB,O),(ARMORY,A)
        (STARPORT,O),
        (STARPORT,O),
        (STARPORT_TECH_LAB,O),
        (STARPORT_TECH_LAB,O),
        (STARPORT_TECH_LAB,O),(FUSION_CORE,A)
        (FACTORY,O),(ARMORY,)
        (FACTORY,O),
        (SCV_MINERAL,O),
        (COMMAND_CENTER,C),(BARRACKS,A)
        (ORBITAL_COMMAND,50),
        (ORBITAL_COMMAND,50),
        (COMMAND_CENTER,C),(ENGINEERING_BAY,A)
        (SCV_MINERAL,O),
        (SUPPLY_DEPOT,C),(ORBITAL_COMMAND,50)
        (SCV_MINERAL,O),
        (SCV_MINERAL,O),(SUPPLY_DEPOT,A)
        (SCV_MINERAL,O),(SUPPLY_DEPOT,A)
        (SCV_MINERAL,O),(BARRACKS,A)
        (BUNKER,C),
        (SCV_MINERAL,O),(ENGINEERING_BAY,A)
        (SCV_MINERAL,O),(ENGINEERING_BAY,A)
        (SCV_MINERAL,O),(BARRACKS,A)
        (SCV_MINERAL,O),(BARRACKS,A)
        (GHOST_ACADEMY,O),
        (GHOST_ACADEMY_ARMED,C),
        (SCV_MINERAL,O),(FACTORY,A)
        (SCV_MINERAL,O),(FACTORY,A)
        (SCV_MINERAL,O),(STARPORT,A)
        (BARRACKS,C),
        (BARRACKS,C),
        (FACTORY,C),
        (FACTORY,C),
        (STARPORT,C),
        (STARPORT,C),
        (BARRACKS_REACTOR,C),(REACTOR_BARRACKS,C)
        (BARRACKS,C),(REACTOR,C)
        (BARRACKS_TECH_LAB,C),(TECH_LAB_BARRACKS,C)
        (BARRACKS,C),(TECH_LAB,C)
        (FACTORY_REACTOR,C),(REACTOR_FACTORY,C)
        (FACTORY,C),(REACTOR,C)
        (FACTORY_TECH_LAB,C),(TECH_LAB_FACTORY,C)
        (FACTORY,C),(TECH_LAB,C)
        (STARPORT_REACTOR,C),(REACTOR_STARPORT,C)
        (STARPORT,C),(REACTOR,C)
        (STARPORT_TECH_LAB,C),(TECH_LAB_STARPORT,C)
        (STARPORT,C),(TECH_LAB,C)
        (ENGINEERING_BAY,O),(INFANTRY_WEAPONS_LEVEL_1,N)
        (ENGINEERING_BAY,O),(INFANTRY_WEAPONS_LEVEL_2,N),(INFANTRY_WEAPONS_LEVEL_1,A),(ARMORY,A)
        (ENGINEERING_BAY,O),(INFANTRY_WEAPONS_LEVEL_3,N),(INFANTRY_WEAPONS_LEVEL_2,A),(ARMORY,A)
        (ARMORY,O),(VEHICLE_WEAPONS_LEVEL_1,N)
        (ARMORY,O),(VEHICLE_WEAPONS_LEVEL_2,N),(VEHICLE_WEAPONS_LEVEL_1,A)
        (ARMORY,O),(VEHICLE_WEAPONS_LEVEL_3,N),(VEHICLE_WEAPONS_LEVEL_2,A)
        (ARMORY,O),(SHIP_WEAPONS_LEVEL_1,N)
        (ARMORY,O),(SHIP_WEAPONS_LEVEL_2,N),(SHIP_WEAPONS_LEVEL_1,A)
        (ARMORY,O),(SHIP_WEAPONS_LEVEL_3,N),(SHIP_WEAPONS_LEVEL_2,A)
        (ENGINEERING_BAY,O),(INFANTRY_ARMOR_LEVEL_1,N)
        (ENGINEERING_BAY,O),(INFANTRY_ARMOR_LEVEL_2,N),(INFANTRY_ARMOR_LEVEL_1,A),(ARMORY,A)
        (ENGINEERING_BAY,O),(INFANTRY_ARMOR_LEVEL_3,N),(INFANTRY_ARMOR_LEVEL_2,A),(ARMORY,A)
        (ARMORY,O),(VEHICLE_PLATING_LEVEL_1,N)
        (ARMORY,O),(VEHICLE_PLATING_LEVEL_2,N),(VEHICLE_PLATING_LEVEL_1,A)
        (ARMORY,O),(VEHICLE_PLATING_LEVEL_3,N),(VEHICLE_PLATING_LEVEL_2,A)
        (ARMORY,O),(SHIP_PLATING_LEVEL_1,N)
        (ARMORY,O),(SHIP_PLATING_LEVEL_2,N),(SHIP_PLATING_LEVEL_1,A)
        (ARMORY,O),(SHIP_PLATING_LEVEL_3,N),(SHIP_PLATING_LEVEL_2,A)
        (TECH_LAB_BARRACKS,O),(NITRO_PACKS,N),(ARMORY,A)
        (ENGINEERING_BAY,O),(HI_SEC_AUTO_TRACKING,N)
        (TECH_LAB_STARPORT,O),(CLOAKING_FIELD,N)
        (TECH_LAB_BARRACKS,O),(CONCUSSIVE_SHELLS,N)
        (GHOST_ACADEMY,O),(PERSONAL_CLOAKING,N)
        (TECH_LAB_BARRACKS,O),(STIMPACK,N)
        (FUSION_CORE,O),(WEAPON_REFIT,N)
        (FUSION_CORE,O),(BEHEMOTH_REACTOR,N)
        (TECH_LAB_STARPORT,O),(CADUCEUS_REACTOR,N)
        (TECH_LAB_STARPORT,O),(CORVID_REACTOR,N)
        (GHOST_ACADEMY,O),(MOEBIUS_REACTOR,N)
        (ENGINEERING_BAY,O),(BUILDING_ARMOR,N)
        (TECH_LAB_BARRACKS,O),(COMBAT_SHIELD,N)
        (TECH_LAB_STARPORT,O),(DURABLE_MATERIALS,N)
        (TECH_LAB_FACTORY,O),(INFERNAL_PRE_IGNITER,N)
        (ENGINEERING_BAY,O),(NEOSTEEL_FRAME,N)
        (TECH_LAB_FACTORY,O),(TRANSFORMATION_SERVOS,N),(ARMORY,A)
        (TECH_LAB_FACTORY,O),(DRILLING_CLAWS,N),(ARMORY,A)
        (HATCHERY,A),(HATCHERY,N)
        (QUEEN,25),(HATCHERY,A)
        (LARVA,C),
        (DRONE_MINERAL,C),(EXTRACTOR,A)
        (DRONE_GAS,C),
        (DRONE_MINERAL,C),
        (DRONE_SCOUT,C),
        (LARVA,C),
        (OVERLORD,C),
        (LARVA,C),(SPAWNING_POOL,A)
        (HATCHERY,O),(SPAWNING_POOL,A)
        (LARVA,C),(HYDRALISK_DEN,A)
        (LARVA,C),(BANELING_NEST,A)
        (LARVA,C),(LAIR,A)
        (LARVA,C),(ROACH_WARREN,A)
        (LARVA,C),(INFESTATION_PIT,A)
        (LARVA,C),(SPIRE,A)
        (LARVA,C),(SPIRE,A)
        (NYDUS_NETWORK,A),
        (LARVA,C),(ULTRALISK_CAVERN,A)
        (LARVA,C),(GREATER_SPIRE,A)
        (LARVA,C),(INFESTATION_PIT,A)
        (LARVA,C),(SPIRE,A)
        (DRONE_MINERAL,C),
        (DRONE_MINERAL,C),
        (DRONE_MINERAL,C),(HATCHERY,A)
        (DRONE_MINERAL,C),(HATCHERY,A)
        (DRONE_MINERAL,C),(SPAWNING_POOL,A)
        (DRONE_MINERAL,C),(SPAWNING_POOL,A)
        (DRONE_MINERAL,C),(SPAWNING_POOL,A)
        (DRONE_MINERAL,C),(SPAWNING_POOL,A)
        (HATCHERY,C),(SPAWNING_POOL,A)
        (DRONE_MINERAL,C),(LAIR,A)
        (DRONE_MINERAL,C),(LAIR,A)
        (DRONE_MINERAL,C),(LAIR,A)
        (DRONE_MINERAL,C),(LAIR,A)
        (LAIR,C),(INFESTATION_PIT,A)
        (DRONE_MINERAL,C),(HIVE,A)
        (SPIRE,C),(HIVE,A)
        (QUEEN,25),
        (CREEP_TUMOR,O),
        (EVOLUTION_CHAMBER,O),(MELEE_ATTACKS_LEVEL_1,N)
        (EVOLUTION_CHAMBER,O),(MELEE_ATTACKS_LEVEL_2,N),(MELEE_ATTACKS_LEVEL_1,A),(LAIR,A)
        (EVOLUTION_CHAMBER,O),(MELEE_ATTACKS_LEVEL_3,N),(MELEE_ATTACKS_LEVEL_2,A),(HIVE,A)
        (EVOLUTION_CHAMBER,O),(MISSILE_ATTACKS_LEVEL_1,N)
        (EVOLUTION_CHAMBER,O),(MISSILE_ATTACKS_LEVEL_2,N),(MISSILE_ATTACKS_LEVEL_1,A),(LAIR,A)
        (EVOLUTION_CHAMBER,O),(MISSILE_ATTACKS_LEVEL_3,N),(MISSILE_ATTACKS_LEVEL_2,A),(HIVE,A)
        (SPIRE,O),(FLYER_ATTACKS_LEVEL_1,N)
        (SPIRE,O),(FLYER_ATTACKS_LEVEL_2,N),(FLYER_ATTACKS_LEVEL_1,A),(LAIR,A)
        (SPIRE,O),(FLYER_ATTACKS_LEVEL_3,N),(FLYER_ATTACKS_LEVEL_2,A),(HIVE,A)
        (EVOLUTION_CHAMBER,O),(GROUND_CARAPACE_LEVEL_1,N)
        (EVOLUTION_CHAMBER,O),(GROUND_CARAPACE_LEVEL_2,N),(GROUND_CARAPACE_LEVEL_1,A),(LAIR,A)
        (EVOLUTION_CHAMBER,O),(GROUND_CARAPACE_LEVEL_3,N),(GROUND_CARAPACE_LEVEL_2,A),(HIVE,A)
        (SPIRE,O),(FLYER_CARAPACE_LEVEL_1,N)
        (SPIRE,O),(FLYER_CARAPACE_LEVEL_2,N),(FLYER_CARAPACE_LEVEL_1,A),(LAIR,A)
        (SPIRE,O),(FLYER_CARAPACE_LEVEL_3,N),(FLYER_CARAPACE_LEVEL_2,A),(HIVE,A)
        (ULTRALISK_CAVERN,O),(CHITINOUS_PLATING,N)
        (BANELING_NEST,O),(CENTRIFUGAL_HOOKS,N),(LAIR,A)
        (ROACH_WARREN,O),(GLIAL_RECONSTRUCTION,N),(LAIR,A)
        (SPAWNING_POOL,O),(METABOLIC_BOOST,N)
        (HATCHERY,O),(PNEUMATIZED_CARAPACE,N)
        (HYDRALISK_DEN,O),(MUSCULAR_AUGMENTS,N)
        (HYDRALISK_DEN,O),(GROOVED_SPINES,N)
        (HATCHERY,O),(BURROW,N)
        (INFESTATION_PIT,O),(NEURAL_PARASITE,N)
        (INFESTATION_PIT,O),(PATHOGEN_GLANDS,N)
        (SPAWNING_POOL,O),(ADRENAL_GLANDS,N)
        (ROACH_WARREN,O),(TUNNELING_CLAWS,N),(LAIR,A)
        (HATCHERY,O),(VENTRAL_SACS,N),(LAIR,A)
        (HYDRALISK_DEN,O),(MUSCULAR_AUGMENTS,N)
        (INFESTATION_PIT,O),(INCREASED_LOCUST_LIFETIME,N)
        (NEXUS,O),
        (PROBE_MINERAL,C),(ASSIMILATOR,A)
        (PROBE_GAS,C),
        (PROBE_MINERAL,C),
        (PROBE_SCOUT,C),
        (GATEWAY,O),
        (WARPGATE,O),
        (GATEWAY,O),(CYBERNETICS_CORE,A)
        (WARPGATE,O),
        (GATEWAY,O),(CYBERNETICS_CORE,A)
        (WARPGATE,O),
        (ROBOTICS_FACILITY,O),
        (ROBOTICS_FACILITY,O),
        (ROBOTICS_FACILITY,O),
        (ROBOTICS_FACILITY,O),(ROBOTICS_BAY,A)
        (STARGATE,O),
        (STARGATE,O),
        (GATEWAY,O),(TEMPLAR_ARCHIVES,A)
        (WARPGATE,O),(TEMPLAR_ARCHIVES,A)
        (GATEWAY,O),(DARK_SHRINE,A)
        (WARPGATE,O),(DARK_SHRINE,A)
        (HIGH_TEMPLAR,C),(DARK_TEMPLAR,C)
        (HIGH_TEMPLAR,C),(HIGH_TEMPLAR,C)
        (DARK_TEMPLAR,C),(DARK_TEMPLAR,C)
        (STARGATE,O),
        (MOTHERSHIP_CORE,C),(FLEET_BEACON,A),(MOTHERSHIP,N)
        (NEXUS,O),(CYBERNETICS_CORE,A),(MOTHERSHIP,N),(MOTHERSHIP_CORE,N)
        (STARGATE,O),
        (STARGATE,O),
        (PROBE_MINERAL,A),
        (NEXUS,25),
        (PROBE_MINERAL,A),
        (PROBE_MINERAL,A),
        (PROBE_MINERAL,A),(PYLON,A)
        (PROBE_MINERAL,A),(NEXUS,A),(PYLON,A)
        (PROBE_MINERAL,A),(FORGE,A)
        (GATEWAY,C),(WARP_GATE,A)
        (WARPGATE,C),
        (WARPGATE,O),(WARPGATE,N)
        (PROBE_MINERAL,A),(GATEWAY,A)
        (PROBE_MINERAL,A),(CYBERNETICS_CORE,A)
        (PROBE_MINERAL,A),(CYBERNETICS_CORE,A)
        (PROBE_MINERAL,A),(CYBERNETICS_CORE,A)
        (PROBE_MINERAL,A),(TWILIGHT_COUNCIL,A)
        (PROBE_MINERAL,A),(TEMPLAR_ARCHIVES,A)
        (PROBE_MINERAL,A),(ROBOTICS_FACILITY,A)
        (PROBE_MINERAL,A),(STARGATE,A)
        (FORGE,O),(GROUND_WEAPONS_LEVEL_1,N)
        (FORGE,O),(GROUND_WEAPONS_LEVEL_2,N),(GROUND_WEAPONS_LEVEL_1,A)
        (FORGE,O),(GROUND_WEAPONS_LEVEL_3,N),(GROUND_WEAPONS_LEVEL_2,A)
        (CYBERNETICS_CORE,O),(AIR_WEAPONS_LEVEL_1,N)
        (CYBERNETICS_CORE,O),(AIR_WEAPONS_LEVEL_2,N),(AIR_WEAPONS_LEVEL_1,A)
        (CYBERNETICS_CORE,O),(AIR_WEAPONS_LEVEL_3,N),(AIR_WEAPONS_LEVEL_2,A)
        (FORGE,O),(GROUND_ARMOR_LEVEL_1,N)
        (FORGE,O),(GROUND_ARMOR_LEVEL_2,N),(GROUND_ARMOR_LEVEL_1,A)
        (FORGE,O),(GROUND_ARMOR_LEVEL_3,N),(GROUND_ARMOR_LEVEL_2,A)
        (CYBERNETICS_CORE,O),(AIR_ARMOR_LEVEL_1,N)
        (CYBERNETICS_CORE,O),(AIR_ARMOR_LEVEL_2,N),(AIR_ARMOR_LEVEL_1,A)
        (CYBERNETICS_CORE,O),(AIR_ARMOR_LEVEL_3,N),(AIR_ARMOR_LEVEL_2,A)
        (FORGE,O),(SHIELDS_LEVEL_1,N)
        (FORGE,O),(SHIELDS_LEVEL_2,N),(SHIELDS_LEVEL_1,A)
        (FORGE,O),(SHIELDS_LEVEL_3,N),(SHIELDS_LEVEL_2,A)
        (TWILIGHT_COUNCIL,O),(CHARGE,N)
        (ROBOTICS_BAY,O),(GRAVITIC_BOOSTERS,N)
        (ROBOTICS_BAY,O),(GRAVITIC_DRIVE,N)
        (FLEET_BEACON,O),(ANION_PULSE_CRYSTALS,N)
        (ROBOTICS_BAY,O),(EXTENDED_THERMAL_LANCE,N)
        (TEMPLAR_ARCHIVES,O),(PSIONIC_STORM,N)
        (CYBERNETICS_CORE,O),(HALLUCINATION,N)
        (TWILIGHT_COUNCIL,O),(BLINK,N)
        (FLEET_BEACON,O),(GRAVITON_CATAPULT,N)
        (CYBERNETICS_CORE,O),(WARP_GATE,N)
        (COMMAND_CENTER,A),(COMMAND_CENTER,N)
        (COMMAND_CENTER,A),(COMMAND_CENTER,N)
        (COMMAND_CENTER,A),(COMMAND_CENTER,N)
        (COMMAND_CENTER,A),(COMMAND_CENTER,N)
]

energy = {
	GHOST : (50,200,MOEBIUS_REACTOR),
	MEDIVAC : (50,200,CADUCEUS_REACTOR),
	RAVEN : (50,200,CORVID_REACTOR),
	BANSHEE : (50,200,None),
	BATTLECRUISER : (50,200,BEHEMOTH_REACTOR),
	ORBITAL_COMMAND : (50,200,None),
	QUEEN : (25,200,None),
	OVERSEER : (50,200,None),
	INFESTOR : (50,200,PATHOGEN_GLANDS),
	VIPER : (50,200,None),
	SENTRY : (50,200,None),
	PHOENIX : (50,200,None),
	HIGH_TEMPLAR : (50,200,None),
	MOTHERSHIP : (50,200,None),
	MOTHERSHIP_CORE : (50,200,None),
	ORACLE : (50,200,None),
	NEXUS : (0,100,None),

}
