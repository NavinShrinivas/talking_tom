import cv2
import numpy as np

def process_image():
    filename=input("ENTER FILE NAME TO READ FROM :")
    image=cv2.imread("test4.png",0)
    cv2.imshow('initial',image)
    ls_image=cv2.medianBlur(image,1)
    recvals,tresholding_image=cv2.threshold(ls_image,30,255,cv2.THRESH_BINARY)
    flag_canny=input("are canny edges needed ? (y/n) :")
    final_img=tresholding_image
    if flag_canny.lower()=='y':
        final_img=cannyedge(tresholding_image)
    cv2.imshow('final', final_img)
    cv2.waitKey()

def cannyedge(image):
    return cv2.Canny(image,100,200)

    
process_image()
