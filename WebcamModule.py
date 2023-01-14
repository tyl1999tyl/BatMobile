import cv2
import utils

cap = cv2.VideoCapture(0)
 
def getImg(display= False,size=[640,480]):
    
    intialTrackbarVals = [137,0,100,240]
    utils.initializeTrackbars(intialTrackbarVals)

    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    img = cv2.flip(img, 0)
    if display:
        cv2.imshow('IMG',img)
    return img
 
if __name__ == '__main__':
    while True:
        img = getImg(True)
