import numpy as np
import cv2

whiteFrame = 255 * np.ones((842,595,3), np.uint8)

cv2.imwrite(r'C:\Users\KIIT\Documents\hell.png',whiteFrame)
