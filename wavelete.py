import pywt
import cv2
import numpy as np

def wavelet_filter(image):
    # تبدیل تصویر به سیاه و سفید
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # اعمال تبدیل Wavelet
    coeffs = pywt.dwt2(gray_image, 'haar')
    cA, (cH, cV, cD) = coeffs
    
    # بازسازی تصویر از ضرایب Wavelet
    reconstructed_image = pywt.idwt2((cA, (None, None, None)), 'haar')
    
    return reconstructed_image.astype(np.uint8)
    # نمایش تصویر حاصل
   

# خواندن تصویر
image = cv2.imread("mEAN63.jpg")
result = wavelet_filter(image)
# اجرای تابع تبدیل
cv2.imshow("Wavelet Filter", result)
cv2.waitKey(0)
cv2.destroyAllWindows()