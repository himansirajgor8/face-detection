import cv2
from random import randrange as p
traindataset=cv2.CascadeClassifier('face.xml')

webcam=cv2.VideoCapture(0)
while True:
  sy,fram=webcam.read()



# Correct file path
#imag_path = r"D:\face\img\img.jpg"

# Load image
#img = cv2.imread(imag_path)
  geaying=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)

  facecoordinates=traindataset.detectMultiScale(geaying)
  for x,y,w,h in facecoordinates:
    cv2.rectangle(fram,(x,y),(x+w,y+h),(p(0,256),p(0,256),p(0,256)),2)
    
#x,y,w,h=facecoordinates[0]

# Check if image is loaded properly

    # Show the image
  cv2.imshow('singal',fram)
  key=cv2.waitKey(1)
  if(key==81 or key==113):
   break 
webcam.release()
print("end")
  