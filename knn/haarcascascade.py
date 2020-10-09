# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 04:25:07 2020

@author: sashank
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 03:38:23 2020

@author: sashankrm
"""

import cv2
import numpy
cap=cv2.VideoCapture(0)
#face detection
skip=0
face_data=[]
face_cascade= cv2.CascadeClassifier("E:/codinngblocks ml course/ML-stuff/knn/face recognition/haarcascade_frontalface_alt.xml")
dataset_path= 'E:/codinngblocks ml course/ML-stuff/knn'
file_name= input("enter the name of the person:")
while True:
        ret,frame = cap.read()
        
        if ret==False:
            continue
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
        faces=face_cascade.detectMultiScale(frame,1.3,5)
        faces = sorted(faces,key=lambda f:f[2]*f[3],reverse=True)
        face_section_list = []
        print(faces)
        #pick the largest face where Area is giben by f[2]*f[3]
        for face in faces:
                x,y,w,h = face
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
                
                #exctract region of interst required face
                offset=10
                face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
                face_section=cv2.resize(face_section,(100,100))
                face_section_list.append(face_section)
                skip+=1
                if(skip%10==0):
                    face_data.append(face_section)
                    print(len(face_data))
        
        
        cv2.imshow("Frame",frame)
       # cv2.imshow("face section",face_section)
        for im in face_section_list:
            cv2.imshow("Face section",im)
            
            key_pressed=cv2.waitKey(1)&0xFF
            if key_pressed == ord('q'):
                    break

face_data=np.asarray(face_data)#convert face_data to numpy array
face_data = face_data.reshape((face_data.shape[0],-1))#making a 1d array ,-1 says itll figure it out
#no of rows =no of faces
print(face_data.shape)

#save this data into file system
np.save(dataset_path+file_name+'.npy',face_data)
print("data succesfully saved at "+dataset_path+file_name+'.npy')
cap.release()
cv2.destroyAllWindows()