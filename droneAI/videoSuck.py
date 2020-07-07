import cv2
import numpy as np


vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()

    if not ret:
        print("uh oh")
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(blurred, 50, 150)
    


    

    grayscaleFrame = np.dot(frame[...,:3], [0.2989, 0.5870, 0.1140])
    cv2.imshow('frame',edged)


    # print(np.shape(frame))
    # print(np.shape(grayscaleFrame))
    print(grayscaleFrame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break
    
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 