# import the necessary packages
import argparse

from helpers.document_scanner import *


def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", default='data/test.PNG', help="Path to the image scanned")

    args = vars(ap.parse_args())

    image, edged, ratio, orig = detection_edge(path=args["image"])
    # show the original and the edge detected images
    print("Step 1: Edge Detection")
    cv2.imshow("Image", image)
    cv2.imshow("Edged", edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    screen_cnt = find_contours(edged=edged)
    # show the contour (outline) of the piece of paper
    print("Step 2: Find contours of paper")
    cv2.drawContours(image, [screen_cnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    warped = perspective_transform(orig=orig, screen_cnt=screen_cnt, ratio=ratio)
    # show the original and scanned images
    print("Step 3: Apply perspective transform")
    cv2.imshow("Original", imutils.resize(orig, height=650))
    cv2.imshow("Scanned", imutils.resize(warped, height=650))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
