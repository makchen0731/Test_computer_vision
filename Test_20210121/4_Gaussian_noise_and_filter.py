import numpy as np
import cv2
import math

img = cv2.imread(r"C:\Users\NTNU-TA410\Desktop\Test_20210121\Result\rotated_image22.png")[:,:,0]

#normalize the input image
h,w = img.shape
img_nol = np.clip(img/np.max(img),0,1)
img_long = h*w

#build normalization gaussian noise 
# Gaussian_noise = np.random.normal(0,10,img_long)
# Gaussian_noise_nol = np.reshape(np.clip(np.abs(Gaussian_noise/np.max(Gaussian_noise)),0,1),(h,w))

Gaussian_noise = np.random.normal(0,10,size = (h,w))
Gaussian_noise_nol = np.clip(np.abs(Gaussian_noise/np.max(Gaussian_noise)),0,1)


#build the gaussion image
G_add_img = (img_nol+Gaussian_noise_nol)
G_img_nol = np.clip(G_add_img/np.max(G_add_img),0,1)
G_img= G_img_nol*np.max(img)


G_img = np.around(G_img).astype(np.uint8)

cv2.imshow('img',G_img)
cv2.imwrite(r'C:\Users\NTNU-TA410\Desktop\Test_20210121\Result\rotated_image3333.png',G_img)