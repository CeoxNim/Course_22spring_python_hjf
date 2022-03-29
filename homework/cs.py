import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-6,6,1201)
x=16*(np.sin(X))**3
y=13*np.cos(X)-5*np.cos(2*X)-2*np.cos(3*X)-np.cos(4*X)

plt.plot(x, y, color = 'r')
plt.xlim(-22,22)
# plt.savefig('心形函数')
plt.show()
