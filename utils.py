import cv2
import numpy as np

def apply_cloak(frame, background, selected_hsv):
    h, s, v = selected_hsv  # all are Python ints now

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([
        max(0, h - 20),
        max(60, s - 80),
        max(60, v - 80)
    ], dtype=np.uint8)

    upper = np.array([
        min(180, h + 20),
        min(255, s + 80),
        min(255, v + 80)
    ], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    mask_inv = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    res2 = cv2.bitwise_and(background, background, mask=mask)

    return cv2.add(res1, res2)
