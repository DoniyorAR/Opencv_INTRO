import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)


#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)   ### (3,3) -> ushbu narsa rasmning tiniqlik darajasini bildiradi
#cv.imshow('Blur',blur)

#canny = cv.Canny(img,135,175)
#cv.imshow('Edge shw',canny)

#dilated = cv.dilate(img,(7,7), iterations=3) # eroded ham yana bir xususiyat
#cv.imshow('dileted',dilated)

#resize
##cv.imshow('resizedr',resized)

#cropped = img[50:200,200:400]       ###-> qirqish
#cv.imshow('cropt',cropped)


cv.waitKey()