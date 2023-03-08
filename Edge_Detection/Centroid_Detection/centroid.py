import numpy as np
import math
import cv2
import argparse
from moments import moments
import matplotlib.pyplot as plt

def centroid(image):
    if len(image.shape) == 3:
        print("Found 3 Channels : {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. Size : {}".format(image.shape))
    else:
        print("Image Shape : {}".format(image.shape))

    moment = moments(image)
    X = int(moment['m10']/moment['m00'])
    Y = int(moment['m01']/moment['m00'])

    return image, X,Y

def circle(image, x, y, rad ):
    print(image.shape[0])
    print(image.shape[1])
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            dist = math.sqrt(((i-x)**2)+((j-y)**2))
            if dist <= rad:
                image[i][j] = 255
    return image

if __name__ == '__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    ap.add_argument("-v", "--verbose", type=bool, default=False, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])

    gray, centroid_X, centroid_Y = centroid(image)
    new_image = circle(gray, centroid_X, centroid_Y, 5)

    plt.imshow(new_image, cmap="gray")
    plt.title("Centroid Detector")
    plt.show()


