import cv2
import numpy as np
import pandas as pd
from PIL import Image
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
#import op

def findpoints(l):
    l=list(l)
    x=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if((l[i][j]==255)or(l[i][j]==1)):
                x.append([i,j])
    return x

def maximin(l):
    Mx=l[0][0]
    mx=l[0][1]
    My=Mx
    my=mx
    h=int(len(l)/2)
    for i in range(len(l)):
            if(l[i][0]>Mx):
                Mx=l[i][0]
            if(l[i][0]<mx):
                mx=l[i][0]
            if(l[i][1]>My):
                My=l[i][1]
            if(l[i][1]<my):
                my=l[i][1]

    return (Mx,My,mx,my)


img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")

w=250
h=300

while(1):
    img1b = cv2.Canny(img1,w,h)
    img2b = cv2.Canny(img2,w,h)

    img3 =img1b-img2b
    #img3=cv2.GaussianBlur(img3,(9,5),cv2.BORDER_DEFAULT)
    cv2.imshow("match",img3)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == 43:
        w+=1

    elif k == 45:
        w-=1
        
    elif k == 42:
        h+=1

    elif k == 47:
        h-=1
print(w)
print(h)
#print(np.array(img3))
np.savetxt("value.csv",np.array(img3),delimiter=",")
f = pd.read_csv("value.csv")
dup=np.array(img3)
l=findpoints(dup)
#print(l)
cl = l
cl = StandardScaler().fit_transform(cl)
dbscan = DBSCAN(eps = 3,min_samples = 2)
model = dbscan.fit(cl)
labels = model.labels_
core_samples =  np.zeros_like(labels,dtype = bool)
core_samples[dbscan.core_sample_indices_] = True
print(core_samples)
n_clusters_ = len(set(labels)) - (l if -l in labels else 0)
n_clusters_
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X,labels))
