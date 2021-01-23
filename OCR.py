import cv2


def process_image():
    filename=input("ENTER FILE NAME TO READ FROM :")
    image=cv2.imread(filename+'.*',0);
    cv2.imshow('image', image)
    cv2.waitKey()


process_image()
