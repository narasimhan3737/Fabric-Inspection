import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('test1.jpg',0)
cap = cv2.VideoCapture(1) 
  
while(1): 
  
    # Take each frame 
    _, frame = cap.read()
    edges = cv2.Canny(frame,100,300)
    #plt.subplot(121),plt.imshow(frame,cmap = 'gray')
    #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot,plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

    
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
cv2.destroyAllWindows() 
  
#release the frame 
cap.release() 
