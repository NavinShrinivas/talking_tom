import cv2


def process_image():
    img=cv2.imread("./text.jpg",0);
    cv2.imshow('image', img)

process_image()
