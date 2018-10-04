
import cv2  
  
img = cv2.imread('1_3.png')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_OTSU) 
  
Image,contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
color = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
cv2.drawContours(img,contours,-1,(0,0,255),1)  
  
cv2.imshow("img",img )  
cv2.waitKey(0)  