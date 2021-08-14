import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
import imutils

if __name__ == '__main__':
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cv2.startWindowThread()

    # open webcam video stream
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))
        
        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        pick = non_max_suppression(boxes, probs=None, overlapThresh=0.65)
        
        for (xA, yA, xB, yB) in pick:
            print(xA, yA, xB, yB)
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                            (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()

    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)