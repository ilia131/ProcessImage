import cv2
import numpy as np

def dft_transform(image):
    # تبدیل تصویر به فضای رنگ سیاه و سفید
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # تبدیل DFT
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

    # محاسبه طیف مقیاس
    magnitude_spectrum = np.log(1 + cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))

    # نرمال‌سازی مقادیر طیف مقیاس
    magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
    magnitude_spectrum = cv2.convertScaleAbs(magnitude_spectrum)

    return magnitude_spectrum

# خواندن تصویر
image = cv2.imread('mEAN63.jpg')

# اعمال تبدیل DFT
result = dft_transform(image)

# نمایش طیف مقیاس
cv2.imshow('DFT Transform', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
