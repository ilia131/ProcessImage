import cv2
import numpy as np

def prewitt_filter(image):
    # تبدیل تصویر به سیاه و سفید
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # اعمال فیلتر Prewitt در جهت افقی
    prewitt_x = cv2.filter2D(gray_image, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
    
    # اعمال فیلتر Prewitt در جهت عمودی
    prewitt_y = cv2.filter2D(gray_image, -1, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]))
    
    # ترکیب نتایج در جهت افقی و عمودی
    prewitt_combined = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)
    
    return prewitt_combined
    # نمایش تصویر حاصل
  

# خواندن تصویر
image = cv2.imread("mEAN63.jpg")
result = prewitt_filter(image)
# اجرای تابع تبدیل
prewitt_filter(image)  
cv2.imshow("Prewitt Filter", result)
cv2.waitKey(0)
cv2.destroyAllWindows()