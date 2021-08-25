#DIVYAM DUBEY 

import cv2

#Creating an object to load Haarcascade File 

face_cascade = cv2.CascadeClassifier("C:\\Users\\Divyam\\Documents\\haarcasscade_frontalface_default1.xml")

eye_cascade = cv2.CascadeClassifier("C:\\Users\\Divyam\\Documents\\haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret ,img1 = cap.read()

#Converting that image to Grey Scale

    img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

#Detecting the face

    faces = face_cascade.detectMultiScale(img1_gray, scaleFactor=1.1,minNeighbors=4)

#print(type(faces))
#print(faces)


#Showing a rectangle around the Image using a FOR loop

    for x,y,w,h in faces:
        img1 = cv2.rectangle(img1, (x,y), (x+w,y+h), (0,255,0),2)
        roi_gray = img1_gray[y:y+h, x:x+w]
        roi_color = img1[y:y+h ,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.09,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh),(255,0,0),1)



#Display the Image with detected face

    cv2.imshow("New",img1)
   
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()    
cv2.destroyAllWindows()