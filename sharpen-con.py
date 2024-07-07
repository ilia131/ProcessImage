import cv2
import numpy as np


def sharpen_filter(image):
    # تعریف ماتریس فیلتر شارپن
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # اعمال فیلتر شارپن بر روی تصویر
    result = cv2.filter2D(image, -1, kernel)

    return result

# خواندن تصویر
image = cv2.imread('mEAN63.jpg')

# اعمال فیلتر شارپن
result = sharpen_filter(image)

# نمایش تصویر نتیجه
cv2.imshow('Sharpen Filter', result)
cv2.waitKey(0)
cv2.destroyAllWindows()