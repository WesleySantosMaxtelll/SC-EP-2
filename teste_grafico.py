import matplotlib.pyplot as plt
import numpy as np

# Generate data...
t = np.linspace(0, 2 * np.pi, 20)
print (t)
x = np.sin(t)
y = np.cos(t)
a = [0]
for _ in range(len(x)-1):
    a.append(int(not a[-1]))
plt.scatter(t,x,c=a)
plt.show()