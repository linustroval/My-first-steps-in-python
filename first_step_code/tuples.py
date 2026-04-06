"""
A tuple is like a list, but you cannot change it once it is created. We can use them for things that should stay constant, like the (x,y,z) coordinates of an atom in a specific frame.
Uses parentheses () instead of brackets []
"""

# Oxygena atom the origin
oxygen_xyz = (0.0, 0.0, 0.0)

# This will cause an error because you can't change a tuple:
# oxygen_xyz[0] = 1.0 
