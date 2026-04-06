"""
In computational chemistry, the "bond lenght" is simply the Euclidian distnace between two coordinate vectors.
1. Define atom_a = np.array([0.0, 0.0, 0.0]) (Oxygen).
2. Define atom_b = np.array([0.0, 0.0, 0.96]) (Hydrogen).
3. Calculate the distance using vector subtraction and np.linalg.norm().
4. Print the result
"""
import numpy as np

atom_a = np.array([0.0, 0.0, 0.0])
atom_b = np.array([0.0, 0.0, 0.96])

diff = atom_a - atom_b
distance = np.linalg.norm(diff)
print(f"The distance is: {distance}")
