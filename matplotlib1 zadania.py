import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
# Zad 1, 2
x = np.arange(20,40,1)
y = (1/x)
plt.plot(x,y, 'b--o')
plt.ylim(0.02,0.05)
plt.xlim(20,40)
plt.xlabel("x")
plt.ylabel("1/x")
plt.title("Wykres funkcji f(x) = 1/x dla x ϵ [20, 40]")
plt.show()
'''
'''
# zad 3
x1 = np.arange(0.45, 2.0, 0.01)
x2 = np.arange(0.45, 2.0, 0.01)
y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'b-', label="sin(x)")
plt.title('Wykres funkcji sin(x) oraz cos(x) dla x ϵ [0, 45] z krokiem 0.1')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r-', label="cos(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
'''
'''
# zad 4
x1 = np.arange(-1, 40.0, 0.89)
x2 = np.arange(-1, 40.0, 0.89)
y1 = np.sin(2 * np.pi * x1)
y2 = np.cos((2 * np.pi * x2)+1.67)
plt.plot(x1, y1, 'b-', label="sin(x)")
plt.plot(x2, y2+2, 'r-', label="sin(x)")
plt.title('Wykres funkcji sin(x), sin(x) ')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
'''