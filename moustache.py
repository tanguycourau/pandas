import numpy as np
import matplotlib
matplotlib.interactive(False)
from matplotlib import pyplot as plt


print('serie', np.arange(9), 'quartiles', np.quantile(np.arange(9),
                                                      [0,0.25,0.5,0.75,1] ))
a = np.array([1, 2, 3, 4, 6, 11])
b = np.quantile(a, [0.25,0.5,0.75])
w = (b[2]-b[0])*1.5
plt.boxplot(a)
plt.ylim(-3, 12)
plt.grid()
plt.text(1.15 ,b[0], 'Q1', verticalalignment='center')
plt.text(1.15 ,b[1], 'Median', verticalalignment='center')
plt.text(1.15 ,b[2], 'Q3', verticalalignment='center')
plt.text(1.15 ,a.max(), 'max', verticalalignment='center')
plt.text(1.15, a.min(), 'min included in w', verticalalignment='center')
plt.text(1.15, a[4], 'max included in w', verticalalignment='center')
plt.text(1.15, b[2]+w, 'wmax=%g'%(b[2]+w), verticalalignment='center')
plt.text(1.15, b[0]-w, 'wmin=%g'%(b[0]-w), verticalalignment='center')
plt.plot(np.ones(a.size)/1.2, a, '+')
#plt.show()

