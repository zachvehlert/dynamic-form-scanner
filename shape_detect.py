import cv2
import os

images = []
for file in os.listdir('Forms_png'):
    path = 'Forms_png/' + str(file)
    images.append(path)

imgOri = cv2.imread(images[0])

# Scale down image
scale = 0.5
w = int(imgOri.shape[1] * scale)
h = int(imgOri.shape[0] * scale)
dim = (w, h)
img = cv2.resize(imgOri, dim, interpolation=cv2.INTER_AREA)

# copy image to draw on later
imgContours = img.copy()


def find_shapes(image, min_area):
    # Find contours, specifically external contours
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Get the area of the contours detected
    tables = []
    for c in contours:
        area = cv2.contourArea(c)
        # If the area is greater than minimum threshold
        if area > min_area:
            cv2.drawContours(imgContours, c, -1, (0, 0, 0), 5)
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            tables.append([y, x, (y + h), (x + w)])
            cv2.rectangle(imgContours, (x, y), (x + w, y + h), (255, 0, 255), 2)
            # cv2.putText(imgContours,str(area),(x,y),1,2,(255,0,0),2)
    return tables


# Detect edges
edges = cv2.Canny(img, 50, 50)
tables = find_shapes(edges, 50000)

cv2.imshow('Shape', imgContours)
cv2.waitKey(0)
for t in tables:
    cv2.imshow('Shape', imgContours[t[0]:t[2],t[1]:t[3]])
    cv2.waitKey(0)
