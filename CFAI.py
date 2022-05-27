import cv2 as cv
import numpy as np
from mss import mss
import pyautogui
from CFApi.guns import snipe, rifle

sel =1

firearms = [snipe,rifle]
# 0 5 165 166 169 147
with mss() as sct:
    while True:
        x, y = pyautogui.position()
        monitor = {'top': y+30, 'left': x-25, 'width': 25, 'height': 50}
        img = np.array(sct.grab(monitor))
        hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        lower = np.array([0, 165, 147])
        upper = np.array([5, 166, 169])
        mask = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(img, img, mask=mask)
        if np.sum(result>10)>50:
            firearms[sel]()