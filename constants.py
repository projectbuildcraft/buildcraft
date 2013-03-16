from bcevent import add, mule, idle, salvage, research, warp, chrono, Event

O = 1
A = 2
C = 3
N = 4

SCV_MINERAL = 1
SCV_GAS = 2
SCV_SCOUT = 3
MARINE = 4
MARAUDER = 5
REAPER = 6
GHOST = 7
HELLION = 8
SIEGE_TANK = 9
THOR = 10
VIKING = 11
MEDIVAC = 12
RAVEN = 13
BANSHEE = 14
BATTLECRUISER = 15
HELLBAT = 16
WIDOW_MINE = 17
COMMAND_CENTER = 18
ORBITAL_COMMAND = 19
PLANETARY_FORTRESS = 20
SUPPLY_DEPOT = 21
REFINERY = 22
BARRACKS = 23
ENGINEERING_BAY = 24
BUNKER = 25
MISSILE_TURRET = 26
SENSOR_TOWER = 27
FACTORY = 28
GHOST_ACADEMY = 29
GHOST_ACADEMY_ARMED = 30
ARMORY = 31
STARPORT = 32
FUSION_CORE = 33
TECH_LAB = 34
REACTOR = 35
BARRACKS_REACTOR = 36
BARRACKS_TECH_LAB = 37
FACTORY_REACTOR = 38
FACTORY_TECH_LAB = 39
STARPORT_REACTOR = 40
STARPORT_TECH_LAB = 41
REACTOR_BARRACKS = 42
REACTOR_FACTORY = 43
REACTOR_STARPORT = 44
TECH_LAB_BARRACKS = 45
TECH_LAB_FACTORY = 46
TECH_LAB_STARPORT = 47
INFANTRY_WEAPONS_LEVEL_1 = 48
INFANTRY_WEAPONS_LEVEL_2 = 49
INFANTRY_WEAPONS_LEVEL_3 = 50
VEHICLE_WEAPONS_LEVEL_1 = 51
VEHICLE_WEAPONS_LEVEL_2 = 52
VEHICLE_WEAPONS_LEVEL_3 = 53
SHIP_WEAPONS_LEVEL_1 = 54
SHIP_WEAPONS_LEVEL_2 = 55
SHIP_WEAPONS_LEVEL_3 = 56
INFANTRY_ARMOR_LEVEL_1 = 57
INFANTRY_ARMOR_LEVEL_2 = 58
INFANTRY_ARMOR_LEVEL_3 = 59
VEHICLE_PLATING_LEVEL_1 = 60
VEHICLE_PLATING_LEVEL_2 = 61
VEHICLE_PLATING_LEVEL_3 = 62
SHIP_PLATING_LEVEL_1 = 63
SHIP_PLATING_LEVEL_2 = 64
SHIP_PLATING_LEVEL_3 = 65
NITRO_PACKS = 66
HI_SEC_AUTO_TRACKING = 67
CLOAKING_FIELD = 68
CONCUSSIVE_SHELLS = 69
PERSONAL_CLOAKING = 70
STIMPACK = 71
WEAPON_REFIT = 72
BEHEMOTH_REACTOR = 73
CADUCEUS_REACTOR = 74
CORVID_REACTOR = 75
MOEBIUS_REACTOR = 76
BUILDING_ARMOR = 77
COMBAT_SHIELD = 78
DURABLE_MATERIALS = 79
INFERNAL_PRE_IGNITER = 80
NEOSTEEL_FRAME = 81
TRANSFORMATION_SERVOS = 82
DRILLING_CLAWS = 83
LARVA = 84
DRONE_MINERAL = 85
DRONE_GAS = 86
DRONE_SCOUT = 87
OVERLORD = 88
ZERGLING = 89
QUEEN = 90
HYDRALISK = 91
BANELING = 92
OVERSEER = 93
ROACH = 94
INFESTOR = 95
MUTALISK = 96
CORRUPTOR = 97
NYDUS_WORM = 98
ULTRALISK = 99
BROOD_LORD = 100
SWARM_HOST = 101
VIPER = 102
HATCHERY = 103
EXTRACTOR = 104
SPAWNING_POOL = 105
EVOLUTION_CHAMBER = 106
SPINE_CRAWLER = 107
SPORE_CRAWLER = 108
ROACH_WARREN = 109
BANELING_NEST = 110
LAIR = 111
HYDRALISK_DEN = 112
INFESTATION_PIT = 113
SPIRE = 114
NYDUS_NETWORK = 115
HIVE = 116
ULTRALISK_CAVERN = 117
GREATER_SPIRE = 118
CREEP_TUMOR = 119
CREEP_TUMOR_USED = 120
MELEE_ATTACKS_LEVEL_1 = 121
MELEE_ATTACKS_LEVEL_2 = 122
MELEE_ATTACKS_LEVEL_3 = 123
MISSILE_ATTACKS_LEVEL_1 = 124
MISSILE_ATTACKS_LEVEL_2 = 125
MISSILE_ATTACKS_LEVEL_3 = 126
FLYER_ATTACKS_LEVEL_1 = 127
FLYER_ATTACKS_LEVEL_2 = 128
FLYER_ATTACKS_LEVEL_3 = 129
GROUND_CARAPACE_LEVEL_1 = 130
GROUND_CARAPACE_LEVEL_2 = 131
GROUND_CARAPACE_LEVEL_3 = 132
FLYER_CARAPACE_LEVEL_1 = 133
FLYER_CARAPACE_LEVEL_2 = 134
FLYER_CARAPACE_LEVEL_3 = 135
CHITINOUS_PLATING = 136
CENTRIFUGAL_HOOKS = 137
GLIAL_RECONSTRUCTION = 138
METABOLIC_BOOST = 139
PNEUMATIZED_CARAPACE = 140
GROOVED_SPINES = 141
BURROW = 142
NEURAL_PARASITE = 143
PATHOGEN_GLANDS = 144
ADRENAL_GLANDS = 145
TUNNELING_CLAWS = 146
VENTRAL_SACS = 147
MUSCULAR_AUGMENTS = 148
INCREASED_LOCUST_LIFETIME = 149
PROBE_MINERAL = 150
PROBE_GAS = 151
PROBE_SCOUT = 152
ZEALOT = 153
STALKER = 154
SENTRY = 155
OBSERVER = 156
IMMORTAL = 157
WARP_PRISM = 158
COLOSSUS = 159
PHOENIX = 160
VOID_RAY = 161
HIGH_TEMPLAR = 162
DARK_TEMPLAR = 163
ARCHON = 164
CARRIER = 165
MOTHERSHIP = 166
MOTHERSHIP_CORE = 167
ORACLE = 168
TEMPEST = 169
NEXUS = 170
PYLON = 171
ASSIMILATOR = 172
GATEWAY = 173
FORGE = 174
PHOTON_CANNON = 175
WARPGATE = 176
CYBERNETICS_CORE = 177
TWILIGHT_COUNCIL = 178
ROBOTICS_FACILITY = 179
STARGATE = 180
TEMPLAR_ARCHIVES = 181
DARK_SHRINE = 182
ROBOTICS_BAY = 183
FLEET_BEACON = 184
GROUND_WEAPONS_LEVEL_1 = 185
GROUND_WEAPONS_LEVEL_2 = 186
GROUND_WEAPONS_LEVEL_3 = 187
AIR_WEAPONS_LEVEL_1 = 188
AIR_WEAPONS_LEVEL_2 = 189
AIR_WEAPONS_LEVEL_3 = 190
GROUND_ARMOR_LEVEL_1 = 191
GROUND_ARMOR_LEVEL_2 = 192
GROUND_ARMOR_LEVEL_3 = 193
AIR_ARMOR_LEVEL_1 = 194
AIR_ARMOR_LEVEL_2 = 195
AIR_ARMOR_LEVEL_3 = 196
SHIELDS_LEVEL_1 = 197
SHIELDS_LEVEL_2 = 198
SHIELDS_LEVEL_3 = 199
CHARGE = 200
GRAVITIC_BOOSTERS = 201
GRAVITIC_DRIVE = 202
ANION_PULSE_CRYSTALS = 203
EXTENDED_THERMAL_LANCE = 204
PSIONIC_STORM = 205
HALLUCINATION = 206
BLINK = 207
GRAVITON_CATAPULT = 208
WARP_GATE = 209

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
BUILD_REACTOR_ONTO_BARRACKS = 42
BUILD_TECH_LAB_ONTO_BARRACKS = 43
BUILD_REACTOR_ONTO_FACTORY = 44
BUILD_TECH_LAB_ONTO_FACTORY = 45
BUILD_REACTOR_ONTO_STARPORT = 46
BUILD_TECH_LAB_ONTO_STARPORT = 47
SEPARATE_REACTOR_FROM_BARRACKS = 48
ATTACH_REACTOR_TO_BARRACKS = 49
SEPARATE_TECH_LAB_FROM_BARRACKS = 50
ATTACH_TECH_LAB_TO_BARRACKS = 51
SEPARATE_REACTOR_FROM_FACTORY = 52
ATTACH_REACTOR_TO_FACTORY = 53
SEPARATE_TECH_LAB_FROM_FACTORY = 54
ATTACH_TECH_LAB_TO_FACTORY = 55
SEPARATE_REACTOR_FROM_STARPORT = 56
ATTACH_REACTOR_TO_STARPORT = 57
SEPARATE_TECH_LAB_FROM_STARPORT = 58
ATTACH_TECH_LAB_TO_STARPORT = 59
RESEARCH_INFANTRY_WEAPONS_LEVEL_1 = 60
RESEARCH_INFANTRY_WEAPONS_LEVEL_2 = 61
RESEARCH_INFANTRY_WEAPONS_LEVEL_3 = 62
RESEARCH_VEHICLE_WEAPONS_LEVEL_1 = 63
RESEARCH_VEHICLE_WEAPONS_LEVEL_2 = 64
RESEARCH_VEHICLE_WEAPONS_LEVEL_3 = 65
RESEARCH_SHIP_WEAPONS_LEVEL_1 = 66
RESEARCH_SHIP_WEAPONS_LEVEL_2 = 67
RESEARCH_SHIP_WEAPONS_LEVEL_3 = 68
RESEARCH_INFANTRY_ARMOR_LEVEL_1 = 69
RESEARCH_INFANTRY_ARMOR_LEVEL_2 = 70
RESEARCH_INFANTRY_ARMOR_LEVEL_3 = 71
RESEARCH_VEHICLE_PLATING_LEVEL_1 = 72
RESEARCH_VEHICLE_PLATING_LEVEL_2 = 73
RESEARCH_VEHICLE_PLATING_LEVEL_3 = 74
RESEARCH_SHIP_PLATING_LEVEL_1 = 75
RESEARCH_SHIP_PLATING_LEVEL_2 = 76
RESEARCH_SHIP_PLATING_LEVEL_3 = 77
RESEARCH_NITRO_PACKS = 78
RESEARCH_HI_SEC_AUTO_TRACKING = 79
RESEARCH_CLOAKING_FIELD = 80
RESEARCH_CONCUSSIVE_SHELLS = 81
RESEARCH_PERSONAL_CLOAKING = 82
RESEARCH_STIMPACK = 83
RESEARCH_WEAPON_REFIT = 84
RESEARCH_BEHEMOTH_REACTOR = 85
RESEARCH_CADUCEUS_REACTOR = 86
RESEARCH_CORVID_REACTOR = 87
RESEARCH_MOEBIUS_REACTOR = 88
RESEARCH_BUILDING_ARMOR = 89
RESEARCH_COMBAT_SHIELD = 90
RESEARCH_DURABLE_MATERIALS = 91
RESEARCH_INFERNAL_PRE_IGNITER = 92
RESEARCH_NEOSTEEL_FRAME = 93
RESEARCH_TRANSFORMATION_SERVOS = 94
RESEARCH_DRILLING_CLAWS = 95
AUTO_SPAWN_LARVA = 96
SPAWN_LARVA = 97
SPAWN_DRONE = 98
SWITCH_DRONE_TO_GAS = 99
SWITCH_DRONE_TO_MINERALS = 100
SEND_DRONE_TO_SCOUT = 101
BRING_BACK_DRONE_SCOUT = 102
SPAWN_OVERLORD = 103
SACRIFICE_OVERLORD = 104
SPAWN_ZERGLING = 105
SPAWN_QUEEN = 106
SPAWN_HYDRALISK = 107
MORPH_BANELING = 108
MORPH_OVERSEER = 109
SPAWN_ROACH = 110
SPAWN_INFESTOR = 111
SPAWN_MUTALISK = 112
SPAWN_CORRUPTOR = 113
SPAWN_NYDUS_WORM = 114
SPAWN_ULTRALISK = 115
MORPH_BROOD_LORD = 116
SPAWN_SWARM_HOST = 117
SPAWN_VIPER = 118
MORPH_HATCHERY = 119
MORPH_EXTRACTOR = 120
MORPH_SPAWNING_POOL = 121
MORPH_EVOLUTION_CHAMBER = 122
MORPH_SPINE_CRAWLER = 123
MORPH_SPORE_CRAWLER = 124
MORPH_ROACH_WARREN = 125
MORPH_BANELING_NEST = 126
MORPH_LAIR = 127
MORPH_HYDRALISK_DEN = 128
MORPH_INFESTATION_PIT = 129
MORPH_SPIRE = 130
MORPH_NYDUS_NETWORK = 131
MORPH_HIVE = 132
MORPH_ULTRALISK_CAVERN = 133
MORPH_GREATER_SPIRE = 134
SPAWN_CREEP_TUMOR = 135
RESPAWN_CREEP_TUMOR = 136
RESEARCH_MELEE_ATTACKS_LEVEL_1 = 137
RESEARCH_MELEE_ATTACKS_LEVEL_2 = 138
RESEARCH_MELEE_ATTACKS_LEVEL_3 = 139
RESEARCH_MISSILE_ATTACKS_LEVEL_1 = 140
RESEARCH_MISSILE_ATTACKS_LEVEL_2 = 141
RESEARCH_MISSILE_ATTACKS_LEVEL_3 = 142
RESEARCH_FLYER_ATTACKS_LEVEL_1 = 143
RESEARCH_FLYER_ATTACKS_LEVEL_2 = 144
RESEARCH_FLYER_ATTACKS_LEVEL_3 = 145
RESEARCH_GROUND_CARAPACE_LEVEL_1 = 146
RESEARCH_GROUND_CARAPACE_LEVEL_2 = 147
RESEARCH_GROUND_CARAPACE_LEVEL_3 = 148
RESEARCH_FLYER_CARAPACE_LEVEL_1 = 149
RESEARCH_FLYER_CARAPACE_LEVEL_2 = 150
RESEARCH_FLYER_CARAPACE_LEVEL_3 = 151
RESEARCH_CHITINOUS_PLATING = 152
RESEARCH_CENTRIFUGAL_HOOKS = 153
RESEARCH_GLIAL_RECONSTRUCTION = 154
RESEARCH_METABOLIC_BOOST = 155
RESEARCH_PNEUMATIZED_CARAPACE = 156
RESEARCH_GROOVED_SPINES = 157
RESEARCH_BURROW = 158
RESEARCH_NEURAL_PARASITE = 159
RESEARCH_PATHOGEN_GLANDS = 160
RESEARCH_ADRENAL_GLANDS = 161
RESEARCH_TUNNELING_CLAWS = 162
RESEARCH_VENTRAL_SACS = 163
RESEARCH_MUSCULAR_AUGMENTS = 164
RESEARCH_INCREASED_LOCUST_LIFETIME = 165
CREATE_PROBE = 166
SWITCH_PROBE_TO_GAS = 167
SWITCH_PROBE_TO_MINERALS = 168
SEND_PROBE_TO_SCOUT = 169
BRING_BACK_PROBE_SCOUT = 170
CREATE_ZEALOT = 171
WARP_IN_ZEALOT = 172
CREATE_STALKER = 173
WARP_IN_STALKER = 174
CREATE_SENTRY = 175
WARP_IN_SENTRY = 176
CREATE_OBSERVER = 177
CREATE_IMMORTAL = 178
CREATE_WARP_PRISM = 179
CREATE_COLOSSUS = 180
CREATE_PHOENIX = 181
CREATE_VOID_RAY = 182
CREATE_HIGH_TEMPLAR = 183
WARP_IN_HIGH_TEMPLAR = 184
CREATE_DARK_TEMPLAR = 185
WARP_IN_DARK_TEMPLAR = 186
FUSE_ARCHON_MIX = 187
FUSE_ARCHON_HIGH = 188
FUSE_ARCHON_DARK = 189
CREATE_CARRIER = 190
CREATE_MOTHERSHIP = 191
CREATE_MOTHERSHIP_CORE = 192
CREATE_ORACLE = 193
CREATE_TEMPEST = 194
WARP_NEXUS = 195
CHRONO_BOOST = 196
WARP_PYLON = 197
WARP_ASSIMILATOR = 198
WARP_GATEWAY = 199
WARP_FORGE = 200
WARP_PHOTON_CANNON = 201
TRANSFORM_INTO_WARPGATE = 202
TRANSFORM_INTO_GATEWAY = 203
WARP_CYBERNETICS_CORE = 204
WARP_TWILIGHT_COUNCIL = 205
WARP_ROBOTICS_FACILITY = 206
WARP_STARGATE = 207
WARP_TEMPLAR_ARCHIVES = 208
WARP_DARK_SHRINE = 209
WARP_ROBOTICS_BAY = 210
WARP_FLEET_BEACON = 211
RESEARCH_GROUND_WEAPONS_LEVEL_1 = 212
RESEARCH_GROUND_WEAPONS_LEVEL_2 = 213
RESEARCH_GROUND_WEAPONS_LEVEL_3 = 214
RESEARCH_AIR_WEAPONS_LEVEL_1 = 215
RESEARCH_AIR_WEAPONS_LEVEL_2 = 216
RESEARCH_AIR_WEAPONS_LEVEL_3 = 217
RESEARCH_GROUND_ARMOR_LEVEL_1 = 218
RESEARCH_GROUND_ARMOR_LEVEL_2 = 219
RESEARCH_GROUND_ARMOR_LEVEL_3 = 220
RESEARCH_AIR_ARMOR_LEVEL_1 = 221
RESEARCH_AIR_ARMOR_LEVEL_2 = 222
RESEARCH_AIR_ARMOR_LEVEL_3 = 223
RESEARCH_SHIELDS_LEVEL_1 = 224
RESEARCH_SHIELDS_LEVEL_2 = 225
RESEARCH_SHIELDS_LEVEL_3 = 226
RESEARCH_CHARGE = 227
RESEARCH_GRAVITIC_BOOSTERS = 228
RESEARCH_GRAVITIC_DRIVE = 229
RESEARCH_ANION_PULSE_CRYSTALS = 230
RESEARCH_EXTENDED_THERMAL_LANCE = 231
RESEARCH_PSIONIC_STORM = 232
RESEARCH_HALLUCINATION = 233
RESEARCH_BLINK = 234
RESEARCH_GRAVITON_CATAPULT = 235
RESEARCH_WARP_GATE = 236

