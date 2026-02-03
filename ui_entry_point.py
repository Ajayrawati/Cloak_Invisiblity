import cv2
import numpy as np
import time
from utils import apply_cloak

cap = cv2.VideoCapture(0)

background = None
selected_hsv = None
cloak_started = False
current_frame = None

VIDEO_W = 640
VIDEO_H = 480
PANEL_W = 260

BTN_BG = (20, 50, 240, 100)
BTN_START = (20, 120, 240, 170)


def draw_button(panel, btn, text, active=False):
    color = (0, 200, 0) if active else (200, 200, 200)
    cv2.rectangle(panel, (btn[0], btn[1]), (btn[2], btn[3]), color, -1)
    cv2.rectangle(panel, (btn[0], btn[1]), (btn[2], btn[3]), (0, 0, 0), 2)
    cv2.putText(panel, text, (btn[0] + 10, btn[1] + 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


def mouse_events(event, x, y, flags, param):
    global background, selected_hsv, cloak_started, current_frame

    if event != cv2.EVENT_LBUTTONDOWN:
        return

    # Clicks inside UI panel
    if x > VIDEO_W:
        px = x - VIDEO_W

        if BTN_BG[0] < px < BTN_BG[2] and BTN_BG[1] < y < BTN_BG[3]:
            print("Capturing background...")
            time.sleep(1)
            for _ in range(30):
                ret, bg = cap.read()
                if ret:
                    background = cv2.flip(bg, 1)
            print("Background captured!")

        elif BTN_START[0] < px < BTN_START[2] and BTN_START[1] < y < BTN_START[3]:
            if background is not None:
                cloak_started = True
                print("Cloak started! Click cloak color.")
            else:
                print("Capture background first!")

    # Click on video → pick cloak color
    else:
        if cloak_started and current_frame is not None:
            hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
            h, s, v = hsv[y, x]

            if s < 50:
                print("Low saturation! Use bright solid color.")
                return

            selected_hsv = (int(h), int(s), int(v))
            print("Selected HSV:", selected_hsv)


cv2.namedWindow("Invisible Cloak")
cv2.setMouseCallback("Invisible Cloak", mouse_events)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (VIDEO_W, VIDEO_H))
    frame = cv2.flip(frame, 1)
    current_frame = frame.copy()

    if cloak_started and selected_hsv is not None:
        video = apply_cloak(frame, background, selected_hsv)
    else:
        video = frame.copy()

    panel = np.ones((VIDEO_H, PANEL_W, 3), dtype=np.uint8) * 240

    draw_button(panel, BTN_BG, "Capture BG", background is not None)
    draw_button(panel, BTN_START, "Start Cloak", cloak_started)

    cv2.putText(panel, "Status:", (20, 220),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    status = "READY" if selected_hsv else "WAITING"
    cv2.putText(panel, status, (20, 260),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 200), 2)

    combined = np.hstack((video, panel))
    cv2.imshow("Invisible Cloak", combined)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
