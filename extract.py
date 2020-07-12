import cv2
import numpy as np
#import image
image = cv2.imread(r'C:\Users\KIIT\Downloads\IMG20200516201648200.jpg')
#cv2.imshow('orig',image)
#cv2.waitKey(0)

#grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

#dilation
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)

#find contours
ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # Getting ROI
    roi = image[y:y+h, x:x+w]

    width,hieght = roi.shape[:2]

    if width>20 and hieght>20:#keep aspect ratio


        new_width = 24

        new_height = new_width * height / width

        new_height = 24

        new_width = new_height * width / height

        output = roi.resize((new_width,new_height), Image.ANTIALIAS)

    # show ROI
    #cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
     cv2.imwrite(r'C:\Users\KIIT\Desktop\Writer\alpha{}.png'.format(i), output)
