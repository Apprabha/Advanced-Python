from sklearn.cluster import k_means, KMeans
import numpy as np
x=np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0],[1,5],[2,7],[3,6],[4,8],[5,9]])
model=KMeans(n_clusters=3, random_state=42)
model.fit(x)
print(model.labels_)

