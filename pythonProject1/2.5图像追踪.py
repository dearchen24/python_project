import cv2
import numpy as np

# 指定摄像头索引，0通常是默认摄像头
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设定红色范围，这里是一个例子，可能需要根据实际情况调整
    lower_red = np.array([0, 50, 50])  # 考虑到红色的不同变种，这里从0开始
    upper_red = np.array([10, 255, 255])
    # 如果需要包含更广泛的红色，可以扩展范围
    # lower_red = np.array([0, 120, 70])
    # upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()