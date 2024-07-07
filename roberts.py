import cv2
import numpy as np

def roberts_filter(image):
    # تبدیل تصویر به سیاه و سفید
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # اعمال فیلتر Roberts در جهت افقی
    roberts_x = cv2.filter2D(gray_image, -1, np.array([[1, 0], [0, -1]]))
    
    # اعمال فیلتر Roberts در جهت عمودی
    roberts_y = cv2.filter2D(gray_image, -1, np.array([[0, 1], [-1, 0]]))
    
    # ترکیب نتایج در جهت افقی و عمودی
    roberts_combined = cv2.addWeighted(roberts_x, 0.5, roberts_y, 0.5, 0)
    
    return roberts_combined
    # نمایش تصویر حاصل
  

# خواندن تصویر
image = cv2.imread("mEAN63.jpg")
resault = roberts_filter(image)
# اجرای تابع تبدیل
roberts_filter(image) 
cv2.imshow("Roberts Filter", resault )
cv2.waitKey(0)
cv2.destroyAllWindows()