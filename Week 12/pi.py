import numpy as np
from numpy.core import numeric

N = 100000

points = np.random.rand(N, 2) #Generates random points in lsit
# print(points)
# [0.71815002 0.56709327]
#  [0.90289592 0.28656308]
#  [0.17067172 0.5163204 ]

norms = np.linalg.norm(points, axis = 1) ##checks if it is in circle radius 1 (norm calucates each point.) 
# puts each in a list)
# sqrt of x^2 + y^2 (get's the distance)
# print(norms)
# [0.39818306 0.24270988 0.46227009 ... 0.39179251 0.33144354 0.95400536]


inside_circle = norms <=1 
# sets true or false if points are in circle or not
# print(inside_circle)
# [ True  True  True ...  True  True False]


number_inside_circle = float(sum(inside_circle))
# print(number_inside_circle)
#sums how many trues there were in inside_circle

print((4 * number_inside_circle / float(N)))
# 4 * Points within a circle / total number of points 