# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 23:43:09 2025

@author: CHANDRU DEIVANAYAGAN
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#IMPORT THE LIBRRAIES
import cv2
import numpy as np
#LOAD THE DATA OR IMAGE
img = cv2.imread(r"C:\Users\CHANDRU DEIVANAYAGAN\OneDrive\Desktop\CV\J1.jpg")

cv2.imshow("My_Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
-----------------------------------------------------------------------
#RGB CONVERT TO GREY

grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("My_Image",grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
---------------------------------------------------------------------
#RESIZE THE IMAGE

resize_img = cv2.resize(img, (250,250))
cv2.imshow("My_Image",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
----------------------------------------------------------------------------------
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
-------------------------------------------------------
#CROPPING
crop_img = img[12:200]
cv2.imshow("My_Image",crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
--------------------------------------------------
crop_img = img[12:200,15:100]
cv2.imshow("My_Image",crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
--------------------------------------------------
#WRITING
cv2.imwrite("Output_2025.jpg",crop_img)
--------------------------------------------------------
#FILTER
blurred_img = cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("My_Image",blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

---------------------------------------------------------------------
#Image Sharpening
kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpen_img = cv2.filter2D(img, -1, kernel)
------------------------------------------------------------
#CANNY EDGE DETECTION
edges = cv2.Canny(img,100,200)
cv2.imshow("My_Image",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
-------------------------------------------------------------------------------
#FLIP OPERATION
center = (width/2,height/2)
Angle_90 = 90
Angle_180 = 180
Angle_270 = 270
scale=1.0
#1----------------------------------------------------------------------
x=cv2.getRotationMatrix2D(center, Angle_90, scale)

Img_90 =cv2.warpAffine(img,x, (height,width))

cv2.imshow("My_Image",Img_90)
cv2.waitKey(0)
cv2.destroyAllWindows()
#2 ---------------------------------------------------------
x=cv2.getRotationMatrix2D(center, Angle_180, scale)

Img_180 =cv2.warpAffine(img,x, (height,width))

cv2.imshow("My_Image",Img_180)
cv2.waitKey(0)
cv2.destroyAllWindows()
#3-------------------------------------------------------------------
x=cv2.getRotationMatrix2D(center, Angle_270, scale)

Img_270 =cv2.warpAffine(img,x, (height,width))

cv2.imshow("My_Image",Img_270)
cv2.waitKey(0)
cv2.destroyAllWindows()