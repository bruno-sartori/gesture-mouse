import handy
import cv2
import os
import pyautogui

__dirname = os.path.dirname(__file__)
video_source = -1 # os.path.join(__dirname, '../test/test2.mp4')
#Open Camera object

hist = handy.capture_histogram()

cap = cv2.VideoCapture(video_source)

def setCursor(fingertips):
    x = sum([pair[0] for pair in fingertips]) / len(fingertips)
    y = sum([pair[1] for pair in fingertips]) / len(fingertips)

    pyautogui.moveTo(x, y)



while True:
    ret, frame = cap.read()

    if (ret == 0):
        print("Error1: check if webcam is connected")
        break
    # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
	
    # detect the hand
    hand = handy.detect_hand(frame, hist)
    
    # plot the fingertips
    for fingertip in hand.fingertips:
        cv2.circle(hand.outline, fingertip, 5, (0, 0, 255), -1)
        
    if(len(hand.fingertips) <= 5 and len(hand.fingertips) > 0):
        setCursor(hand.fingertips)

    cv2.imshow("Handy", hand.outline)
    
    k = cv2.waitKey(5)
    if k == ord('q'):
        break
