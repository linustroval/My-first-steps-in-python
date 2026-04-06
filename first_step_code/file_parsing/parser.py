import os

# 1. Define our chemical Database
atomic_masses = {
        "O": 15.999,
        "H": 1.008,
        "C": 12.011,
        "N": 14.007
}

# 2. Open the file

filename = "water.xyz"

if not os.path.exists(filename):
    print(f"Error: {filename} not found !")
else:
    with open(filename, "r") as f:
        all_lines = f.readlines()
    
    # 3. Initialize our counter
    total_mass = 0.0

    # 4. Process the lines
    # We use slicing [2:] to skip the first two lines (0 and 1)
    for line in all_lines[2:]:
        parts = line.strip().split()

        if not parts:
            continue
        
        symbol = parts[0]

        if symbol in atomic_masses:
            mass = atomic_masses[symbol]
            total_mass += mass
            print(f"Adding {symbol}: {mass} u")
        else:
            print(f"Warning: Mass for {symbol} not found in database.")
    print("-" * 30)
    print(f"Total Molecular Mass: {total_mass:.3f} u")
