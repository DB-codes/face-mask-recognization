import cv2
import uuid
#used to create a unique identifier for each image taken
capture= cv2.VideoCapture(0) #selecting our capture device iewebcam
w=int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))#extracting
width of image from webcam
h=int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))#extracting
height of image from webcam
while True:
 ret, frame = capture.read() #capture and read
 image = 'C:/Users/prash/Documents/C.S
Project/Mask/{}.jpg'.format(str(uuid.uuid1())) #path the file is
to be saved
 cv2.imwrite(image, frame)#writing it to the file
 cv2.imshow('frame', frame)#showing the frame
 if cv2.waitKey(1) & 0xFF == ord('q'): #wait key to quit out of
the capture device
 break
