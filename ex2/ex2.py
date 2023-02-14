#Ex2 Converting Between Color-spaces
import cv2
image = cv2.imread("colorspace.png")
# converting BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
# converting BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
