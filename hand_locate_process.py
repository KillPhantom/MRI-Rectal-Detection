import os
import cv2
import numpy as np 
from matplotlib import pyplot as plt  


def on_mouse(event,x,y,flags,param):
	global img, point1, point2,min_x,min_y,height,width
	img2 = img.copy()
	if event == cv2.EVENT_LBUTTONDOWN:
		point1 = (x,y)
		cv2.circle(img2, point1, 10, (0,255,0), 5)
		cv2.imshow('image', img2)
	elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
		cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
		cv2.imshow('image', img2)
	elif event == cv2.EVENT_LBUTTONUP:
		point2 = (x,y)
		cv2.rectangle(img2, point1, point2, (0,0,255), 5)
		cv2.imshow('image', img2)
		min_x = min(point1[0],point2[0])     
		min_y = min(point1[1],point2[1])
		width = abs(point1[0] - point2[0])
		height = abs(point1[1] -point2[1])
		cut_img = img[min_y:min_y+height, min_x:min_x+width]


def main():
	global img
count = 0
root_path = os.getcwd()
for filename in os.listdir(root_path):
	if(filename[-3:]=='jpg'):
		img = cv2.imread(filename)
		cv2.namedWindow('image')
		cv2.setMouseCallback('image', on_mouse)
		cv2.imshow('image',img)
		cv2.waitKey(0)	

		roiImg=img[min_y:min_y+height, min_x:min_x+width]
		plt.imshow(roiImg,cmap = plt.cm.gray)
		plt.axis('on')
		plt.show()
		count+=1
		cv2.imwrite('1_%d.png' %count,roiImg)  

		cv2.waitKey(0)#等待按键按下
		cv2.destroyAllWindows()#清除所有窗口

	



if __name__ == '__main__':
    main()        


# test = cv2.imread('qiuyaocai10.jpg')

# cv2.imwrite('test.png',roiImg)
# plt.imshow(test,'gray')

# plt.show()

# roiImg = test[470:600,330:500]





# root_path = os.getcwd()
# count = 0
# for filename in os.listdir(root_path):
# 	srcImg = cv2.imread(filename)
# #	srcImg = cv2.cvtColor(srcImg,cv2.COLOR_RGB2GRAY)
# 	roiImg = srcImg[490:620,330:500]
# 	count +=1
# 	cv2.imwrite('1_%d.png' %count,roiImg)  
# 	print(count)
