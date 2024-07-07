import cv2

def laplacian_filter(image):
    # اعمال فیلتر لاپلاسیان
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # تبدیل مقادیر به عدد بین 0 و 255
    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return laplacian

# خواندن تصویر
image = cv2.imread('mEAN63.jpg', 0)

# اعمال فیلتر لاپلاسیان
result = laplacian_filter(image)

# نمایش تصویر نتیجه
cv2.imshow('Laplacian Filter', result)
cv2.waitKey(0)
cv2.destroyAllWindows()