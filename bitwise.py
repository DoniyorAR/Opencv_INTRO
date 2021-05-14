import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(350,370),255,thickness=-1)
circle = cv.circle(blank.copy(),(200,200),200,255,thickness=-1)

#cv.imshow('rec',rectangle)
#cv.imshow('cic',circle)

#rasmlarni qoshish
#bitwise_and = cv.bitwise_and(rectangle,circle)
#cv.imshow('bitwise and',bitwise_and)

#rasmlarni ayrish
#bitwise_or = cv.bitwise_or(rectangle,circle)
#cv.imshow('bitwise or',bitwise_or)

#bitwise xor -> kesishmagan qimi olinadi
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise xor',bitwise_xor)

# biwise not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('circle not',bitwise_not)

cv.waitKey(0)
