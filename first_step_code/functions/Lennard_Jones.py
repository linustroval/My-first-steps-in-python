"""
In chemistry, the Lennard-Jones potential is used to approximate the interaction between two non-bonded atoms:
V(r) = 4ϵ[(σ/r)¹² - (σ/r)⁶]
"""
def lennard_jones(r, epsilon, sigma):
    ratio = sigma / r
    V = 4 * epsilon * ((ratio)**12 - (ratio)**6)
    return V

first_try = lennard_jones(3.5, 0.5, 3.0)
print(first_try)
