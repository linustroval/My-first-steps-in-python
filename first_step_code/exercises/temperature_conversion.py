"""
You have a temperature of 373.15K.
1. Convert it in to Celsius (C = K - 273.15)
2. Then, convert that Celsius value to Fahrenheit (F = (C x 9/5) + 32)
3. Print both results

"""

kelvin = 373.15 # Temperature in Kelvins
celsius = kelvin - 273.15 # Temperature in Celsius
fahrenheit = (celsius * 9/5) + 32

print(f"The temperature is {kelvin} in Kelvin, {celsius} in celsius and {fahrenheit} in Fahrenheit")
