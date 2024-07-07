import cv2
import numpy as np

def median_filter(image, kernel_size):
    # اعمال فیلتر Median
    median_image = cv2.medianBlur(image, kernel_size)
    
    return median_image



    # نمایش تصویر حاصل


# خواندن تصویر
image = cv2.imread("mEAN63.jpg")

result = median_filter(image,3)

cv2.imshow("Median Filter", result)
cv2.waitKey(0)
cv2.destroyAllWindows()