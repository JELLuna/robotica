import cv2
from blue_detector import BlueDetctor
from kalmanfilter import KalmanFilter

cap = cv2.VideoCapture("kobefor3.mp4")

# Load detector
od = BlueDetctor()

# Load Kalman filter to predict the trajectory
kf = KalmanFilter()

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    orange_bbox = od.detect(frame)
    x, y, x2, y2 = orange_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)

    predicted = kf.predict(cx, cy)
    #cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 4)
    cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)
    cv2.circle(frame, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(300)
    if key == 27:
        break