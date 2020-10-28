import matplotlib.pyplot as plt
import numpy as np

# Your code for generating the list of uniform random variables goes here
indices, random_variables = np.zeros(100), np.zeros(100)
  
# This will plot a graph showing your uniform random variables.
plt.plot( indices, random_variables, ".") 
plt.savefig("uniform_rvs.png")
