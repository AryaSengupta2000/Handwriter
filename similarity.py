from skimage.metrics import structural_similarity
import cv2

# 3. Load the two input images
imageA = cv2.imread(r'C:\Users\KIIT\Downloads\ROI_20.png')
imageB = cv2.imread(r'C:\Users\KIIT\Desktop\Writer\alpha661.png')

# 4. Convert the images to grayscale
#grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
#grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = structural_similarity(imageA, imageB, full=True)
diff = (diff * 255).astype("uint8")

# 6. You can print only the score if you want
print("SSIM: {}".format(score))
