#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

x_train=x[:80]
y_train=y[:80]


mymodel = numpy.poly1d(numpy.polyfit(x_train, y_train, 3))

myline = numpy.linspace(1, 22, 100)

plt.subplot(1,2,1)
plt.scatter(x_train, y_train)
plt.plot(myline,mymodel(myline))
plt.title("Poly Train")
print(r2_score(y_train, mymodel(x_train)))




x_test=x[80:]
y_test=y[80:]

slope, intercept, r, p, std_err = stats.linregress(x_test, y_test)

def myfunc(x_test):
  return slope * x_test + intercept

mymodel2= list(map(myfunc, x_test))

plt.subplot(1,2,2)
plt.scatter(x_test, y_test)
plt.plot(x_test, mymodel2)
plt.title("Linear Test")
print(r)

plt.suptitle("Train/Test Graph")
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
