import numpy as np
import cv2
from util.analysis_realtime import analysis

cap = cv2.VideoCapture('../video/test.mp4')
ana = analysis()

while(cap.isOpened()):
    ret, frame = cap.read()

    bm = ana.detect_face(frame)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()