"""
Imagine you have a Water molecule and you want to move it 2.0 Å in the Y-axis.
1. Create a matrix for Water.
2. Create  a "translation vector".
3. Add shift to water.
4. Print the result.
"""
import numpy as np

water = np.array([
    [0.0, 0.0, 0.0],
    [0.7, 0.5, 0.0],
    [-0.7, 0.5, 0.0]
])

shift = np.array([0.0, 2.0, 0.0])

new_coord = water + shift

print(f"The new coord is: {new_coord}")
