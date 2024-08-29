import numpy as np
import cv2
import math


def shear(angle, x, y):
    '''
    |1  -tan(𝜃/2) |  |1        0|  |1  -tan(𝜃/2) | 
    |0      1     |  |sin(𝜃)   1|  |0      1     |
    '''

    tangent = math.tan(angle/2)

    new_x = round(x-y*tangent)
    new_y = y
    
    """
    need to caculater the new_y first
    that is wrong in following 
    --->
    new_x = round(new_x-new_y*tangent)     
    new_y = round(new_x*math.sin(angle)+new_y)

    """
    
    new_y = round(new_x*math.sin(angle)+new_y)      #new_y input to the next new_x
    new_x = round(new_x-new_y*tangent)              #since there is no change in new_y according to the shear matrix

    
    return new_y, new_x

def shear_No_tan(angle, x, y):

    new_x = round(x * math.cos(angle) + y * -math.sin(angle))
    new_y = round(x * math.sin(angle) + y * math.cos(angle))

    return new_y, new_x

image = cv2.imread(r"C:\Users\user\Desktop\Software\Python_3.12\git_test\Test_20210121\lena.bmp")[:,:,0]
print(image.shape)
angle = int(input("Enter the angle :")) # Ask the user to enter the angle of rotation

angle = math.radians(angle) #change angle to radian 弳度. 
cosine = math.cos(angle)
sine = math.sin(angle)

height = image.shape[0] #y top
width = image.shape[1] #x top

new_height  = round(abs(image.shape[0] * cosine) + abs(image.shape[1] * sine)) + 1 
new_width  = round(abs(image.shape[1] * cosine) + abs(image.shape[0] * sine)) + 1

output = np.zeros((new_height, new_width))
image_copy = output.copy()

original_centre_height  = round(((image.shape[0] + 1) / 2) - 1)    #with respect to the original image
original_centre_width = round(((image.shape[1] + 1) / 2) - 1)    #with respect to the original image

new_centre_height = round(((new_height + 1) / 2) - 1)        #with respect to the new image
new_centre_width = round(((new_width + 1) / 2) - 1)          #with respect to the new image

if __name__ == "__main__":
    
    for i in range(height):
        for j in range(width):
            #coordinates of pixel with respect to the centre of original image
            y=image.shape[0] - 1 - i - original_centre_height                   
            x=image.shape[1] - 1 - j - original_centre_width

            """
            if didn't move to center, image will be like No move to center_rotated_image1
            y=i             
            x=j
            """
            
            new_y, new_x = shear_No_tan(angle,x,y) #did't useing tan
            # new_y,new_x = shear(angle,x,y) #Usign tan
            new_y = new_centre_height - new_y
            new_x = new_centre_width - new_x
            output[new_y,new_x]=image[i,j]  #writing the pixels to the new destination in the output image
            
    for u in range(new_height):
        for v in range(new_width):
            if output[u,v] == 0 and u-1 >= 0 and v-1 >= 0 and u+1 <= new_height-1 and v+1 <= new_width-1:
                output[u,v] = round((output[u+1,v] + output[u,v-1] + output[u,v+1] + output[u-1,v]) / 4) # like convelution. get Mes from neighbor
            else:
                output[u,v] = output[u,v]

                    
cv2.imwrite(r'C:\Users\user\Desktop\Software\Python_3.12\git_test\Test_20210121\rotated_image.png',output.astype(np.uint8))
# cv2.imwrite(r'C:\Users\user\Desktop\Software\Python_3.12\git_test\Test_20210121\rotated_image1.png',output.astype(np.uint8))
