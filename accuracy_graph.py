## -*- coding: utf-8 -*-
#
#import numpy as np
#import matplotlib.pyplot as plt
#data = [[10, 20, 14],
#[18, 26, 20],
#[37.23, 34.65, 35.89]]
#X = np.arange(3)
#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
#ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
#ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
#

import matplotlib.pyplot as plt
import numpy as np


labels = ['Obs1', 'Obs2', 'Obs3','Obs4']
#b1 = [10, 20, 14]
#b2 = [18, 26, 20]
#b3=[37.23, 34.65, 35.89]

b1 = [10, 18, 37.23,34.23]
b2 = [20, 26, 34.65,40.86]
b3=[14, 40, 35.89,37.25]




x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, b1, width, label='Precison')
rects2 = ax.bar(x + width/2, b2, width, label='Recall')
rects3 = ax.bar(x + 3*width/2, b3, width, label='F-score')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores in each observation')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


fig.tight_layout()

plt.show()





#
#
## libraries
#import numpy as np
#import matplotlib.pyplot as plt
#
## set width of bar
#barWidth = 0.25
#
## set height of bar
#bars1 = [10, 18, 37.23]
#bars2 = [20, 26, 34.65]
#bars3 =[14, 40, 35.89]
#
## Set position of bar on X axis
#r1 = np.arange(len(bars1))
#r2 = [x + barWidth for x in r1]
#r3 = [x + barWidth for x in r2]
#
## Make the plot
#plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Precison')
#plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Recall')
#plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='F-score')
#
## Add xticks on the middle of the group bars
#plt.xlabel('Observations', fontweight='bold')
#plt.xticks([r + barWidth for r in range(len(bars1))], ['obs1','obs2','obs3'])
#
## Create legend & Show graphic
#plt.legend()
#plt.show()
#
#
#def autolabel(rects):
#    """Attach a text label above each bar in *rects*, displaying its height."""
#    for rect in rects:
#        height = rect.get_height()
#        ax.annotate('{}'.format(height),
#                    xy=(rect.get_x() + rect.get_width() / 2, height),
#                    xytext=(0, 3),  # 3 points vertical offset
#                    textcoords="offset points",
#                    ha='center', va='bottom')
#
#
#autolabel(r1)
#autolabel(r2)
#autolabel(r3)


















