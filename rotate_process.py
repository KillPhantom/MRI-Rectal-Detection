from PIL import Image

count=0
for i in range(112,148):
	img=Image.open('1_%d.png' %i)
	img = img.resize((256,256))
	im_rotate = img.transpose(Image.FLIP_LEFT_RIGHT)
#	im_rotate = img.rotate(270)
	count +=1
	temp = 257+count
	im_rotate.save('1_%d.png' %temp)
