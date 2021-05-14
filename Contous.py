import cv2 as cv

img = cv.imread('Photos/cat.jpg')
#cv.imshow('cat',img)

#canny = cv.Canny(img,125,255,)
#cv.imshow('canny',canny)

#blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)
 
ret,trash = cv.threshold(img,125,255,cv.THRESH_BINARY)
cv.imshow('trash',trash)

contours, hierarchies = cv.findContours(trash,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.waitKey(0)