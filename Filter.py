import cv2 
import numpy as np

image =cv2.imread('/Untitled.jpeg')
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# نمایش تصویر اصلی و طیف فرکانسی
cv2.imshow('Image', image)
cv2.imshow('Magnitude Spectrum', magnitude_spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()
