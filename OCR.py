import cv2
import numpy as np
import os
from flask import Flask, render_template

def process_image():
    filename=input("ENTER FILE NAME TO READ FROM :") #failename contains name of img to be processed
    clr_image=cv2.imread(filename) #using opencv read meathod to get img
    clr_image=cv2.resize(clr_image, (960, 540))  #resizing img
    image=cv2.cvtColor(clr_image,cv2.COLOR_RGB2GRAY) #converting to gray as OTSU_THRESH works only on grayscale
    ls_image=cv2.medianBlur(image,3) #used for removing noise from image can only take odd number as arg
    recvals,tresholding_image=cv2.threshold(ls_image,40,255,cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)
    final_img=tresholding_image
    return(clr_image,final_img)
    


def contours():
    image,pred_image=process_image()
    kernel=np.ones((15,20), np.uint8) #rectangular kerenels seem so work better than structuring elements
    dialted_image=cv2.dilate(pred_image, kernel, iterations = 2) 
    contour,unusedvar=cv2.findContours(dialted_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    drawnimg=image
    # cv2.drawContours(drawnimg, contour, -1, (0, 255, 0), 3) 
    for i in contour:
        x,y,a,d=cv2.boundingRect(i)
        cv2.rectangle(drawnimg, (x, y), (x + a, y + d), (0,0,255), 2)
    cv2.imshow('inital image',image) #will always be shown
    cv2.imshow('final', drawnimg) #showing drwaimg till final
    cv2.imshow('dilated image',dialted_image) #shown only for test
    cv2.waitKey()
    exit()
    return drawnimg



contours()







#--------------flask app----------[needs work]
# app=Flask(__name__)

# @app.route('/')
# def image_setting():
#     render=contours()
#     return render_template('index.html',url=render)

# if __name__ == '__main__':
#     app.run()