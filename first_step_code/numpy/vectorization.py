"""
In Python to add two lists, you need a for loop.
In Numpy, you just use +. This is called Vectorization.
"""
import numpy as np

coord = np.array([1.2, 0.5, 3.1])
shift = np.array([0.5, 0.0, 0.0])

new_coord = coord + shift
print(new_coord) 
