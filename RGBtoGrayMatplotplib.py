from matplotlib.image import imread
import matplotlib.pyplot as plt
import sys

input_img = imread(sys.path[0]+"\\lena.bmp", 0)

r,g,b = input_img[:,:,0], input_img[:,:,1], input_img[:,:,2]

gamma = 1.1

r_const, g_const, b_const = 0.2126, 0.7152, 0.0722

gray_img = r_const * r ** gamma + g_const * g ** gamma + b_const * b ** gamma

fig = plt.figure(figsize=(10,7))
img1, img2 = fig.add_subplot(121), fig.add_subplot(122)

img1.imshow(input_img)
img2.imshow(gray_img, cmap=plt.cm.get_cmap('gray'))

fig.show()
plt.show()
