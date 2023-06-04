#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')  # or 'QtAgg' depending on your system
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

inertias=[]
for i in range(1,11):
 kmeans=KMeans(n_clusters=i)
 kmeans.fit(data)
 inertias.append(kmeans.inertia_)

plt.subplot(1,3,1)
plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
plt.subplot(1,2,1)
plt.scatter(x, y, c=kmeans.labels_)


classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(data,classes)
prediction=knn.predict(new_point)
plt.subplot(1,2,2)
plt.scatter(x+[new_x],y+[new_y], c=classes+ [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")

plt.show()
print(prediction)
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
