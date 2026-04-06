import numpy as np

water = np.array([
    [0.0, 0.0, 0.0],
    [0.7, 0.5, 0.0],
    [-0.7, 0.5, 0.0]
])

oxygen = water[0, :]
hydrogen_1 = water[1, :]
hydrogen_2 = water[2, :]

v1 = hydrogen_1 - oxygen
v2 = hydrogen_2 - oxygen

# print(v1)
# print(v2)

numerator = np.dot(v1, v2)
denominator = np.linalg.norm(v1) * np.linalg.norm(v2)

angle_radians = np.arccos(numerator / denominator)
angle_degrees = np.degrees(angle_radians)

print(f"The angle in radians is: {angle_radians}")
print(f"The angle in degrees is: {angle_degrees}")

