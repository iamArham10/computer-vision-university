import cv2 as cv2

def task_01():
    """Write a python script that loads an image from your local machine and displays it using openCV."""
    image = cv2.imread('sample_image.jpg')
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')

def task_02():
    """Convert Image to Grayscale."""
    image = cv2.imread('sample_image.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')
    cv2.destroyWindow('Grayscale Image')

def task_03():
    """Apply Gaussian Blur to Image."""
    image = cv2.imread('sample_image.jpg')
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow('Original Image', image)
    cv2.imshow('Gaussian Blur Image', gaussian_blur)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')
    cv2.destroyWindow('Gaussian Blur Image')

def task_04():
    """Perform Edge Detection on a grayscale image."""
    image = cv2.imread('sample_image.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edge_image = cv2.Canny(gray_image, 100, 200)
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge Detection Image', edge_image)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')
    cv2.destroyWindow('Edge Detection Image')