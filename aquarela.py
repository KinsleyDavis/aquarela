import cv2
import os
 
path = 'c:/Filtros/'
 
for x in os.listdir():
    if x.endswith(".jpg") or x.endswith(".png"):      
        img = cv2.imread(path + x)
        res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)

        
        cv2.imshow('Original image',img)
        cv2.imshow('aquarela image', res)
        cv2.imwrite(path + x,res)
        print(x)


cv2.waitKey(0)
cv2.destroyAllWindows()



