import os
import cv2   
from PIL import Image
import numpy as np


"""
This method is used to generate ground truth values.

"""
def generate_gt(filename,image):
    
    # Grayscale 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    # Find Canny edges 
    edged = cv2.Canny(gray, 30, 200) 
    cv2.waitKey(0) 
    # Finding Contours 
    # Use a copy of the image e.g. edged.copy() 
    # since findContours alters the image 
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    #cv2.imshow('Canny Edges After Contouring', edged) 
    cv2.waitKey(0) 
    #print("Number of Contours found = " + str(len(contours))) 
    # Draw all contours 
    # -1 signifies drawing all contours 
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    #cv2.imshow('Contours', image) 
    #cv2.waitKey(0) 
    cv2.destroyAllWindows()
    cv2.imwrite(filename, gray) 



def label_pixels(image,filename):
    
     x = np.asarray(image)
     x[x == 150 ] = 1  #green
     x[x == 255 ] = 2  #blue
     print(np.unique(x))
     image2 =  x.astype(np.uint8)
     cv2.imwrite(name, image2) 

if __name__ == "__main__":
    

    count = 1
    for root, dirs, files in os.walk('D:\\Spring2020\\CV\\Project\\Workspace\\Model23\\SegMed\\datasets\\Multi_organs\\training\\gt\\', topdown=False):
        for name in files:
            # Let's load a simple image with 3 black squares 
            image = cv2.imread(name) 
            cv2.waitKey(0) 
            generate_gt(name,image)
            label_pixels(name,image)
            count += 1
            
             
   
#    image = cv2.imread('10100_10600_ConfidenceMap.png') 
#    cv2.waitKey(0) 
#   
#    x = np.asarray(image)
#    x[x > 100 ] = 255
#    image =  x.astype(np.uint8)
#             
#    
#    