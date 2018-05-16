import cv2
import random

# set frame counter

count = 0

# I have two webcams, one is connected via usb and the other is built in.
# To create a loop by turning the camera on the monitor, you will need a peripheral webcam.

cap1 = cv2.VideoCapture(0) # USB webcam
cap2 = cv2.VideoCapture(1) # Built-in webcam


while(True):
    
    # Capture frame-by-frame
    
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Resize playback windows, width is desired new width
    
    width = 600 # change this number to desired width
    r = width / frame1.shape[1]
    height = int(frame1.shape[0] * r)
    dim = (width,height)
    
    resized1 = cv2.resize(frame1, dim, interpolation = cv2.INTER_AREA)
    resized2 = cv2.resize(frame2, dim, interpolation = cv2.INTER_AREA)
    
    # Add effects
    
    blur1 = cv2.GaussianBlur(resized1,(11,11),100)
    blur2 = cv2.GaussianBlur(resized2,(11,11),200)
    filt1 = cv2.bilateralFilter(blur1,33,75,75)
    filt2 = cv2.bilateralFilter(blur2,33,75,75)
    
    # convert to HSV from BGR
    
    hsv1=cv2.cvtColor(filt1, cv2.COLOR_BGR2HSV)
    hsv2=cv2.cvtColor(filt2, cv2.COLOR_BGR2HSV)
    
    # show the windows with the images

    cv2.imshow('orig1', resized1)
    cv2.imshow('result1', hsv1)
    
    cv2.imshow('orig2',resized2)
    cv2.imshow('result2',hsv2)
    
    # move windows so they don't overlap
    
    wh = (height+45)
    cv2.moveWindow('orig1',0,0)
    cv2.moveWindow('orig2',0,wh)
    cv2.moveWindow('result1',width,0)
    cv2.moveWindow('result2',width,wh)
    
    # write frames to jpg
    # this will write a jpg every five frames from each result
        
    if count%5 == 0:
        cv2.imwrite('pics/opencv/capture%d.jpg'%(random.randint(1,10000000)),hsv1)
        cv2.imwrite('pics/opencv/capture%d.jpg'%(random.randint(1,10000000)),hsv2)
        print('captured frame')
    
    count+=1

    # press 'q' to stop
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, this releases the capture

cap1.release()
cap2.release()
cv2.destroyAllWindows()
cv2.waitKey(1)