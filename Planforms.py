# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

# Input parameters
S = 0.42
b_in = 2
taper_in = 0.4
sweep_in = 0.002
front_spar = 0.15
aft_spar = 0.7

# Calculate aspect ratio
A = b_in**2 / S

# Root chord definition from total surface area
c_root_in = 2*b_in / (A * (1 + taper_in))

# Chord definition at kink
c_tip_in = taper_in * c_root_in

# Calculate MAC
MACin = (b_in * c_root_in**2) / (3 * S) * (1 + taper_in + taper_in  **2)

# Location of the trailing edge at the root of the inner wing is the reference origin
xt_root_in = (0, 0)

def sweep_to_sweep(x_over_c_start, sweep_start, x_over_c_end):
    tan_sweep_end = tan(sweep_start) - 4 / A * (x_over_c_end - x_over_c_start) * (1 - taper_in) / (1 + taper_in)
    return atan(tan_sweep_end)

sweep_aft = sweep_to_sweep(front_spar, 0, aft_spar)
dX = tan(sweep_aft) * 0.2
dXdC = dX / c_root_in
print(aft_spar + dXdC)
print(degrees(sweep_aft))

# Prepare for coordinate lists
span = np.linspace(0,b_in/2,100)

LEx = []
LEy = []
TEx = []
TEy = []
xc4_x = []
xc4_y = []

MACS = 0
# Create coordinates
for y in span:
    if y < b_in:
        # Location of a point at distance y along the trailing edge of the inner wing
        xt_coor_in = (xt_root_in[0] + y * tan(sweep_in), xt_root_in[1] + y)
        
        # Chord at a distance y from the root of the inner wing
        c_y_in = c_root_in - (y/b_in * (c_root_in - c_tip_in))
        
        
        # Location of a point at distance y along the leading edge of the inner wing
        xl_coor_in = (xt_coor_in[0] - c_y_in, xt_coor_in[1])
        
        # Location of the quarter chord point at distance y from the root of the inner wing
        xc4_coor_in = (xt_coor_in[0] - 3/4 * c_y_in, xt_coor_in[1])
        
        # Append values to leading edge coordinates
        LEx.append(xl_coor_in[0])
        LEy.append(xl_coor_in[1])
        # Append values to trailing edge coordinates
        TEx.append(xt_coor_in[0])
        TEy.append(xt_coor_in[1])
        # Append values to quarter chord coordinates
        xc4_x.append(xc4_coor_in[0])
        xc4_y.append(xc4_coor_in[1])
        
# Plot wing planform and use trailing edge of root airfoil as reference        
plt.plot(LEx,LEy)
plt.plot(TEx,TEy)
plt.plot([LEx[-1],TEx[-1]],[LEy[-1],TEy[-1]])
plt.plot(xc4_x,xc4_y, 'r--')
plt.xlim(-0.7,0.7)
plt.show()