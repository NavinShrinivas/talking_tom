import cv2
import numpy as np
import psutil as res
import os

def process_image():
    filename=input("ENTER FILE NAME TO READ FROM :")
    clr_image=cv2.imread("test2.png")
    clr_image=cv2.resize(clr_image, (960, 540)) 
    image=cv2.cvtColor(clr_image,cv2.COLOR_RGB2GRAY)
    ls_image=cv2.medianBlur(image,3)
    recvals,tresholding_image=cv2.threshold(ls_image,40,255,cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)
    final_img=tresholding_image
    return(clr_image,final_img)
    

def contours():
    image,pred_image=process_image()
    kernel=np.ones((18,20), np.uint8) #rectangular kerenels seem so work better than structuring elements
    dialted_image=cv2.dilate(pred_image, kernel, iterations = 1) 
    contour,unusedvar=cv2.findContours(dialted_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    drawnimg=image
    # cv2.drawContours(drawnimg, contour, -1, (0, 255, 0), 3) 
    for i in contour:
        x,y,a,d=cv2.boundingRect(i)
        cv2.rectangle(drawnimg, (x, y), (x + a, y + d), (0,0,255), 2)
    cv2.imshow('inital image',image)
    cv2.imshow('final', drawnimg)
    cv2.imshow('dilated image',dialted_image)
    cv2.waitKey()
    exit()


#process=res.Process(os.getpid())
#print(process.memory_info().rss)
contours()
