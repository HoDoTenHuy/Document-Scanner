# import the necessary packages
import cv2
import imutils

from skimage.filters import threshold_local
from utils.common import four_point_transform


def detection_edge(path):
    """----- Step 1 -----"""
    # load the image and compute the ratio of the old height to the new height, clone it, and resize it
    image = cv2.imread(path)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

    # convert image to grayscale, blur it, amd find edges in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray - cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    return image, edged, ratio, orig


def find_contours(edged):
    """----- Step 2 -----"""
    # find the contours in the edged image, keeping only the largest ones, and initialize the screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then we can assume that we have found our screen
        if len(approx) == 4:
            screen_cnt = approx
            break

    return screen_cnt


def perspective_transform(orig, screen_cnt, ratio):
    """----- Step 3 -----"""
    # apply the four points transform to obtain a top-down view of the original image
    warped = four_point_transform(orig, screen_cnt.reshape(4, 2) * ratio)

    # convert the warped image to grayscale, then threshold it to give it that 'black and white' paper effect
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method='gaussian')
    warped = (warped > T).astype("uint8") * 255
    return warped
