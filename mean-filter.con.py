import cv2
import numpy as np

def mean_filter(image, kernel_size):
    # ایجاد ماتریس فیلتر میانگین
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

    # اعمال فیلتر میانگین بر روی تصویر
    result = cv2.filter2D(image, -1, kernel)

    return result

# خواندن تصویر
image = cv2.imread('mEAN63.jpg')

# تبدیل کانولوشن میانگین
result = mean_filter(image, 5)

# نمایش تصویر نرم شده
cv2.imshow('Mean Filter', result)
cv2.waitKey(0)
cv2.destroyAllWindows()