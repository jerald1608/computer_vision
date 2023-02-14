#Converting 24bit image to 8bit, 4bit, 1bit

import cv2
#Input image
input = cv2.imread('parrot.jpg')
#Get input size
height, width = input.shape[:2]
cv2.imshow("parrot.jpg",input)

#24 Bit to 8 Bit
w, h = (256, 256)
temp = cv2.resize(input, (w, h), cv2.INTER_LINEAR) 
output1 = cv2.resize(temp, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("parrot_8.jpg",output1)

#24 Bit to 4 Bit
a, b = (16, 16)
temp1 = cv2.resize(input, (a, b), cv2.INTER_LINEAR) 
output2 = cv2.resize(temp1, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("parrot_4.jpg",output2)

#24 Bit to 1 Bit
c, d = (2, 2)
temp2 = cv2.resize(input, (c, d), cv2.INTER_LINEAR) 
output3 = cv2.resize(temp2, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("parrot_1.jpg",output3)
