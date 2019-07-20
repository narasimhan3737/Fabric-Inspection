import cv2
import numpy as np
import pandas as pd
from PIL import Image
#import op

def findpoints(l):
    l=list(l)
    x=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if((l[i][j]==255)or(l[i][j]==1)):
                x.append([i,j])
    return x

def find(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if(l[i][j]>=50):
                l[i][j]=255
    return l

def mean(l):
    mx=0
    my=0
    n=len(l)
    for i in l:
        mx+=i[0]
        my+=i[1]


    return (int(mx/n),int(my/n),n)



img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")

w=250
h=300

while(1):
    img1b = cv2.Canny(img1,w,h)
    img2b = cv2.Canny(img2,w,h)

    img3 =img1b-img2b
    img3=cv2.GaussianBlur(img3,(9,9),cv2.BORDER_DEFAULT)
    img3=find(np.array(img3))
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
x,y,n=mean(l)
cv2.circle(img1,(y,x),int(n/2),(0,0,125),2)
cv2.imshow("match",img1)
