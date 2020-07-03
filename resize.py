import cv2

img = cv2.imread (r'C:\Users\KIIT\Documents\black-and-whit.png',cv2.IMREAD_UNCHANGED)

dsize = (24,24)

output = cv2.resize( img , dsize)

cv2.imwrite(r'C:\Users\KIIT\Documents\hey.png', output)
