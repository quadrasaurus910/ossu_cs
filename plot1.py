import matplotlib.pyplot as plt
import numpy as np

# pylab has been discontinued
# pylab.figure(1)
# pylab.plot([1,2,3,4], [1,7,3,5])
# pylab.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y)
plt.show()