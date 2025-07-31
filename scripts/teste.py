import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,5,10)
y = np.cos(t)
print(t)
print(y)

plt.plot(t,y)
plt.show()