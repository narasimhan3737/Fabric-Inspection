import cv2
import numpy as np

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
print(np.array(img3))
f=open("val.txt","a")
for i in np.array(img3):
    s=""
    for j in i:
        s=str(j)+" "
    s+="\n"
    f.write(s)
f.close()
cv2.destroyAllWindows()
