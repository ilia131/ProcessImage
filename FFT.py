import cv2
import numpy as np
import matplotlib.pyplot as plt

image =cv2.imread('mEAN63.jpg')

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 255.0

        # انجام تبدیل و محاسبه طیف فرکانسی
f = np.fft.fft2(image_gray)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.where(np.abs(fshift) == 0, 1, np.abs(fshift)))

        # نمایش تصویر اصلی
cv2.imshow('Image', image)

        # نمایش طیف فرکانسی
plt.imshow(magnitude_spectrum, cmap='gray')
plt.axis('off')
plt.show()

plt.imsave('path_to_save_magnitude_spectrum.png', magnitude_spectrum, cmap='gray')