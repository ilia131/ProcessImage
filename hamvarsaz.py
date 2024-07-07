import cv2
import numpy as np


def image_smoothing(image, kernel_size):
    # اعمال فیلتر هموارسازی بر روی تصویر
    smoothed_image = cv2.blur(image, (kernel_size, kernel_size))

    return smoothed_image

# خواندن تصویر
image = cv2.imread('photomode_14072023_120259.png')

# اعمال هموارسازی با استفاده از یک فیلتر متوسط
kernel_size = 5
result = image_smoothing(image, kernel_size)

# نمایش تصویر هموارسازی شده
cv2.imshow('Smoothed Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()