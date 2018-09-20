# Python Lists - 2

#
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall, kit, liv, bed, bath]

print(areas)

#
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

print(areas)

#
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

print(house)
print(type(house))

#
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

print(areas[1])
print(areas[-1])
print(areas[5])

#
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

eat_sleep_area = areas[3] + areas[7]

print(eat_sleep_area)

#
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

downstairs = areas[0:6]

upstairs = areas[6:]

print(downstairs)
print(upstairs)

#
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

downstairs = areas[:6]

upstairs = areas[6:]

#
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

areas[-1] = 10.50

areas[4] = "chill zone"

#
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

areas_1 = areas + ["poolhouse", 24.5]

areas_2 = areas_1 + ["garage", 15.45]

#
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

areas_copy = areas[:]

areas_copy[0] = 5.0

print(areas)