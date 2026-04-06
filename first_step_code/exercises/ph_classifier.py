"""
Create a script where you define a variable current_ph.
Use if/elif/else to print:
"Strongly Acidic" if pH is less than 3
"Acidic" if pH is between 3 and 6.9
"Neutral" if pH is exactly 7
"Basic" if pH is greater than 7
"""
current_ph = float(input("Enter the value of ph: "))
print("The pH is:", current_ph)

if current_ph < 3.0:
    print("The pH is Strongly Acidic")
elif 3 < current_ph < 6.9:
    print("The pH is Acididc")
elif current_ph == 7.0:
    print("The pH is Neutral")
elif current_ph > 7.0:
    print("The pH is Basic")
