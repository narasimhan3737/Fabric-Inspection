print("Started")

import cv2
import numpy as np

print("Imported")

img1 = cv2.imread("2.jpg")

cap = cv2.VideoCapture(1)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
l=[]
while(True):
    _, frame = cap.read()
    kp2, des2 = orb.detectAndCompute(frame,None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    try:
        matches = bf.match(des1, des2)
        matches = sorted(matches, key = lambda x:x.distance)
        img3 = cv2.drawMatches(img1,kp1,frame,kp2, matches[:5], None, flags=2)
        cv2.imshow("match",img3)
        l.append(len(matches))
        print(len(matches))
    except:
        print("Shake Found!!!")
        break
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
s=0
for i in l:
    s+=i
if(len(l)==0):
    l.append(0)

print("\n\nAverage",s/len(l))
print("match1:",matches[0].distance)
pts = np.float([kp2[idx].pt for idx in range(0, len(kp2))]).reshape(-1, 1, 2)
x=0
y=0
w=1000
h=1000
for i in range(len(pts)):
    if(i%2!=0):
        if(pts[i].distance>x):
            x=pts[i].distance
        if(pts[i].distance<w):
            w=pts[i].distance
    else:
        if(pts[i].distance>y):
            y=pts[i].distance
        if(pts[i].distance<h):
            h=pts[i].distance
img=frame
x=int(x)
y=int(y)
w=int(w)
h=int(h)
try:
    col=(0,0,127)
    st=2
    endx=x+w
    endy=y+h
    cv2.rectangle(img,(w,h),(endx,endy),col,st)
    cv2.imshow("match",img)
except:
    print("Error")
cap.release()
#cv2.destroyAllWindows()
print("Ended")
