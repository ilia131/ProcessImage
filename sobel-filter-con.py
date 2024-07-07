import cv2
import numpy as np


def sobel_filter(image):
    # اعمال فیلتر سابل در راستای افقی
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

    # اعمال فیلتر سابل در راستای عمودی
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # محاسبه مقدار مطلق گرادیان
    gradient = np.sqrt(np.square(sobelx) + np.square(sobely))

    # تبدیل مقادیر گرادیان به عدد بین 0 و 255
    gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient

# خواندن تصویر
image = cv2.imread('mEAN63.jpg', 0)

# اعمال فیلتر سابل
result = sobel_filter(image)

# نمایش تصویر نتیجه
cv2.imshow('Sobel Filter', result)
cv2.waitKey(0)
cv2.destroyAllWindows()