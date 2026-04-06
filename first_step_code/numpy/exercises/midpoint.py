"""
Find the center between two atoms
"""
import numpy as np

p1 = np.array([1.0, 2.0, 3.0])
p2 = np.array([4.0, 5.0, 6.0])

midpoint = (p1 + p2)/2

print(f"The midpoint is: {midpoint}")
