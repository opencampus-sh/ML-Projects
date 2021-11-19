import time
import cv2 as cv
import numpy as np

import imutils
from imutils.video import FPS

# Get Prediction OpenCV
def get_video_inference(net, input_vid_path="io/sample.mp4", output_vid_path="io/yolo_output.avi", confidence_threshold=0.5, iou_threshold=0.3, write_output=False, show_display=True, labels = None):
    
    np.random.seed(111)
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

    # get layers
    ln = net.getLayerNames()
    ln =[ln[i[0]-1] for i in net.getUnconnectedOutLayers()]

    cap = cv.VideoCapture(input_vid_path)

    # if ! not read frame
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
        return
    
    (success, frame) = cap.read()
    # frame = imutils.resize(frame, width=640)

    # Write video file
    if write_output:
        out = cv.VideoWriter( output_vid_path
                            , cv.VideoWriter_fourcc(*"MJPG")
                            , cap.get(cv.CAP_PROP_FPS)
                            , (frame.shape[1]
                            , frame.shape[0])
                            , True)

    # Start FPS Measurement
    fps = FPS().start()

    while success:
        
        # read height and width
        (H, W) = frame.shape[:2]

        # Normalize, Scale and Reshape image to blob darknet input
        blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        # get feed forward output and time taken
        start = time.perf_counter()
        layer_outputs = net.forward(ln)
        time_taken = time.perf_counter() - start
        print(f'>> Inference Time per Frame : {time_taken:.2f}s')

        # prediction accumulators
        boxes, confidences, class_ids = [],[],[]

        for output in layer_outputs:

            for detection in output:

                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                # discarding weak predictions
                if confidence > confidence_threshold:

                    # b-box scaled to image size
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype('int')

                    # top-left co-ordinates derived from center
                    x = int(centerX - (width / 2))
                    y = int(centerY -(height / 2))

                    # b-box co-ordinates, confidence and classes to accumulators
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Remove overlapping bounding boxes and boundig boxes
        bboxes = cv.dnn.NMSBoxes(
            boxes, confidences, confidence_threshold, iou_threshold)
            
        if len(bboxes) > 0:
            for i in bboxes.flatten():

                # boundary boxes
                x, y = boxes[i][0], boxes[i][1]
                w, h = boxes[i][2], boxes[i][3]

                # draw bounding boxes
                color = [int(c) for c in colors[class_ids[i]]]
                cv.rectangle(frame, (x, y), (x + w, y + h), color=color, thickness=2)
                text = f'{labels[class_ids[i]]} : {confidences[i]:.2f}'

                # bbox overlay
                (text_width, text_height) = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, fontScale = 1, thickness=2)[0]
                
                text_offset_x = x
                text_offset_y = y - 5

                bbox_coords = ((text_offset_x, text_offset_y),(text_offset_x + text_width + 2, text_offset_y - text_height ))
                
                overlay = frame.copy()
                cv.rectangle(overlay, bbox_coords[0], bbox_coords[1], color=color, thickness=cv.FILLED)

                # opacity
                frame = cv.addWeighted(overlay, 0.6, frame, 0.4, 0)

                # label info ( label : confidence %)
                cv.putText(frame, text, (x,y-5), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)

        if show_display:
            cv.imshow("predictions", frame)
            key = cv.waitKey(1) & 0xFF
            # if the `q` key was pressed, break the loop
            if key == ord("q"):
                break

        if write_output:
            out.write(frame)

        fps.update()
        (success, frame) = cap.read()

    fps.stop()

    print("Elasped time: {:.2f}".format(fps.elapsed()))
    print("FPS: {:.2f}".format(fps.fps()))
    
    cap.release()

    if write_output:
        out.release()

    cv.destroyAllWindows()