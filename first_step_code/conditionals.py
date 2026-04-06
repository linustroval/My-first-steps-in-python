delta_g = -20.5 # Gibbs Free Energy in KJ/mol

if delta_g < 0:
    print("The reaction is spontaneous.")
elif delta_g == 0:
    print("The reaction is at equilibrium.")
else:
    print("The reaction is non-spontaneous.")
