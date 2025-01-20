# Name of the file: demo_cv.py
# In this file, we want to be able to have our basics on 
# OpenCV more clear. This file is for any beginners who want
# to implement this project but are unsure on how to begin. 

import cv2 

image = cv2.imread("python.gif") 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("This is processed image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()