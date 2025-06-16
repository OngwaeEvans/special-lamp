# assignment1.py

# (a) Line graph for temperature readings
import matplotlib.pyplot as plt

temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.plot(days, temperatures, marker='o')
plt.title("Temperature Readings Over a Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("temperature_plot.png")  # Saves the plot as an image
plt.show()

# (b) Arithmetic sequence
start = 5
difference = 3
terms = 8

sequence = [start + i * difference for i in range(terms)]
print("Arithmetic Sequence:", sequence)

# (c) Calculate volume under z = x^2 + y^2 over region 0 ≤ x,y ≤ 1
import numpy as np
from scipy import integrate

def surface_function(x, y):
    return x**2 + y**2

volume, _ = integrate.dblquad(surface_function, 0, 1, lambda x: 0, lambda x: 1)
print("Volume under surface z = x² + y² over 0 ≤ x,y ≤ 1:", volume)

# (d) Compiled vs Interpreted
"""
Compiled languages (e.g. C, C++) are converted into machine code before execution, which makes them faster.
Interpreted languages (e.g. Python) are run line-by-line using an interpreter, making development easier but slightly slower.
Python is an interpreted language.
"""
