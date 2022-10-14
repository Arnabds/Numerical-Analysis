# Lab 2 , exercise 2
# A sample scriptfile.
# Arnab Dey Sarkar and 09.07.2022
import numpy as np
import matplotlib.pyplot as plt
meshPoints = np.linspace(-1, 1 , 1000) 
plt.plot(meshPoints, np.sin(2*np.pi*meshPoints))
plt.show ()