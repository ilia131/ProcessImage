import cv2
import pywt

def wavelet_transform(image):
    # تبدیل تصویر به فضای رنگ سیاه و سفید
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # اعمال تبدیل ویولت
    coeffs = pywt.dwt2(image, 'haar')

    return coeffs

# خواندن تصویر
image = cv2.imread('photomode_14072023_120259.png')

# اعمال تبدیل ویولت
coeffs = wavelet_transform(image)

# نمایش ضرایب تبدیل
cA, (cH, cV, cD) = coeffs
cv2.imshow('Approximation (cA)', cA)
cv2.imshow('Horizontal Detail (cH)', cH)
cv2.imshow('Vertical Detail (cV)', cV)
cv2.imshow('Diagonal Detail (cD)', cD)
cv2.waitKey(0)
cv2.destroyAllWindows()
