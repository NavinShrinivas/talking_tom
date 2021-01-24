import cv2
import numpy as np

def process_image():
    filename=input("ENTER FILE NAME TO READ FROM :")
    clr_image=cv2.imread("test4.png")
    clr_image=cv2.resize(clr_image, (960, 540)) 
    image=cv2.cvtColor(clr_image,cv2.COLOR_RGB2GRAY)
    ls_image=cv2.medianBlur(image,1)
    recvals,tresholding_image=cv2.threshold(ls_image,30,255,cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
    final_img=tresholding_image
    return(clr_image,final_img)
    # cv2.imshow('initial',image)
    # cv2.imshow('final', final_img)
    # cv2.waitKey()



def contours():
    image,pred_image=process_image()
    rectdef=cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
    dialted_image=cv2.dilate(pred_image, rectdef, iterations = 1) 
    contour,unusedvar=cv2.findContours(dialted_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    drawnimg=image
    # cv2.drawContours(drawnimg, contour, -1, (0, 255, 0), 3) 
    for i in contour:
        x,y,a,d=cv2.boundingRect(i)
        cv2.rectangle(drawnimg, (x, y), (x + a, y + d), (0,255,0), 2)

    cv2.imshow('final', drawnimg)
    cv2.waitKey()
    


contours()
