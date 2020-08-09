import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    
    laplacian  = cv2.Laplacian(frame,cv2.CV_64F)


    # Laplacian Transformation. Laplacian Operator is also a derivative operator which is used to find edges in an image.
    #  It is a second order derivative mask. ... 
    # Unlike other operators Laplacian didn't take out edges in any particular direction but it takes out edges in following classification.
    

    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)


    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release() 