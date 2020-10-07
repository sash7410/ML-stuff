# =============================================================================
# # Facial Recognition
# 
# # Generating selfie training data using webcam
# 
# # 1. Read video stream and capture images
# # 2. Detect faces and show bounding boxes over them
# # 3. Pick the largest face image, flatten it into a numpy array and store it
# # 4. Repeat for different faces. This forms the training data
# =============================================================================

import cv2 as cv
import numpy as np

# Initialize camera
cap = cv.VideoCapture(0)

# Face detection (using Haar cascade classifier)
face_cascade = cv.CascadeClassifier("D:/Python/Downloaded files/haarcascade_frontalface_alt.xml")

skip = 0
face_data = []
dataset_path = "D:/Python/Facial recognition/Data/"

file_name = input("Enter the name of the person :")

while True:
    ret,frame = cap.read()
    
    if ret == False:
        continue
    
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        
    #face detection
    #faces is a list of faces. each face is a tuple of (x,y,w,h)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    
    
    #Sorting to store only largest face if image has multiple faces
    #in the tuple (x,y,w,h) w and h are the sorting keys
    #largest face is largest area which is w * h
    
    faces = sorted(faces, key = lambda f:f[2]*f[3])
    
    
    #Creating bounding boxes around faces
    #Pick the last face because its the largest (ascending sort)
    #faces[-1: ] = last element in list and all tuples in that element
    for face in faces[-1:]:
        x,y,w,h = faces
        cv.rectange(frame, (x,y), (x+w, y+h), (0,255,255), 2)
        
    #Extracting region of interest (cropping only face part of the image)
    #Offset= 10 around bounding box for some tolerance
    #Slicing is done in y axis,a axis order 
    
    offset = 10
    face_section = frame [y-offset: y+h+offset, x-offset: x+w+offset]
    face_section = cv.resize(face_section, (100,100))
    

    
    #Storing every 10th face (every 10th frame itll store a face)
    skip += 1
    if (skip%10 == 0):
        face_data.append(face_section)
        #length of face data gives how many images are stored
        print (len(face_data))
        
    
    
    cv.imshow("Frame", frame)
    cv.imshow("Face section",face_section)
    

    

    key_pressed = cv.waitKey(1) & 0xff
    if key_pressed == ord ('q'):
        break
    
# Convert face list into a numpy array
face_data = np.asarray(face_data)
#Number of rows is no of faces, no of columns is automatic
face_data = face_data.reshape((face_data.shape[0]),-1)
print (face_data.shape)

#Save this data as numpy files
#parameters: path + file name + extension, what data to save

np.save(dataset_path + file_name+'.npy',face_data)

cap.release()
cv.destroyAllWindows()











