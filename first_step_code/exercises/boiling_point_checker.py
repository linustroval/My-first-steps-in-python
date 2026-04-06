"""
You have a list of temperatures in Celsius: [80, 100, 120, 95]
1. Use a for loop to check each temperature.
2. Inside the loop, use an if statement to print "Boilling!" only if the temperature is 100 or higher. Otherwise, print "Not boliling yet!".
"""
temperatures = [80, 100, 120, 95]

for i in temperatures:
    if i < 100:
        print("The temperature is", i,"so Not boliling yet!")
    else:
        print("The temperature is", i, "so Boilling!")
