import numpy as np
>>> import pandas as pd
>>> import matplotlib as mpl
>>> import seaborn as sns
>>> m-c-p = [100, 100, 27.08, 100]
SyntaxError: cannot assign to operator
>>> mcp = [100, 100, 27.08, 100]
>>> madultp = [32.5, 8.33, 16.23, 22.27]
>>> fcp = [100, 100, 45.1, 100]
>>> fadultp = [97.2, 86.02, 46.06, 86.9]
>>> fig = plt.figure()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fig = plt.figure()
NameError: name 'plt' is not defined
>>> fig = plt.figure()
plt.plot(years, gdp, color='black', marker='o', linestyle='dash')
SyntaxError: multiple statements found while compiling a single statement
>>> fig = plt.figure()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fig = plt.figure()
NameError: name 'plt' is not defined
>>> import matplotlib.pyplot as plt

>>> import matplotlib.pyplot as plt
>>> fig = plt.figure()
>>> plt.plot(years, gdp, color='black', marker='o', linestyle='dash')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module
    plt.plot(grade, mcp, color='black', marker='o', linestyle='dash')
NameError: name 'years' is not defined
>>> grade = [1, 2, 3, 4]
ValueError: 'dash' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
>>> plt.plot(grade, mcp, color='black', marker='o', linestyle='dashed')
[<matplotlib.lines.Line2D object at 0x0000022EC2015070>]
>>> plt.show()
>>> fig = plt.figure()
>>> plt.plot(grade, madultp, color='black', marker='o', linestyle='dashed')
[<matplotlib.lines.Line2D object at 0x0000022EC7A77F10>]
>>> plt.show()
>>> fig = plt.figure()
>>> plt.plot(grade, fcp, color='black', marker='o', linestyle='dashed')
[<matplotlib.lines.Line2D object at 0x0000022EC7C14C10>]
>>> fig = plt.figure()
>>> plt.plot(grade, fadultp, color='black', marker='o', linestyle='dashed')
[<matplotlib.lines.Line2D object at 0x0000022EC3D866D0>]
>>> plt.show()
>>> import matplotlib.pyplot as plt
>>> from mpl_toolkits.mplot3d import Axes3D
>>> from matplotlib import cm
>>> fig = plt.figure()

