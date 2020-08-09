import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img  = cv.imread('watch.jpg',cv.IMREAD_GRAYSCALE)

cv.imshow('image',img)



# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  #hide x and y axis
# plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
# plt.show()

cv.imwrite('watch.jpg',img)