import matplotlib.pyplot as plt
import pydicom
import cv2
import numpy as np
# def loadFile(filename):
#     ds = sitk.ReadImage(filename)
#     img_array = sitk.GetArrayFromImage(ds)
#     frame_num, width, height = img_array.shape
#     return img_array, frame_num, width, height

dataset = pydicom.dcmread("D:\\文件\\毕设\\DICOM\\20171125\\12300000\\51783698")
filename="D:\\文件\\毕设\\DICOM\\20171125\\12300000\\51783698"
print()
print("Filename.........:", filename)
print("Storage type.....:", dataset.SOPClassUID)
print()

pat_name = dataset.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print("Patient's name...:", display_name)
print("Patient id.......:", dataset.PatientID)
print("Modality.........:", dataset.Modality)
print("Study Date.......:", dataset.StudyDate)

if 'PixelData' in dataset:
    rows = int(dataset.Rows)
    cols = int(dataset.Columns)
    print("Image size.......: {rows:d} x {cols:d}, {size:d} bytes".format(
        rows=rows, cols=cols, size=len(dataset.PixelData)))
    if 'PixelSpacing' in dataset:
        print("Pixel spacing....:", dataset.PixelSpacing)

# use .get() if not sure the item exists, and want a default value if missing
print("Slice location...:", dataset.get('SliceLocation', "(missing)"))

# plot the image using matplotlib
def limitedEqualize(img_array, limit = 4.0):
   img_array_list = []
   for img in img_array:
       clahe = cv2.createCLAHE(clipLimit = limit, tileGridSize = (8,8))
       img_array_list.append(clahe.apply(img))
   img_array_limited_equalized = np.array(img_array_list)
   return img_array_limited_equalized
pic = limitedEqualize(dataset.pixel_array)
# plt.figure('test')

# plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
# plt.show()

cv2.namedWindow("test")
cv2.imshow('test',pic)
cv2.waitKey(0)

cv2.imwrite('1.png',pic, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])


