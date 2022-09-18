import numpy as np
import cv2
from util.analysis_realtime import analysis
import seaborn as sns
import matplotlib.pyplot as plt


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

    count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        result.write(frame)

        if ret:

            pred, bm = ana.detect_face(frame)
            print(pred)

            if pred == "You are highly engaged!":
                preds_graph.append(5)
            elif pred == "You are engaged.":
                preds_graph.append(4)
            else:
                preds_graph.append(2)
            
            cv2.imshow('Frame',frame)

            count += 30 # i.e. at 30 fps, this advances one second
            cap.set(cv2.CAP_PROP_POS_FRAMES, count)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:    
            cap.release()
            result.release()
            break
        
    _x = [i+1 for i in range(len(preds_graph))]
    # sns.lineplot(_x, preds_graph)
    # plt.savefig('../images/graph.png')
    

    cv2.destroyAllWindows()

    predictionPercentages = {'high': (preds_graph.count(5)/len(preds_graph)) * 100, 'good': (preds_graph.count(4)/len(preds_graph))*100, 'low': (preds_graph.count(2)/len(preds_graph))*100}
    
    return predictionPercentages

predValues = getVideoAndGraph()
print(predValues)