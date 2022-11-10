import sys
import cv2

img1 = cv2.imread(sys.path[0]+'\\lena.bmp')

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.imshow('ori', img1)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
