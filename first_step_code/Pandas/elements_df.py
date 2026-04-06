import pandas as pd

# We use a Dictionary to define the columns
data = {
        "Symbol": ["H", "C", "O", "N", "Cl"],
        "Name": ["Hydrogen", "Carbon", "Oxygen", "Nitrogen", "Chlorine"],
        "Atomic_Weight": [1.008, 12.011, 15.999, 14.007, 35.45],
        "Electronegativity":[2.20, 2.55, 3.44, 3.04, 3.16]
}

# Create the Dataframe
df = pd.DataFrame(data)
df["Mass_mg"] = df["Atomic_Weight"] * 1000

# Show the table
print(df)

# Get a summary of the numerical data
print(df.describe())

# Get the average atomic weight
avg_weight = df["Atomic_Weight"].mean()
print(f"\nThe average atomic weight is: {avg_weight:.2f} u")

# Filter: Show rows where Electronegativity > 3.0
high_en = df[df["Electronegativity"] > 3.0]

heavy_elements = df[df["Atomic_Weight"] > 13.0]

print("\nHighly Electronegative Elements:")
print(high_en)

# Save the heavy elements specifically
heavy_elements.to_csv("heavy_elements.csv", index=False)

print("\nSaved the following heavy elements to heavy_elements.csv:")
print(heavy_elements)

import matplotlib.pyplot as plt

# Create a scatter plot
plt.scatter(df["Atomic_Weight"], df["Electronegativity"])

# Add labels (Always label your axes!)
plt.xlabel("Atomic Weight (u)")
plt.ylabel("Electronegativity (Pauling scale)")
plt.title("Atomic Weight vs Electronegativity")

# Save the plot as an image
plt.savefig("chemistry_plot.png")

# Show the plot (This will open a window in Ubuntu)
plt.show()
