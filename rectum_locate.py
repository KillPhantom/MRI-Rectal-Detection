import os 
import numpy
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import cv2


global img 
global point1,point2

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
        



def rgb2gray(rgb):
   return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


path = os.getcwd() +'\\test3'
data = np.empty((30,649,1105))

for root,dirs,files in os.walk(path):
	for i in range(len(files)):
 		if(files[i][-3:]=='jpg'):
 			file_path = root+'\\'+files[i]
 			print(file_path)
 			temp = rgb2gray(mpimg.imread(file_path))
 			data[i,:,:] = temp


def main():
	global img

	img = cv2.imread('20.jpg')
	cv2.namedWindow('image')
	cv2.setMouseCallback('image', on_mouse)
	cv2.imshow('image',img)
	cv2.waitKey(0)

	plt.imshow(data[19,min_y:min_y+height, min_x:min_x+width],cmap = plt.cm.gray)
	plt.axis('on')
	plt.show()

if __name__ == '__main__':
    main()



# cv2.namedWindow('image', cv2.WINDOW_NORMAL)#
# cv2.imshow('image',data[1,:,:])#展示图片
# cv2.waitKey(0)#等待按键按下
# cv2.destroyAllWindows()#清除所有窗口


