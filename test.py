import numpy as np
import cv2
from PIL import Image
import os
# coord = []
# for i in range(480):
#     temp = []
#     for j in range(640):
#         temp.append([i,j])
#     temp = np.array(temp)
#     coord.append(temp)
# coord = np.array(coord)
#
# img = cv2.imread('/Users/pro/Desktop/0054-001749-label.png', cv2.IMREAD_GRAYSCALE)
#
# gray_value = []
#
# for i in range(480):
#     for j in range(640):
#         if img[i][j] not in gray_value:
#             gray_value.append(img[i][j])
#
# thisgray = np.zeros((480,640), dtype=np.uint8)
# thisgray.fill(0)
# print(thisgray)
# pixels = coord[thisgray == img]
#
# print(pixels)

# emptyBoard = np.zeros((5, 5))
# print(emptyBoard)

# img_path = '/Users/pro/Desktop/Lab/Syndata/syndata-generation-11-3/crop_N5_348.jpg'
# img = cv2.imread(img_path)
# mask = np.zeros((img.shape[0], img.shape[1]))
# mask.fill(1)
# for i in range(len(img)):
    # for j in range(len(img[0])):
        # if img[i][j][0] > 0:
            # mask[i][j] = 0
# img = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))

# cv2.imwrite('test.png', img)


# a = cv2.imread("/Users/pro/desktop/test.png")
# print(a.shape)
# b = a[:,100:150]
# print(b.shape)
# cv2.imwrite("testout.png", b)

# l = os.listdir("/Users/pro/Desktop/")
# print(l)

a = [1,2,3,4,5,6,7,8,9]
b = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [6,7]]
less = lambda x: x[0]<5 and x[1]<5
b = list(filter(less, b))
print(b)
