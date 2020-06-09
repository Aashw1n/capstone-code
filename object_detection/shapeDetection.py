# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Aashwin Ranjan 
#3/2/20

import torch 
import cv2 
import numpy as np

img = cv2.imread("RAVEN_NEW_000401.png", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    



for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    
#Displaying Everything on the screen
cv2.imshow("Shapes",img)
cv2.imshow("Threshold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()