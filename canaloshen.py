import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_convolution(image, kernel_size, sigma):
    # ایجاد فیلتر گوسی
    kernel = cv2.getGaussianKernel(kernel_size, sigma)

    # اعمال فیلتر گوسی بر روی تصویر
    result = cv2.filter2D(image, -1, kernel)

    return result

# خواندن تصویر
image = cv2.imread('mEAN63.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0
# تبدیل کانولوشن گوسی
result = gaussian_convolution(image, 5, 1)

# نمایش تصویر نرم شده
cv2.imshow('Gaussian Convolution', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
