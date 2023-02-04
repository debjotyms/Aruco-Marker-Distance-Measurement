import cv2
import numpy as np
import pickle

with open("calib.pckl", "rb") as f:
    data = pickle.load(f)
    cMat = data[0]
    dcoeff = data[1]

cap = cv2.VideoCapture(0)

dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_100)
dt = cv2.aruco.DetectorParameters_create()

while True:
    ret, frame = cap.read()
    corners, ids, _ = cv2.aruco.detectMarkers(frame, dict, parameters=dt)

    if ids is not None and ids.size > 0:
        id = ids[0]
        corner = corners[0][0]
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[0], 0.05, cMat, dcoeff)
        dist = np.linalg.norm(tvec)*100
        cv2.aruco.drawDetectedMarkers(frame, corners)
        cv2.putText(frame, f"Distance: {dist:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
