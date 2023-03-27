# import the necessary packages
import cv2
import numpy as np

# read the image
img = cv2.imread('capture.png', 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]


# define the kernel
kernel = np.ones((5, 5), np.uint8)

# invert the image
invert = cv2.bitwise_not(binr)

cv2.imshow('Original image',img)
#cv2.waitkey()
#cv2.destroyAllWindows()

# erode the image
erosion = cv2.erode(invert, kernel,iterations=1)
cv2.imshow('Eroded image',erosion)
#cv2.waitKey()
#cv2.destroyAllWindows()

dilation = cv2.dilate(invert, kernel, iterations=1)
cv2.imshow('Dilated image',dilation)
#cv2.waitKey()
#cv2.destroyAllWindows()

opening = cv2.morphologyEx(binr, cv2.MORPH_OPEN,kernel, iterations=1)
cv2.imshow('Opened image',opening)
#cv2.waitKey()
#cv2.destroyAllWindows()

closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('Closed image',closing)
cv2.waitKey()
cv2.destroyAllWindows()
