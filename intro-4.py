# NumPy - 4

#
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

import numpy as np

np_baseball = np.array(baseball)

print(type(np_baseball))

#
import numpy as np

np_height = np.array(height)

print(np_height)

np_height_m = np_height * 0.025

print(np_height_m)

#
import numpy as np

np_height_m = np.array(height) * 0.0254

np_weight_kg = np.array(weight) * 0.453592

bmi = np_weight_kg / (np_height_m ** 2)

print(bmi)

#
import numpy as np

np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

light = bmi < 21 #Create a boolean numpy array: True/ False

print(light)

print(bmi[light])

#
import numpy as np

np_weight = np.array(weight)
np_height = np.array(height)

print(weight[50])

print(np_height[100:111])

#
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
import numpy as np

np_baseball = np.array(baseball)

print(type(np_baseball))

print(np_baseball.shape)

#
import numpy as np

np_baseball = np.array(baseball)

print(np_baseball.shape)

#
import numpy as np

np_baseball = np.array(baseball)

print(np_baseball[49,:])

np_weight = np_baseball[:,1]

print(np_baseball[123,0])

#
import numpy as np

np_baseball = np.array(baseball)

print(np_baseball + updated)

conversion = np.array([0.0254, 0.453592, 1])

print(np_baseball * conversion)

#
import numpy as np

np_height = np_baseball[:,0]

print(np.mean(np_height))

print(np.median(np_height))

#
import numpy as np

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg)) # You have to do the type conversion !!!

med = np.median(np_baseball[:,0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

#
import numpy as np

np_positions = np.array(positions)
np_heights = np.array(heights)

gk_heights = np_heights[np_positions == 'GK']

other_heights = np_heights[np_positions != 'GK']

print("Median height of goalkeepers: " + str(np.median(gk_heights)))