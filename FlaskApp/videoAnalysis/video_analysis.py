import numpy as np
import cv2
from util.analysis_realtime import analysis



def getVideoAndGraph():
    cap = cv2.VideoCapture('../video/test.mp4')
    ana = analysis()

    if (cap.isOpened() == False): 
        print("Error reading video file")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    size = (frame_width, frame_height)

    result = cv2.VideoWriter('../video/markedTest.mp4', 
                            cv2.VideoWriter_fourcc(*'MP4V'),
                            10, size)

    preds_graph = []

    while(cap.isOpened()):
        ret, frame = cap.read()
        result.write(frame)

        pred, bm = ana.detect_face(frame)
        preds_graph.append(pred)

        cv2.imshow('Frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    result.release()

    cv2.destroyAllWindows()

    return preds_graph