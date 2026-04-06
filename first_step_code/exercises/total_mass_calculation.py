# First I declare the different masses of the molecule

mass = [1.008, 1.008, 15.999]

# Second I define the total_mass variable

total_mass = 0
for i in mass:
    total_mass += i

print(f"The total mass is: {total_mass}")

