import cv2
import utils

cap = cv2.VideoCapture('video.h264')
 
def getImg(display= False,size=[480,240]):

    
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    img = cv2.flip(img, 0)

    if display:
        cv2.imshow('IMG',img)
    return img
 
if __name__ == '__main__':

   
    while True:
        img = getImg(True)
