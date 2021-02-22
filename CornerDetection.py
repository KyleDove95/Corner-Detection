import cv2
import numpy as np
def harris_corner(windowSize, k):
    greyImage = cv2.imread("image.jpg", 0)

    rows = greyImage.shape[0]
    cols = greyImage.shape[1]

    colorImage = cv2.imread("image.jpg")
    colorImage2 = cv2.imread("image.jpg")
    offset = int(windowSize/2)

    iY = np.zeros((rows, cols), np.float32)
    iX = np.zeros((rows, cols), np.float32)
    rValue = np.zeros((rows, cols), np.float32)
    maxValue = 0
    for j in range(1, rows-1):
        for i in range(1, cols-1):
            iY[j][i] = int(greyImage[j-1][i]) - int(greyImage[j+1][i])
            iX[j][i] = int(greyImage[j][i-1]) - int(greyImage[j][i+1])

    i_YY = iY*iY
    i_XX = iX*iX
    i_XY = iX*iY

    for j in range(offset, rows-offset):
        for i in range(offset, cols-offset):
            sumIXX = 0
            sumIYY = 0
            sumIXY = 0
            Ixx = i_XX[j-offset+1: j+offset+1, i-offset+1: i+offset+1]
            Iyy = i_YY[j-offset+1: j+offset+1, i-offset+1: i+offset+1]
            Ixy = i_XY[j-offset+1: j+offset+1, i-offset+1: i+offset+1]

            for b in range(Ixx.shape[0]):
                for a in range(Ixx.shape[1]):
                    sumIXX = sumIXX + Ixx[b][a]
            for b in range(Iyy.shape[0]):
                for a in range(Iyy.shape[1]):
                    sum_Iyy = sumIYY + Iyy[b][a]
            for b in range(Ixy.shape[0]):
                for a in range(Ixy.shape[1]):
                    sumIXY = sumIXY + Ixy[b][a]

            detSum=(sumIXX*sum_Iyy)-(sumIXY**2)
            trace = sumIXX+sumIYY
            rValue[j][i] = (detSum - k*(trace**2))

            if rValue[j][i] > maxValue:
                maxValue = rValue[j][i]


    for j in range(rValue.shape[0]):
        for i in range(rValue.shape[1]):
            if rValue[j][i] > 0.1*maxValue:
                cv2.circle(colorImage, (i, j), 3, (0, 0, 255), -1)

            if rValue[j][i] > .3*maxValue:
                largestValue = rValue[j][i]

    for j in range(rValue.shape[0]):
        for i in range(rValue.shape[1]):
            if rValue[j][i] == largestValue:
                cv2.circle(colorImage2, (i, j), 3, (0, 0, 255), -1)

    cv2.imshow("Corner Picture", colorImage)
    cv2.imshow("Max Corner Picture", colorImage2)

def main():
    harris_corner(3, .3)
    
main()
