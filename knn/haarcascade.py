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
