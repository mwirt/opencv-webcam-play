import cv2
import random


# set frame counter

count = 0


# I have two webcams, one is connected via usb and the other is built into the monitor.
# To create a loop by turning the camera on the monitor, you will need a webcam that is separate from the monitor.

cap = cv2.VideoCapture(0) # USB webcam


while(True):
    
    # Capture frame-by-frame
    
    ret, frame = cap.read()


    # Resize playback windows, width is desired new width
    
    width = 600 # change this number to desired width
    r = width / frame.shape[1]
    height = int(frame.shape[0] * r)
    dim = (width,height)
    
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    

    # Add effects
    
    blur = cv2.GaussianBlur(resized,(11,11),100)
    filt = cv2.bilateralFilter(blur,33,75,75)
    

    # convert to HSV from BGR
    
    hsv=cv2.cvtColor(filt, cv2.COLOR_BGR2HSV)
    

    # show the windows with the images

    cv2.imshow('orig', resized)
    cv2.imshow('result', hsv)


    # move windows so they don't overlap
    
    cv2.moveWindow('orig',0,0)
    cv2.moveWindow('result',width,0)
    

    # this will write a jpg every five frames from the result
        
    if count%5 == 0:
        cv2.imwrite('pics/opencv/capture%d.jpg'%(random.randint(1,10000000)),hsv)
        print('captured frame')
    

    count+=1


    # press 'q' to stop
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, this releases the capture

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)