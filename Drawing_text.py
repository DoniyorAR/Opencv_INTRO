import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype='uint8')
cv.rectangle(blank,(50,50),(250,250),(255,100,100),thickness=cv.FILLED)
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,0,250),thickness=cv.FILLED)
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('Line', blank)

#write text
cv.putText(blank,'Hello',(225,225),cv.FONT_ITALIC,1.0,(0,255,0),2)
cv.imshow('Text', blank)
cv.waitKey(0)