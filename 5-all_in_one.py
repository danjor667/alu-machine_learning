#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create a figure with a 3x2 grid

fig = plt.figure(figsize=(12, 10))
gs = GridSpec(3, 2, height_ratios=[1, 1, 2], width_ratios=[1, 1])


fig.suptitle('All in One', fontsize='x-large')

# dividing the grid for  each graph
ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])
ax3 = plt.subplot(gs[1, 0])
ax4 = plt.subplot(gs[1, 1])
ax5 = plt.subplot(gs[2, :])


# Plot 1: Line plot

ax1.plot(y0, color='red')
ax1.set_title('Line Plot', fontsize='x-small')
ax1.set_xlabel('X-axis', fontsize='x-small')
ax1.set_ylabel('Y-axis', fontsize='x-small')
ax1.legend(fontsize='x-small')

# Plot 2: Scatter plot

ax2.scatter(x1, y1, alpha=1, color='magenta')
ax2.set_title('Scatter Plot', fontsize='x-small')
ax2.set_xlabel('X-axis', fontsize='x-small')
ax2.set_ylabel('Y-axis', fontsize='x-small')

# Plot 3: Exponential decay

ax3.plot(x2, y2)
ax3.set_title('Exponential Decay of C-14', fontsize='x-small')
ax3.set_xlabel('Time (years)', fontsize='x-small')
ax3.set_ylabel('Fraction Remaining', fontsize='x-small')
ax3.set_yscale('log')
ax3.set_xlim(0, 28650)
ax3.legend(fontsize='x-small')

# Plot 4: Broken line plot

ax4.plot(x3, y31, linestyle='--', label='C-14', color="red")
ax4.plot(x3, y32, color="green", label='Ra-226')
ax4.set_title('Exponential Decay od Radioactive element', fontsize='x-small')
ax4.set_xlabel('Time (Years)', fontsize='x-small')
ax4.set_ylabel("Fration Remaining", fontsize='x-small')
ax4.legend(fontsize='x-small')

# Plot 5: Histogram of student grades

ax5.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
ax5.set_title('Project', fontsize='x-small')
ax5.set_xlabel('Grades', fontsize='x-small')
ax5.set_ylabel('Number of Students', fontsize='x-small')

# Adjust layout if needed

"""
plt.tight_layout(rect=[0, 0, 1, 0.95])
"""

# Show the plot
plt.show()
