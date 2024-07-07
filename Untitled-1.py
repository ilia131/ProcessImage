import cv2
import numpy as np
import matplotlib.pyplot as plt
image =cv2.imread('mEAN63.jpg')

image = image.astype(float) / 255

f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.where(np.abs(fshift) == 0, 1, np.abs(fshift)))

# نمایش تصویر اصلی و طیف فرکانسی
cv2.imshow('Image', image)

plt.imshow(magnitude_spectrum)
plt.axis('off')
plt.show()
