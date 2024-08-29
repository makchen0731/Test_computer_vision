import cv2
import numpy as np

def Gaussian_Filter(img):
    
    h,w = img.shape

    Kernal_size = 3
    sigma = 5
    
    pad = Kernal_size//2
    G_F_img = np.zeros((h + 2*pad,w + 2*pad))
    G_F_img[pad:pad+h,pad:pad+w] = np.copy(img)
    
    Kernal = np.zeros((Kernal_size,Kernal_size))
    
    #build gaussian filter = kernal
    for x in range(-pad,-pad+Kernal_size):
        for y in range(-pad,-pad+Kernal_size):
            Kernal[y+pad,x+pad] = np.exp(-(x**2+y**2)/(2*(sigma**2)))
    
    Kernal /= (sigma*np.sqrt(2*np.pi))
    Kernal /=  Kernal.sum()
    
    # Kernal = np.random.normal(0,sigma,size = (Kernal_size,Kernal_size))
    
    #convelution
    for y in range(h):
        for x in range(w):
                G_F_img[pad+y,pad+x] = np.sum(Kernal*G_F_img[y:y+Kernal_size,x:x+Kernal_size])
    
    G_F_img = G_F_img[pad:pad+h,pad:pad+w].astype(np.uint8)
    
    return G_F_img

img = cv2.imread(r'C:\Users\NTNU-TA410\Desktop\Test_20210121\Result\rotated_image3333.png')[:,:,0]
cv2.imwrite(r'C:\Users\NTNU-TA410\Desktop\Test_20210121\Result\rotated_image1111111111.png',Gaussian_Filter(img))
