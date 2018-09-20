# Functions and packages - 3

#
var1 = [1, 2, 3, 4]
var2 = True

print(type(var1))
print(len(var1))
out2 = int(var2)

#
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second

full_sorted = sorted(full, reverse = True)

print(full_sorted)

#
place = "poolhouse"

place_up = place.upper()

print(place)
print(place_up)

print(place.count("o"))

#
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

print(areas.index(20.0))
print(areas.count(9.50))

#
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

areas.append(24.5)
areas.append(15.45)

print(areas)

areas.reverse()

print(areas)

#
import math

C = 2 * math.pi * r
A = math.pi * r ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

#
r = 192500

from math import radians

dist = r * radians(12)

print(dist)