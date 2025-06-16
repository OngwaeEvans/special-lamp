# surface_volume.py
# Calculate volume under the surface z = x^2 + y^2 over 0 ? x, y ? 1

from scipy import integrate

# Define the surface function
def surface_function(y, x):
    return x**2 + y**2

# Integrate over x = 0 to 1 and y = 0 to 1
volume, error = integrate.dblquad(surface_function, 0, 1, lambda x: 0, lambda x: 1)

# Output the result
print("Volume under surface z = x² + y² over 0 ? x, y ? 1:", volume)
