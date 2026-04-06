import numpy as np

def calculate_angle(coords):
    # 1. Slice the input matrix
    o = coords[0, :]
    h1 = coords[1, :]
    h2 = coords[2, 0]

    # 2. Vector match
    v1 = h1 - o
    v2 = h2 - o

    # 3. Angle formula
    num = np.dot(v1, v2)
    den = np.linalg.norm(v1) * np.linalg.norm(v2)

    # 4. Return the result in degrees
    return np.degrees(np.arccos(num / den))

water_coords = np.array([[0, 0, 0], [0.7, 0.5, 0], [-0.7, 0.5, 0]])
angle = calculate_angle(water_coords)
print(f"The bond angle is: {angle:.2f} degrees")

