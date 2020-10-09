# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:01:09 2020

@author: sashank
"""
#haar cascade
import cv2
cap =cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier("E:/codinngblocks ml course/ML-stuff/knn/face recognition/haarcascade_frontalface_alt.xml")
while True:
        ret,frame = cap.read()
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
         
        if ret == False:
            continue
        faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
       
       # cv2.imshow("Gray Frame:",gray_frame)
  
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.imshow("Video Frame:",frame)  
        #wait for user input - q,then you will stop the loop
        key_pressed = cv2.waitKey(1) &0xFF#0xff 111111 8 1's 
        #cv2.waitkey is 32 bit int 
        if key_pressed == ord('q'):#ascii value
            break
cap.release()
cv2.destroyAllWindows()
#%%%
# =============================================================================
# # # Facial Recognition
# 
# # Generating selfie training data using webcam
# 
# # 1. Read video stream and capture images
# # 2. Detect faces and show bounding boxes over them
# # 3. Pick the largest face image, flatten it into a numpy array and store it
# # 4. Repeat for different faces. This forms the training data
# 
# =============================================================================
import cv2
import numpy
cap=cv2.VideoCapture(0)

#face detection
skip = 0
face_data = []
face_section[]
face_cascade = cv2.CascadeClassifier("E:/codinngblocks ml course/ML-stuff/knn/face recognition/haarcascade_frontalface_alt.xml")
while True:
    ret,frame = cap.read()
    
    if ret==False:
        continue
    
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   
    faces=face_cascade.detectMultiScale(frame,1.3,5)#second one is  scaling factor
    faces = sorted(faces,key=lambda f:f[2]*f[3])
   # print(faces)
   
    for face in faces[-1:]:#descending order
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        #extract (crop out of the required face) :region of Interest
        offset = 10
        face_section = frame [y-offset: y+h+offset,x-offset: x+w+offset]
        face_section = cv2.resize(face_section,(100,100))
        skip+=1
        if skip%10==0:
            face_data.append(face_section)
            print(len(face_data))
    
        
    cv2.imshow("Frame",frame)
    cv2.imshow("face section",face_section)
    #last parameter looks for the number of neighbours so increase in quality but lesser detections 
    #(it HASS to be THAT or else it wont detect)
     #store every 10th face
  #  if(skip%10==0):
        #stor the 10th face later on
    #    pass#used as a placeholder continue is different this does literally does nothing ,used for checking rest of the code
    
    key_pressed = cv2.waitKey(1)&0xFF#k capital
    if key_pressed== ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

