import numpy as np
import cv2
import math

height = 600
width = 800

output = np.zeros([height,width],dtype='uint8')
img = cv2.imread(r"C:\Users\NTNU-TA410\Desktop\Test_20210121\Result\rotated_image.png")[:,:,0]
h,w = img.shape

for H_y in range(height):
    for W_x in range(width):
        #we want define H = y, W = x but we want output[y][x] as (x,y) so y = (W_x/width)*w
        y = (W_x/width)*w
        x = (H_y/height)*h
        
        x1 = int(x)
        y1 = int(y)
        
        x2 = x1
        y2 = round(y1)
        
        x3 = round(x1)
        y3 = y1
        
        x4 = round(x1)
        y4 = round(y1)
        
        u = x - x1
        v = y - y1
        
        if x4 >= w:
            x1 = x4 - 1
            x2 = x1
            x3 = x4 - 1
            x4 = x4 - 1
        if y4 >= h:
            y1 = y4 - 1
            y2 = y1
            y3 = y4 - 1
            y4 = y4 - 1
        
        #f(i+u,j+v) = (1-u)(1-v)f(i,j) + (1-u)*v*f(i,j+1)+u*(1-v)*f(i+1,j)+u*v*f(i+1,j+1)
        
        output[H_y , W_x] = (1-u)*(1-v)*int(img[x1, y1]) \
                          + (1-u)*v*int(img[x2, y2]) \
                          + u*(1-v)*int(img[x3, y3]) \
                          + u*v*int(img[x4, y4])

cv2.imwrite(r'C:\Users\NTNU-TA410\Desktop\Test_20210121\Result\rotated_image22.png',output.astype(np.uint8))
