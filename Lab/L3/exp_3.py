# Exp 3: Create various types of plots/charts like histograms, plot based on sine/cosine function based on data from a matrix. 
# Further, lable different axes in a plot and data in a plot

import numpy as np
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-np.pi,np.pi,np.pi/40)
print(x)

mat = np.array([x, np.sin(x), np.cos(x)])
print(mat)

plt.plot(mat[0],mat[1], label="sin(x)")
plt.plot(mat[0],mat[2], label="cos(x)")

#Line Plot
plt.title("Line plot on Trigonometric Functions",fontsize='20')
plt.xlabel("Values of x"+r"$\rightarrow$")
plt.ylabel("Function values"+r"$\rightarrow$")
plt.axhline(y=0, color = "black")
plt.axvline(x=0, color = "black")
plt.legend()
plt.grid()

#Scatter Plot
plt.scatter(mat[0],mat[1], label="sin(x)")
plt.scatter(mat[0],mat[2], label="cos(x)")

plt.title("Scatter Plot on Trigonometric Functions",fontsize='20')
plt.xlabel("Values of x"+r"$\rightarrow$")
plt.ylabel("Function values"+r"$\rightarrow$")
plt.axhline(y=0, color = "black")
plt.axvline(x=0, color = "black")
plt.legend()
plt.grid()

#Box Plot
plt.boxplot([mat[0],mat[1],mat[2]], labels = ['x','sin(x)','cos(x)'])
plt.title("Box Plot",fontsize='20')
plt.xlabel("X"+r"$\rightarrow$")
plt.ylabel("Y"+r"$\rightarrow$")
plt.grid()


a = np.array(["A", "B", "C", "D"])
b = np.array([3, 8, 1, 10])
print(a)
print(b)

#Bar Graph
plt.bar(a,b, color='red')
plt.title('Bar Graph',fontsize='20')
plt.xlabel("Product Name"+r"$\rightarrow$")
plt.ylabel("Quantity"+r"$\rightarrow$")
plt.grid()

#Pie Chart
plt.figure(figsize=(6,6))
plt.pie(b, labels=a, autopct = "%1.1f%%",wedgeprops={'linewidth': 3.0, 'edgecolor': 'black'})
plt.title("Pie Chart",fontsize='20')

#Histogram
plt.hist(np.random.normal(23,19,22), color='green')
plt.title("Histogram",fontsize='20')
plt.xlabel("X"+r"$\rightarrow$")
plt.ylabel("Y"+r"$\rightarrow$")
plt.grid()
