#Mapping and Equalisation
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('cat.jpg', 0)
# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)
#for mapping
h=cv2.calcHist((img), [0], None, [256], [0,256])
h1=cv2.calcHist((equ), [0], None, [256], [0,256])
# stacking images side-by-side
res = np.hstack((img, equ))
# show image input vs output
cv2.imshow('image.jpg', res)
cv2.imshow('cat.jpg',img)
plt.plot(h)
plt.plot(h1)
plt.title("Histogram Mapping & Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.grid()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
