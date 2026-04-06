"""
In chemistry, we often store coordinates as a matrix of shape (N,3),
where N is the number of atoms.
"""
# A water molecule (approximate coords)
# Rows: Oxygen, Hydrogen1, Hydrogen2

import numpy as np

water = np.array([
    [0.000, 0.000, 0.000],
    [0.757, 0.586, 0.000],
    [-0.757, 0.586, 0.000]
])

print(water.shape)
