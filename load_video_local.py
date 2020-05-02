import numpy as np
import cv2
from IBM import Model
from bounding_box import bounding_box as bb

api_key = " "
model_id = " "

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #salvando frame
    cv2.imwrite("frame.jpg", frame)     # save frame as JPEG file
    # Our operations on the frame come here
    # Load Model
    clf = Model("frame.jpg",api_key=api_key,model_id=model_id)
    result = clf.label_predict()
    #'left': 265, 'top': 297, 'width': 161, 'height': 181
    for detect in result:
        label = detect['object']
        left = detect['location']['left']
        top = detect['location']['top']
        width = detect['location']['width']
        height = detect['location']['height']
        if label ==  "Sem_Mascara":
          bb.add(frame, left, top, left+width, top+height, label, "red")
        if label ==  "Errado_Mascara":
          bb.add(frame, left, top, left+width, top+height, label, "purple")
        if label ==  "Com_Mascara":
          bb.add(frame, left, top, left+width, top+height, label, "purple")
    cv2.imshow('frame',frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
