import cv2
import numpy as np
import matplotlib.pyplot as plt

import cv2
import numpy as np

def low_pass_filter(image, cutoff_freq):
    # تبدیل تصویر به فضای رنگ سیاه و سفید
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # اعمال تبدیل DFT
    dft = cv2.dft(np.float32(image_gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # محاسبه مرکز فضای فرکانسی
    rows, cols = image_gray.shape
    crow, ccol = rows // 2, cols // 2

    # ایجاد ماسک فیلتر پایین گذرو
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow - cutoff_freq:crow + cutoff_freq, ccol - cutoff_freq:ccol + cutoff_freq, :] = 1

    # اعمال ماسک بر روی تبدیل DFT
    dft_shift_filtered = dft_shift * mask

    # بازگرداندن تبدیل DFT به حالت اصلی
    dft_filtered = np.fft.ifftshift(dft_shift_filtered)
    image_filtered = cv2.idft(dft_filtered)

    # استخراج قسمت حقیقی تصویر فیلتر شده
    image_filtered = cv2.magnitude(image_filtered[:, :, 0], image_filtered[:, :, 1])

    # نرمال‌سازی مقادیر تصویر فیلتر شده
    image_filtered = cv2.normalize(image_filtered, None, 0, 255, cv2.NORM_MINMAX)
    image_filtered = cv2.convertScaleAbs(image_filtered)

    return image_filtered

# خواندن تصویر
image = cv2.imread('photomode_14072023_120259.png')

# اعمال فیلتر پایین گذرو با فرکانس قطع
cutoff_freq = 30
result = low_pass_filter(image, cutoff_freq)

# نمایش تصویر فیلتر شده
cv2.imshow('Low Pass Filter', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
