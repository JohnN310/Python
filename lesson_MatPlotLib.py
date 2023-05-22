#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.subplot(1,4,1)
plt.plot(x,y, ls=":",linewidth=2, marker="o", mec="blue", mfc="red")
plt.grid()
plt.title("Title1")


z = np.array([5,7,8,7,2,17,2,9,4,11,12])
k = np.array([99,86,87,88,111,86,103,87,94,78,77])
colors = np.array([0,10,20,30,40,50,60,70,80,90,100])

plt.subplot(1,4,2)
plt.scatter(z,k, c=colors, cmap='viridis')
plt.title("Title2")



a=np.random.normal(170,10,250)
plt.subplot(1,4,3)
plt.hist(a)
plt.title("HIstogram")


b=np.array([75,15,10])
colors1=np.array(["brown","green","blue"])
mylabels=["Food","Drinks","Exercise"]
plt.subplot(1,4,4)
plt.pie(b,colors=colors1, labels=mylabels, shadow=True, explode=[0,0.2,0])
plt.legend(title="My daily routine")


plt.suptitle("SuperTitle")
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
