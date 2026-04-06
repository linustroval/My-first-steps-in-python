import os
import numpy as np

# 1. Define our chemical database

atomic_masses = {
        "O": 15.999,
        "H": 1.008,
        "C": 12.011,
        "N": 14.007
}

total_mass = 0.0
weighted_position_sum = np.array([0.0, 0.0, 0.0]) 

filename = "methane.xyz"

if not os.path.exists(filename):
    print(f"Error: {filename} not found !")
else:
    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines[2:]:
        parts = line.strip().split()

        if not parts:
            continue
        symbol = parts[0]
        r_i = np.array(parts[1:], dtype=float)
        m_i = atomic_masses[symbol]
        total_mass += m_i
        weighted_position_sum += m_i * r_i
center_of_mass = weighted_position_sum / total_mass

output = "cm_output.txt"

with open(output, "w") as f:
    f.write("--- Center of Mass Calculation ---\n")
    f.write(f"Source file: {filename}\n")
    f.write(f"Total Mass: {total_mass:.4f} u\n")
    f.write(f"CM Coordinates (x, y, z): {center_of_mass}\n")

print(f"Results successfully saved to {output}")
 