events = [
	Event('Build SCV',50,0,1,0,17,add,(SCV_MINERAL,),((COMMAND_CENTER,O),)),
	Event('Switch SCV to Gas',0,0,0,0,0,add,(SCV_GAS,),((SCV_MINERAL,C),(REFINERY,A))),
	Event('Switch SCV to Minerals',0,0,0,0,0,add,(SCV_MINERAL,),((SCV_GAS,C),)),
	Event('Send SCV to Scout',0,0,0,0,0,add,(SCV_SCOUT,),((SCV_MINERAL,C),)),
	Event('Bring back SCV Scout',0,0,0,0,0,add,(SCV_MINERAL,),((SCV_SCOUT,C),)),
	Event('Train Marine',50,0,1,0,25,add,(MARINE,),((BARRACKS,O),)),
	Event('Train Marauder',100,25,2,0,30,add,(MARAUDER,),((BARRACKS_TECH_LAB,O),)),
	Event('Train Reaper',50,50,1,0,45,add,(REAPER,),((BARRACKS,O),)),
	Event('Train Ghost',200,100,2,0,40,add,(GHOST,),((BARRACKS_TECH_LAB,O),)),
	Event('Build Hellion',100,0,2,0,30,add,(HELLION,),((FACTORY,O),)),
	Event('Build Siege Tank',150,125,3,0,45,add,(SIEGE_TANK,),((FACTORY_TECH_LAB,O),)),
	Event('Build Thor',300,200,6,0,60,add,(THOR,),((FACTORY_TECH_LAB,O),(ARMORY,A))),
	Event('Build Viking',150,75,2,0,42,add,(VIKING,),((STARPORT,O),)),
	Event('Build Medivac',100,100,2,0,42,add,(MEDIVAC,),((STARPORT,O),)),
	Event('Build Raven',100,200,2,0,60,add,(RAVEN,),((STARPORT_TECH_LAB,O),)),
	Event('Build Banshee',150,100,3,0,60,add,(BANSHEE,),((STARPORT_TECH_LAB,O),)),
	Event('Build Battlecruiser',400,300,6,0,90,add,(BATTLECRUISER,),((STARPORT_TECH_LAB,O),(FUSION_CORE,A))),
	Event('Build Hellbat',100,0,2,0,30,add,(HELLBAT,),((FACTORY,O),(ARMORY,))),
	Event('Build Widow Mine',75,25,2,0,40,add,(WIDOW_MINE,),((FACTORY,O),)),
	Event('Build Command Center',400,0,0,0,100,add,(COMMAND_CENTER,),((SCV_MINERAL,O),)),
	Event('Upgrade to Orbital Command',150,0,0,11,35,add,(ORBITAL_COMMAND,),((COMMAND_CENTER,C),(BARRACKS,A))),
	Event('Call Down Mule',0,0,0,0,0,mule,(None,),((ORBITAL_COMMAND,50),)),
	Event('Scanner Sweep',0,0,0,0,0,idle,(None,),((ORBITAL_COMMAND,50),)),
	Event('Upgrade to Planetary Fortress',150,150,0,0,50,add,(PLANETARY_FORTRESS,),((COMMAND_CENTER,C),(ENGINEERING_BAY,A))),
	Event('Build Supply Depot',100,0,0,8,30,add,(SUPPLY_DEPOT,),((SCV_MINERAL,O),)),
	Event('Upgrade Supply Depot',0,0,0,8,4,add,(SUPPLY_DEPOT_EXTRA,),((SUPPLY_DEPOT,C),(ORBITAL_COMMAND,50))),
	Event('Build Refinery',75,0,0,0,30,add,(REFINERY,),((SCV_MINERAL,O),)),
	Event('Build Barracks',150,0,0,0,65,add,(BARRACKS,),((SCV_MINERAL,O),(SUPPLY_DEPOT,A))),
	Event('Build Engineering Bay',125,0,0,0,35,add,(ENGINEERING_BAY,),((SCV_MINERAL,O),(SUPPLY_DEPOT,A))),
	Event('Build Bunker',100,0,0,0,40,add,(BUNKER,),((SCV_MINERAL,O),(BARRACKS,A))),
	Event('Salvage Bunker',0,0,0,0,0,salvage,(75,),((BUNKER,C),)),
	Event('Build Missile Turret',100,0,0,0,25,add,(MISSILE_TURRET,),((SCV_MINERAL,O),(ENGINEERING_BAY,A))),
	Event('Build Sensor Tower',125,100,0,0,25,add,(SENSOR_TOWER,),((SCV_MINERAL,O),(ENGINEERING_BAY,A))),
	Event('Build Factory',150,100,0,0,60,add,(FACTORY,),((SCV_MINERAL,O),(BARRACKS,A))),
	Event('Build Ghost Academy',150,50,0,0,40,add,(GHOST_ACADEMY,),((SCV_MINERAL,O),(BARRACKS,A))),
	Event('Arm Silo with Nuke',100,100,0,0,60,add,(GHOST_ACADEMY_ARMED,),((GHOST_ACADEMY,O),)),
	Event('Fire Nuke',0,0,0,0,0,add,(GHOST_ACADEMY,),((GHOST_ACADEMY_ARMED,C),)),
	Event('Build Armory',150,100,0,0,65,add,(ARMORY,),((SCV_MINERAL,O),(FACTORY,A))),
	Event('Build Starport',150,100,0,0,50,add,(STARPORT,),((SCV_MINERAL,O),(FACTORY,A))),
	Event('Build Fusion Core',150,150,0,0,65,add,(FUSION_CORE,),((SCV_MINERAL,O),(STARPORT,A))),
	Event('Build Reactor onto Barracks',50,50,0,0,25,add,(BARRACKS_REACTOR,),((BARRACKS,C),)),
	Event('Build Tech Lab onto Barracks',50,25,0,0,25,add,(BARRACKS_TECH_LAB,),((BARRACKS,C),)),
	Event('Build Reactor onto Factory',50,50,0,0,25,add,(FACTORY_REACTOR,),((FACTORY,C),)),
	Event('Build Tech Lab onto Factory',50,25,0,0,25,add,(FACTORY_TECH_LAB,),((FACTORY,C),)),
	Event('Build Reactor onto Starport',50,50,0,0,25,add,(STARPORT_REACTOR,),((STARPORT,C),)),
	Event('Build Tech Lab onto Starport',50,25,0,0,25,add,(STARPORT_TECH_LAB,),((STARPORT,C),)),
	Event('Separate Reactor from Barracks',0,0,0,0,2,add,(BARRACKS,REACTOR,),((BARRACKS_REACTOR,C),(REACTOR_BARRACKS,C))),
	Event('Attach Reactor to Barracks',0,0,0,0,2,add,(BARRACKS_REACTOR,REACTOR_BARRACKS,),((BARRACKS,C),(REACTOR,C))),
	Event('Separate Tech Lab from Barracks',0,0,0,0,2,add,(BARRACKS,TECH_LAB,),((BARRACKS_TECH_LAB,C),(TECH_LAB_BARRACKS,C))),
	Event('Attach Tech Lab to Barracks',0,0,0,0,2,add,(BARRACKS_TECH_LAB,TECH_LAB_BARRACKS,),((BARRACKS,C),(TECH_LAB,C))),
	Event('Separate Reactor from Factory',0,0,0,0,2,add,(FACTORY,REACTOR,),((FACTORY_REACTOR,C),(REACTOR_FACTORY,C))),
	Event('Attach Reactor to Factory',0,0,0,0,2,add,(FACTORY_REACTOR,REACTOR_FACTORY,),((FACTORY,C),(REACTOR,C))),
	Event('Separate Tech Lab from Factory',0,0,0,0,2,add,(FACTORY,TECH_LAB,),((FACTORY_TECH_LAB,C),(TECH_LAB_FACTORY,C))),
	Event('Attach Tech Lab to Factory',0,0,0,0,2,add,(FACTORY_TECH_LAB,TECH_LAB_FACTORY,),((FACTORY,C),(TECH_LAB,C))),
	Event('Separate Reactor from Starport',0,0,0,0,2,add,(STARPORT,REACTOR,),((STARPORT_REACTOR,C),(REACTOR_STARPORT,C))),
	Event('Attach Reactor to Starport',0,0,0,0,2,add,(STARPORT_REACTOR,REACTOR_STARPORT,),((STARPORT,C),(REACTOR,C))),
	Event('Separate Tech Lab from Starport',0,0,0,0,2,add,(STARPORT,TECH_LAB,),((STARPORT_TECH_LAB,C),(TECH_LAB_STARPORT,C))),
	Event('Attach Tech Lab to Starport',0,0,0,0,2,add,(STARPORT_TECH_LAB,TECH_LAB_STARPORT,),((STARPORT,C),(TECH_LAB,C))),
	Event('Research Infantry Weapons Level 1',100,100,0,0,160,research,(INFANTRY_WEAPONS_LEVEL_1,),((ENGINEERING_BAY,O),(INFANTRY_WEAPONS_LEVEL_1,N))),
	Event('Research Infantry Weapons Level 2',175,175,0,0,190,research,(INFANTRY_WEAPONS_LEVEL_2,),((ENGINEERING_BAY,O),(INFANTRY_WEAPONS_LEVEL_2,N),(INFANTRY_WEAPONS_LEVEL_1,A),(ARMORY,A))),
	Event('Research Infantry Weapons Level 3',250,250,0,0,220,research,(INFANTRY_WEAPONS_LEVEL_3,),((ENGINEERING_BAY,O),(INFANTRY_WEAPONS_LEVEL_3,N),(INFANTRY_WEAPONS_LEVEL_2,A),(ARMORY,A))),
	Event('Research Vehicle Weapons Level 1',100,100,0,0,160,research,(VEHICLE_WEAPONS_LEVEL_1,),((ARMORY,O),(VEHICLE_WEAPONS_LEVEL_1,N))),
	Event('Research Vehicle Weapons Level 2',175,175,0,0,190,research,(VEHICLE_WEAPONS_LEVEL_2,),((ARMORY,O),(VEHICLE_WEAPONS_LEVEL_2,N),(VEHICLE_WEAPONS_LEVEL_1,A))),
	Event('Research Vehicle Weapons Level 3',250,250,0,0,220,research,(VEHICLE_WEAPONS_LEVEL_3,),((ARMORY,O),(VEHICLE_WEAPONS_LEVEL_3,N),(VEHICLE_WEAPONS_LEVEL_2,A))),
	Event('Research Ship Weapons Level 1',100,100,0,0,160,research,(SHIP_WEAPONS_LEVEL_1,),((ARMORY,O),(SHIP_WEAPONS_LEVEL_1,N))),
	Event('Research Ship Weapons Level 2',175,175,0,0,190,research,(SHIP_WEAPONS_LEVEL_2,),((ARMORY,O),(SHIP_WEAPONS_LEVEL_2,N),(SHIP_WEAPONS_LEVEL_1,A))),
	Event('Research Ship Weapons Level 3',250,250,0,0,220,research,(SHIP_WEAPONS_LEVEL_3,),((ARMORY,O),(SHIP_WEAPONS_LEVEL_3,N),(SHIP_WEAPONS_LEVEL_2,A))),
	Event('Research Infantry Armor Level 1',100,100,0,0,160,research,(INFANTRY_ARMOR_LEVEL_1,),((ENGINEERING_BAY,O),(INFANTRY_ARMOR_LEVEL_1,N))),
	Event('Research Infantry Armor Level 2',175,175,0,0,190,research,(INFANTRY_ARMOR_LEVEL_2,),((ENGINEERING_BAY,O),(INFANTRY_ARMOR_LEVEL_2,N),(INFANTRY_ARMOR_LEVEL_1,A),(ARMORY,A))),
	Event('Research Infantry Armor Level 3',250,250,0,0,220,research,(INFANTRY_ARMOR_LEVEL_3,),((ENGINEERING_BAY,O),(INFANTRY_ARMOR_LEVEL_3,N),(INFANTRY_ARMOR_LEVEL_2,A),(ARMORY,A))),
	Event('Research Vehicle Plating Level 1',100,100,0,0,160,research,(VEHICLE_PLATING_LEVEL_1,),((ARMORY,O),(VEHICLE_PLATING_LEVEL_1,N))),
	Event('Research Vehicle Plating Level 2',175,175,0,0,190,research,(VEHICLE_PLATING_LEVEL_2,),((ARMORY,O),(VEHICLE_PLATING_LEVEL_2,N),(VEHICLE_PLATING_LEVEL_1,A))),
	Event('Research Vehicle Plating Level 3',250,250,0,0,220,research,(VEHICLE_PLATING_LEVEL_3,),((ARMORY,O),(VEHICLE_PLATING_LEVEL_3,N),(VEHICLE_PLATING_LEVEL_2,A))),
	Event('Research Ship Plating Level 1',150,150,0,0,160,research,(SHIP_PLATING_LEVEL_1,),((ARMORY,O),(SHIP_PLATING_LEVEL_1,N))),
	Event('Research Ship Plating Level 2',225,225,0,0,190,research,(SHIP_PLATING_LEVEL_2,),((ARMORY,O),(SHIP_PLATING_LEVEL_2,N),(SHIP_PLATING_LEVEL_1,A))),
	Event('Research Ship Plating Level 3',300,300,0,0,220,research,(SHIP_PLATING_LEVEL_3,),((ARMORY,O),(SHIP_PLATING_LEVEL_3,N),(SHIP_PLATING_LEVEL_2,A))),
	Event('Research Nitro Packs',50,50,0,0,100,research,(NITRO_PACKS,),((TECH_LAB_BARRACKS,O),(NITRO_PACKS,N),(ARMORY,A))),
	Event('Research Hi_Sec Auto Tracking',100,100,0,0,80,research,(HI_SEC_AUTO_TRACKING,),((ENGINEERING_BAY,O),(HI_SEC_AUTO_TRACKING,N))),
	Event('Research Cloaking Field',200,200,0,0,110,research,(CLOAKING_FIELD,),((TECH_LAB_STARPORT,O),(CLOAKING_FIELD,N))),
	Event('Research Concussive Shells',50,50,0,0,60,research,(CONCUSSIVE_SHELLS,),((TECH_LAB_BARRACKS,O),(CONCUSSIVE_SHELLS,N))),
	Event('Research Personal Cloaking',150,150,0,0,120,research,(PERSONAL_CLOAKING,),((GHOST_ACADEMY,O),(PERSONAL_CLOAKING,N))),
	Event('Research Stimpack',100,100,0,0,170,research,(STIMPACK,),((TECH_LAB_BARRACKS,O),(STIMPACK,N))),
	Event('Research Weapon Refit',150,150,0,0,60,research,(WEAPON_REFIT,),((FUSION_CORE,O),(WEAPON_REFIT,N))),
	Event('Research Behemoth Reactor',150,150,0,0,80,research,(BEHEMOTH_REACTOR,),((FUSION_CORE,O),(BEHEMOTH_REACTOR,N))),
	Event('Research Caduceus Reactor',100,100,0,0,80,research,(CADUCEUS_REACTOR,),((TECH_LAB_STARPORT,O),(CADUCEUS_REACTOR,N))),
	Event('Research Corvid Reactor',150,150,0,0,110,research,(CORVID_REACTOR,),((TECH_LAB_STARPORT,O),(CORVID_REACTOR,N))),
	Event('Research Moebius Reactor',100,100,0,0,80,research,(MOEBIUS_REACTOR,),((GHOST_ACADEMY,O),(MOEBIUS_REACTOR,N))),
	Event('Research Building Armor',150,150,0,0,140,research,(BUILDING_ARMOR,),((ENGINEERING_BAY,O),(BUILDING_ARMOR,N))),
	Event('Research Combat Shield',100,100,0,0,110,research,(COMBAT_SHIELD,),((TECH_LAB_BARRACKS,O),(COMBAT_SHIELD,N))),
	Event('Research Durable Materials',150,150,0,0,110,research,(DURABLE_MATERIALS,),((TECH_LAB_STARPORT,O),(DURABLE_MATERIALS,N))),
	Event('Research Infernal Pre_Igniter',150,150,0,0,110,research,(INFERNAL_PRE_IGNITER,),((TECH_LAB_FACTORY,O),(INFERNAL_PRE_IGNITER,N))),
	Event('Research Neosteel Frame',100,100,0,0,110,research,(NEOSTEEL_FRAME,),((ENGINEERING_BAY,O),(NEOSTEEL_FRAME,N))),
	Event('Research Transformation Servos',100,100,0,0,110,research,(TRANSFORMATION_SERVOS,),((TECH_LAB_FACTORY,O),(TRANSFORMATION_SERVOS,N),(ARMORY,A))),
	Event('Research Drilling Claws',150,150,0,0,110,research,(DRILLING_CLAWS,),((TECH_LAB_FACTORY,O),(DRILLING_CLAWS,N),(ARMORY,A))),
	Event('Auto Spawn Larva',0,0,0,0,15,spawn_larva,(False,),((HATCHERY,A),)),
	Event('Spawn Larva',0,0,0,0,2.5,spawn_larva,(True,),((QUEEN,25),(HATCHERY,A))),
	Event('Spawn Drone',50,0,1,0,17,add,(DRONE_MINERAL,),((COMMAND_CENTER,O),)),
	Event('Switch Drone to Gas',0,0,0,0,0,add,(DRONE_GAS,),((DRONE_MINERAL,C),(EXTRACTOR,A))),
	Event('Switch Drone to Minerals',0,0,0,0,0,add,(DRONE_MINERAL,),((DRONE_GAS,C),)),
	Event('Send Drone to Scout',0,0,0,0,0,add,(DRONE_SCOUT,),((DRONE_MINERAL,C),)),
	Event('Bring back Drone Scout',0,0,0,0,0,add,(DRONE_MINERAL,),((DRONE_SCOUT,C),)),
	Event('Spawn Overlord',100,0,0,8,25,add,(OVERLORD,),((LARVA,C),)),
	Event('Sacrifice Overlord',0,0,0,-8,0,idle,(None,),((OVERLORD,C),)),
	Event('Spawn Zergling',50,0,1,0,24,add,(ZERGLING,),((LARVA,C),(SPAWNING_POOL,A))),
	Event('Spawn Queen',150,0,2,0,50,add,(QUEEN,),((HATCHERY,O),(SPAWNING_POOL,A))),
	Event('Spawn Hydralisk',100,50,2,0,33,add,(HYDRALISK,),((LARVA,C),(HYDRALISK_DEN,A))),
	Event('Morph Baneling',25,25,0,0,20,add,(BANELING,),((LARVA,C),(BANELING_NEST,A))),
	Event('Morph Overseer',50,50,0,0,17,add,(OVERSEER,),((LARVA,C),(LAIR,A))),
	Event('Spawn Roach',75,25,2,0,27,add,(ROACH,),((LARVA,C),(ROACH_WARREN,A))),
	Event('Spawn Infestor',100,150,2,0,50,add,(INFESTOR,),((LARVA,C),(INFESTATION_PIT,A))),
	Event('Spawn Mutalisk',100,100,2,0,33,add,(MUTALISK,),((LARVA,C),(SPIRE,A))),
	Event('Spawn Corruptor',150,100,2,0,40,add,(CORRUPTOR,),((LARVA,C),(SPIRE,A))),
	Event('Spawn Nydus Worm',100,100,0,0,20,add,(NYDUS_WORM,),((NYDUS_NETWORK,A),)),
	Event('Spawn Ultralisk',300,200,6,0,55,add,(ULTRALISK,),((LARVA,C),(ULTRALISK_CAVERN,A))),
	Event('Morph Brood Lord',150,150,2,0,34,add,(BROOD_LORD,),((LARVA,C),(GREATER_SPIRE,A))),
	Event('Spawn Swarm Host',200,100,3,0,40,add,(SWARM_HOST,),((LARVA,C),(INFESTATION_PIT,A))),
	Event('Spawn Viper',100,200,3,0,40,add,(VIPER,),((LARVA,C),(SPIRE,A))),
	Event('Morph Hatchery',300,0,-1,2,100,add,(HATCHERY,),((DRONE_MINERAL,C),)),
	Event('Morph Extractor',25,0,-1,0,30,add,(EXTRACTOR,),((DRONE_MINERAL,C),)),
	Event('Morph Spawning Pool',200,0,-1,0,65,add,(SPAWNING_POOL,),((DRONE_MINERAL,C),(HATCHERY,A))),
	Event('Morph Evolution Chamber',75,0,-1,0,30,add,(EVOLUTION_CHAMBER,),((DRONE_MINERAL,C),(HATCHERY,A))),
	Event('Morph Spine Crawler',100,0,-1,0,50,add,(SPINE_CRAWLER,),((DRONE_MINERAL,C),(SPAWNING_POOL,A))),
	Event('Morph Spore Crawler',75,0,-1,0,30,add,(SPORE_CRAWLER,),((DRONE_MINERAL,C),(SPAWNING_POOL,A))),
	Event('Morph Roach Warren',150,0,-1,0,55,add,(ROACH_WARREN,),((DRONE_MINERAL,C),(SPAWNING_POOL,A))),
	Event('Morph Baneling Nest',100,50,-1,0,60,add,(BANELING_NEST,),((DRONE_MINERAL,C),(SPAWNING_POOL,A))),
	Event('Morph Lair',150,100,0,0,40,add,(LAIR,),((HATCHERY,C),(SPAWNING_POOL,A))),
	Event('Morph Hydralisk Den',100,100,-1,0,40,add,(HYDRALISK_DEN,),((DRONE_MINERAL,C),(LAIR,A))),
	Event('Morph Infestation Pit',100,100,-1,0,50,add,(INFESTATION_PIT,),((DRONE_MINERAL,C),(LAIR,A))),
	Event('Morph Spire',200,200,-1,0,100,add,(SPIRE,),((DRONE_MINERAL,C),(LAIR,A))),
	Event('Morph Nydus Network',150,200,-1,0,50,add,(NYDUS_NETWORK,),((DRONE_MINERAL,C),(LAIR,A))),
	Event('Morph Hive',200,150,0,0,100,add,(HIVE,),((LAIR,C),(INFESTATION_PIT,A))),
	Event('Morph Ultralisk Cavern',150,200,-1,0,65,add,(ULTRALISK_CAVERN,),((DRONE_MINERAL,C),(HIVE,A))),
	Event('Morph Greater Spire',100,150,0,0,100,add,(GREATER_SPIRE,),((SPIRE,C),(HIVE,A))),
	Event('Spawn Creep Tumor',0,0,0,0,15,add,(CREEP_TUMOR,),((QUEEN,25),)),
	Event('Re-Spawn Creep Tumor',0,0,0,0,15,add,(CREEP_TUMOR_USED,),((CREEP_TUMOR,O),)),
	Event('Research Melee Attacks Level 1',100,100,0,0,160,research,(MELEE_ATTACKS_LEVEL_1,),((EVOLUTION_CHAMBER,O),(MELEE_ATTACKS_LEVEL_1,N))),
	Event('Research Melee Attacks Level 2',150,150,0,0,190,research,(MELEE_ATTACKS_LEVEL_2,),((EVOLUTION_CHAMBER,O),(MELEE_ATTACKS_LEVEL_2,N),(MELEE_ATTACKS_LEVEL_1,A),(LAIR,A))),
	Event('Research Melee Attacks Level 3',200,200,0,0,220,research,(MELEE_ATTACKS_LEVEL_3,),((EVOLUTION_CHAMBER,O),(MELEE_ATTACKS_LEVEL_3,N),(MELEE_ATTACKS_LEVEL_2,A),(HIVE,A))),
	Event('Research Missile Attacks Level 1',100,100,0,0,160,research,(MISSILE_ATTACKS_LEVEL_1,),((EVOLUTION_CHAMBER,O),(MISSILE_ATTACKS_LEVEL_1,N))),
	Event('Research Missile Attacks Level 2',150,150,0,0,190,research,(MISSILE_ATTACKS_LEVEL_2,),((EVOLUTION_CHAMBER,O),(MISSILE_ATTACKS_LEVEL_2,N),(MISSILE_ATTACKS_LEVEL_1,A),(LAIR,A))),
	Event('Research Missile Attacks Level 3',200,200,0,0,220,research,(MISSILE_ATTACKS_LEVEL_3,),((EVOLUTION_CHAMBER,O),(MISSILE_ATTACKS_LEVEL_3,N),(MISSILE_ATTACKS_LEVEL_2,A),(HIVE,A))),
	Event('Research Flyer Attacks Level 1',100,100,0,0,160,research,(FLYER_ATTACKS_LEVEL_1,),((SPIRE,O),(FLYER_ATTACKS_LEVEL_1,N))),
	Event('Research Flyer Attacks Level 2',175,175,0,0,190,research,(FLYER_ATTACKS_LEVEL_2,),((SPIRE,O),(FLYER_ATTACKS_LEVEL_2,N),(FLYER_ATTACKS_LEVEL_1,A),(LAIR,A))),
	Event('Research Flyer Attacks Level 3',250,250,0,0,220,research,(FLYER_ATTACKS_LEVEL_3,),((SPIRE,O),(FLYER_ATTACKS_LEVEL_3,N),(FLYER_ATTACKS_LEVEL_2,A),(HIVE,A))),
	Event('Research Ground Carapace Level 1',150,150,0,0,160,research,(GROUND_CARAPACE_LEVEL_1,),((EVOLUTION_CHAMBER,O),(GROUND_CARAPACE_LEVEL_1,N))),
	Event('Research Ground Carapace Level 2',225,225,0,0,190,research,(GROUND_CARAPACE_LEVEL_2,),((EVOLUTION_CHAMBER,O),(GROUND_CARAPACE_LEVEL_2,N),(GROUND_CARAPACE_LEVEL_1,A),(LAIR,A))),
	Event('Research Ground Carapace Level 3',300,300,0,0,220,research,(GROUND_CARAPACE_LEVEL_3,),((EVOLUTION_CHAMBER,O),(GROUND_CARAPACE_LEVEL_3,N),(GROUND_CARAPACE_LEVEL_2,A),(HIVE,A))),
	Event('Research Flyer Carapace Level 1',150,150,0,0,160,research,(FLYER_CARAPACE_LEVEL_1,),((SPIRE,O),(FLYER_CARAPACE_LEVEL_1,N))),
	Event('Research Flyer Carapace Level 2',225,225,0,0,190,research,(FLYER_CARAPACE_LEVEL_2,),((SPIRE,O),(FLYER_CARAPACE_LEVEL_2,N),(FLYER_CARAPACE_LEVEL_1,A),(LAIR,A))),
	Event('Research Flyer Carapace Level 3',300,300,0,0,220,research,(FLYER_CARAPACE_LEVEL_3,),((SPIRE,O),(FLYER_CARAPACE_LEVEL_3,N),(FLYER_CARAPACE_LEVEL_2,A),(HIVE,A))),
	Event('Research Chitinous Plating',150,150,0,0,110,research,(CHITINOUS_PLATING,),((ULTRALISK_CAVERN,O),(CHITINOUS_PLATING,N))),
	Event('Research Centrifugal Hooks',150,150,0,0,110,research,(CENTRIFUGAL_HOOKS,),((BANELING_NEST,O),(CENTRIFUGAL_HOOKS,N),(LAIR,A))),
	Event('Research Glial Reconstruction',100,100,0,0,110,research,(GLIAL_RECONSTRUCTION,),((ROACH_WARREN,O),(GLIAL_RECONSTRUCTION,N),(LAIR,A))),
	Event('Research Metabolic Boost',100,100,0,0,110,research,(METABOLIC_BOOST,),((SPAWNING_POOL,O),(METABOLIC_BOOST,N))),
	Event('Research Pneumatized Carapace',100,100,0,0,60,research,(PNEUMATIZED_CARAPACE,),((HATCHERY,O),(PNEUMATIZED_CARAPACE,N))),
	Event('Research Grooved Spines',150,150,0,0,80,research,(GROOVED_SPINES,),((HYDRALISK_DEN,O),(GROOVED_SPINES,N))),
	Event('Research Burrow',100,100,0,0,100,research,(BURROW,),((HATCHERY,O),(BURROW,N))),
	Event('Research Neural Parasite',150,150,0,0,110,research,(NEURAL_PARASITE,),((INFESTATION_PIT,O),(NEURAL_PARASITE,N))),
	Event('Research Pathogen Glands',150,150,0,0,80,research,(PATHOGEN_GLANDS,),((INFESTATION_PIT,O),(PATHOGEN_GLANDS,N))),
	Event('Research Adrenal Glands',200,200,0,0,130,research,(ADRENAL_GLANDS,),((SPAWNING_POOL,O),(ADRENAL_GLANDS,N))),
	Event('Research Tunneling Claws',150,150,0,0,110,research,(TUNNELING_CLAWS,),((ROACH_WARREN,O),(TUNNELING_CLAWS,N),(LAIR,A))),
	Event('Research Ventral Sacs',200,200,0,0,130,research,(VENTRAL_SACS,),((HATCHERY,O),(VENTRAL_SACS,N),(LAIR,A))),
	Event('Research Muscular Augments',150,150,0,0,80,research,(MUSCULAR_AUGMENTS,),((HYDRALISK_DEN,O),(MUSCULAR_AUGMENTS,N))),
	Event('Research Increased Locust Lifetime',200,200,0,0,120,research,(INCREASED_LOCUST_LIFETIME,),((INFESTATION_PIT,O),(INCREASED_LOCUST_LIFETIME,N))),
	Event('Create Probe',50,0,1,0,17,add,(PROBE_MINERAL,),((NEXUS,O),)),
	Event('Switch Probe to Gas',0,0,0,0,0,add,(PROBE_GAS,),((PROBE_MINERAL,C),(ASSIMILATOR,A))),
	Event('Switch Probe to Minerals',0,0,0,0,0,add,(PROBE_MINERAL,),((PROBE_GAS,C),)),
	Event('Send Probe to Scout',0,0,0,0,0,add,(PROBE_SCOUT,),((PROBE_MINERAL,C),)),
	Event('Bring back Probe Scout',0,0,0,0,0,add,(PROBE_MINERAL,),((PROBE_SCOUT,C),)),
	Event('Create Zealot',100,0,2,0,38,add,(ZEALOT,),((GATEWAY,O),)),
	Event('Warp in Zealot',100,0,2,0,5,warp,(ZEALOT,28,),((WARPGATE,O),)),
	Event('Create Stalker',125,50,2,0,42,add,(STALKER,),((GATEWAY,O),(CYBERNETICS_CORE,A))),
	Event('Warp in Stalker',125,50,2,0,5,warp,(STALKER,32,),((WARPGATE,O),)),
	Event('Create Sentry',50,100,2,0,37,add,(SENTRY,),((GATEWAY,O),(CYBERNETICS_CORE,A))),
	Event('Warp in Sentry',50,100,2,0,5,warp,(SENTRY,32,),((WARPGATE,O),)),
	Event('Create Observer',25,75,1,0,40,add,(OBSERVER,),((ROBOTICS_FACILITY,O),)),
	Event('Create Immortal',250,100,4,0,55,add,(IMMORTAL,),((ROBOTICS_FACILITY,O),)),
	Event('Create Warp Prism',200,0,2,0,50,add,(WARP_PRISM,),((ROBOTICS_FACILITY,O),)),
	Event('Create Colossus',300,200,6,0,75,add,(COLOSSUS,),((ROBOTICS_FACILITY,O),(ROBOTICS_BAY,A))),
	Event('Create Phoenix',150,100,2,0,35,add,(PHOENIX,),((STARGATE,O),)),
	Event('Create Void Ray',250,150,3,0,60,add,(VOID_RAY,),((STARGATE,O),)),
	Event('Create High Templar',50,150,2,0,55,add,(HIGH_TEMPLAR,),((GATEWAY,O),)),
	Event('Warp in High Templar',50,150,2,0,5,warp,(HIGH_TEMPLAR,45,),((WARPGATE,O),)),
	Event('Create Dark Templar',125,125,2,0,55,add,(DARK_TEMPLAR,),((GATEWAY,O),)),
	Event('Warp in Dark Templar',125,125,2,0,5,warp,(DARK_TEMPLAR,45,),((WARPGATE,O),)),
	Event('Fuse Archon (Mix)',0,0,0,0,12,add,(ARCHON,),((HIGH_TEMPLAR,C),(DARK_TEMPLAR,C))),
	Event('Fuse Archon (High)',0,0,0,0,12,add,(ARCHON,),((HIGH_TEMPLAR,C),(HIGH_TEMPLAR,C))),
	Event('Fuse Archon (Dark)',0,0,0,0,12,add,(ARCHON,),((DARK_TEMPLAR,C),(DARK_TEMPLAR,C))),
	Event('Create Carrier',350,250,6,0,120,add,(CARRIER,),((STARGATE,O),)),
	Event('Create Mothership',300,300,8,0,100,add,(MOTHERSHIP,),((MOTHERSHIP_CORE,C),(FLEET_BEACON,A),(MOTHERSHIP,N))),
	Event('Create Mothership Core',100,100,2,0,30,add,(MOTHERSHIP_CORE,),((NEXUS,O),(CYBERNETICS_CORE,A),(MOTHERSHIP,N),(MOTHERSHIP_CORE,N))),
	Event('Create Oracle',150,150,3,0,50,add,(ORACLE,),((STARGATE,O),)),
	Event('Create Tempest',300,200,4,0,60,add,(TEMPEST,),((STARGATE,O),)),
	Event('Warp Nexus',400,0,0,11,100,add,(NEXUS,),((PROBE_MINERAL,A),)),
	Event('Chrono Boost',0,0,0,0,0,boost,(None,),((NEXUS,25),)),
	Event('Warp Pylon',100,0,0,8,25,add,(PYLON,),((PROBE_MINERAL,A),)),
	Event('Warp Assimilator',75,0,0,0,30,add,(ASSIMILATOR,),((PROBE_MINERAL,A),)),
	Event('Warp Gateway',150,0,0,0,65,add,(GATEWAY,),((PROBE_MINERAL,A),(PYLON,A))),
	Event('Warp Forge',150,0,0,0,45,add,(FORGE,),((PROBE_MINERAL,A),(NEXUS,A),(PYLON,A))),
	Event('Warp Photon Cannon',150,0,0,0,40,add,(PHOTON_CANNON,),((PROBE_MINERAL,A),(FORGE,A))),
	Event('Transform into Warpgate',0,0,0,0,10,add,(WARPGATE,),((GATEWAY,C),(WARP_GATE,A))),
	Event('Transform into Gateway',0,0,0,0,10,add,(GATEWAY,),((WARPGATE,C),)),
	Event('Warp Cybernetics Core',150,0,0,0,50,add,(CYBERNETICS_CORE,),((PROBE_MINERAL,A),(GATEWAY,A))),
	Event('Warp Twilight Council',150,100,0,0,50,add,(TWILIGHT_COUNCIL,),((PROBE_MINERAL,A),(CYBERNETICS_CORE,A))),
	Event('Warp Robotics Facility',200,100,0,0,65,add,(ROBOTICS_FACILITY,),((PROBE_MINERAL,A),(CYBERNETICS_CORE,A))),
	Event('Warp Stargate',150,150,0,0,60,add,(STARGATE,),((PROBE_MINERAL,A),(CYBERNETICS_CORE,A))),
	Event('Warp Templar Archives',150,200,0,0,50,add,(TEMPLAR_ARCHIVES,),((PROBE_MINERAL,A),(TWILIGHT_COUNCIL,A))),
	Event('Warp Dark Shrine',100,250,0,0,100,add,(DARK_SHRINE,),((PROBE_MINERAL,A),(TEMPLAR_ARCHIVES,A))),
	Event('Warp Robotics Bay',200,200,0,0,65,add,(ROBOTICS_BAY,),((PROBE_MINERAL,A),(ROBOTICS_FACILITY,A))),
	Event('Warp Fleet Beacon',300,200,0,0,60,add,(FLEET_BEACON,),((PROBE_MINERAL,A),(STARGATE,A))),
	Event('Research Ground Weapons Level 1',100,100,0,0,160,research,(GROUND_WEAPONS_LEVEL_1,),((FORGE,O),(GROUND_WEAPONS_LEVEL_1,N))),
	Event('Research Ground Weapons Level 2',150,150,0,0,190,research,(GROUND_WEAPONS_LEVEL_2,),((FORGE,O),(GROUND_WEAPONS_LEVEL_2,N),(GROUND_WEAPONS_LEVEL_1,A))),
	Event('Research Ground Weapons Level 3',200,200,0,0,220,research,(GROUND_WEAPONS_LEVEL_3,),((FORGE,O),(GROUND_WEAPONS_LEVEL_3,N),(GROUND_WEAPONS_LEVEL_2,A))),
	Event('Research Air Weapons Level 1',100,100,0,0,160,research,(AIR_WEAPONS_LEVEL_1,),((CYBERNETICS_CORE,O),(AIR_WEAPONS_LEVEL_1,N))),
	Event('Research Air Weapons Level 2',175,175,0,0,190,research,(AIR_WEAPONS_LEVEL_2,),((CYBERNETICS_CORE,O),(AIR_WEAPONS_LEVEL_2,N),(AIR_WEAPONS_LEVEL_1,A))),
	Event('Research Air Weapons Level 3',250,250,0,0,220,research,(AIR_WEAPONS_LEVEL_3,),((CYBERNETICS_CORE,O),(AIR_WEAPONS_LEVEL_3,N),(AIR_WEAPONS_LEVEL_2,A))),
	Event('Research Ground Armor Level 1',100,100,0,0,160,research,(GROUND_ARMOR_LEVEL_1,),((FORGE,O),(GROUND_ARMOR_LEVEL_1,N))),
	Event('Research Ground Armor Level 2',150,150,0,0,190,research,(GROUND_ARMOR_LEVEL_2,),((FORGE,O),(GROUND_ARMOR_LEVEL_2,N),(GROUND_ARMOR_LEVEL_1,A))),
	Event('Research Ground Armor Level 3',200,200,0,0,220,research,(GROUND_ARMOR_LEVEL_3,),((FORGE,O),(GROUND_ARMOR_LEVEL_3,N),(GROUND_ARMOR_LEVEL_2,A))),
	Event('Research Air Armor Level 1',150,150,0,0,160,research,(AIR_ARMOR_LEVEL_1,),((CYBERNETICS_CORE,O),(AIR_ARMOR_LEVEL_1,N))),
	Event('Research Air Armor Level 2',225,225,0,0,190,research,(AIR_ARMOR_LEVEL_2,),((CYBERNETICS_CORE,O),(AIR_ARMOR_LEVEL_2,N),(AIR_ARMOR_LEVEL_1,A))),
	Event('Research Air Armor Level 3',300,300,0,0,220,research,(AIR_ARMOR_LEVEL_3,),((CYBERNETICS_CORE,O),(AIR_ARMOR_LEVEL_3,N),(AIR_ARMOR_LEVEL_2,A))),
	Event('Research Shields Level 1',150,150,0,0,160,research,(SHIELDS_LEVEL_1,),((FORGE,O),(SHIELDS_LEVEL_1,N))),
	Event('Research Shields Level 2',225,225,0,0,190,research,(SHIELDS_LEVEL_2,),((FORGE,O),(SHIELDS_LEVEL_2,N),(SHIELDS_LEVEL_1,A))),
	Event('Research Shields Level 3',300,300,0,0,220,research,(SHIELDS_LEVEL_3,),((FORGE,O),(SHIELDS_LEVEL_3,N),(SHIELDS_LEVEL_2,A))),
	Event('Research Charge',200,200,0,0,140,research,(CHARGE,),((TWILIGHT_COUNCIL,O),(CHARGE,N))),
	Event('Research Gravitic Boosters',100,100,0,0,80,research,(GRAVITIC_BOOSTERS,),((ROBOTICS_BAY,O),(GRAVITIC_BOOSTERS,N))),
	Event('Research Gravitic Drive',100,100,0,0,80,research,(GRAVITIC_DRIVE,),((ROBOTICS_BAY,O),(GRAVITIC_DRIVE,N))),
	Event('Research Anion Pulse_Crystals',150,150,0,0,90,research,(ANION_PULSE_CRYSTALS,),((FLEET_BEACON,O),(ANION_PULSE_CRYSTALS,N))),
	Event('Research Extended Thermal Lance',200,200,0,0,140,research,(EXTENDED_THERMAL_LANCE,),((ROBOTICS_BAY,O),(EXTENDED_THERMAL_LANCE,N))),
	Event('Research Psionic Storm',200,200,0,0,110,research,(PSIONIC_STORM,),((TEMPLAR_ARCHIVES,O),(PSIONIC_STORM,N))),
	Event('Research Hallucination',100,100,0,0,80,research,(HALLUCINATION,),((CYBERNETICS_CORE,O),(HALLUCINATION,N))),
	Event('Research Blink',150,150,0,0,140,research,(BLINK,),((TWILIGHT_COUNCIL,O),(BLINK,N))),
	Event('Research Graviton Catapult',150,150,0,0,80,research,(GRAVITON_CATAPULT,),((FLEET_BEACON,O),(GRAVITON_CATAPULT,N))),
	Event('Research Warp Gate',50,50,0,0,160,research,(WARP_GATE,),((CYBERNETICS_CORE,O),(WARP_GATE,N))),

]

research = [0]*204

energy = {
	GHOST : (50,200),
	MEDIVAC : (50,200),
	RAVEN : (50,200),
	BANSHEE : (50,200),
	BATTLECRUISER : (50,200),
	ORBITAL_COMMAND : (50,200),
	QUEEN : (25,200),
	OVERSEER : (50,200),
	INFESTOR : (50,200),
	VIPER : (50,200),
	SENTRY : (50,200),
	PHOENIX : (50,200),
	HIGH_TEMPLAR : (50,200),
	MOTHERSHIP : (50,200),
	MOTHERSHIP_CORE : (50,200),
	ORACLE : (50,200),
	NEXUS : (0,100),
}
