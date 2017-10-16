import cv2
import numpy as np
img = cv2.imread('1.png',cv2.IMREAD_UNCHANGED)
img = np.array(img,uint8)
cv2.imwrite('1.jpg', img)
