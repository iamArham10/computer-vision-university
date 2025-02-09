import cv2 as cv2

def task_01():
    """Write a python script that loads an image from your local machine and displays it using openCV."""
    image = cv2.imread('sample_image.jpg')
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')
    return image

def task_02():
    """Convert Image to Grayscale."""
    image = cv2.imread('sample_image.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')
    cv2.destroyWindow('Grayscale Image')
    return gray_image

def task_03():
    """Apply Gaussian Blur to Image."""
    image = cv2.imread('sample_image.jpg')
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow('Original Image', image)
    cv2.imshow('Gaussian Blur Image', gaussian_blur)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')
    cv2.destroyWindow('Gaussian Blur Image')
    return gaussian_blur

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
    return edge_image

def task_05():
    """Resize the image to half it's original size"""
    image = cv2.imread('sample_image.jpg')
    resized_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')
    cv2.destroyWindow('Resized Image')
    return resized_image

def task_06(image, image_path):
    """Save the processed image"""
    try:
        cv2.imwrite(image_path, image)
    except Exception as e:
        print(f'Error: {e}')

def main():
    image = task_01()
    gray_image = task_02()
    gaussian_blur = task_03()
    edge_image = task_04()
    resized_image = task_05()
    task_06(resized_image, 'resized_image.jpg')
    task_06(edge_image, 'edge_image.jpg')
    task_06(gaussian_blur, 'gaussian_blur.jpg')
    task_06(gray_image, 'gray_image.jpg')
    task_06(image, 'original_image.jpg')

if __name__ == '__main__':
    main()