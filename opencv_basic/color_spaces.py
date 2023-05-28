import cv2

# Load image
img = cv2.imread('HBD.jpg')

# Convert to different color spaces
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
luv_img = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)

# Split channels for each color space
gray_channels = cv2.split(gray_img)
hsv_channels = cv2.split(hsv_img)
lab_channels = cv2.split(lab_img)
ycrcb_channels = cv2.split(ycrcb_img)
hls_channels = cv2.split(hls_img)
luv_channels = cv2.split(luv_img)

# Display original and color space images
cv2.imshow("Original Image", img)

cv2.imshow("Grayscale Image", gray_img)
cv2.imshow("Gray Channel", gray_channels[0])

cv2.imshow("HSV Image", hsv_img)
cv2.imshow("H Channel", hsv_channels[0])
cv2.imshow("S Channel", hsv_channels[1])
cv2.imshow("V Channel", hsv_channels[2])

cv2.imshow("LAB Image", lab_img)
cv2.imshow("L Channel", lab_channels[0])
cv2.imshow("A Channel", lab_channels[1])
cv2.imshow("B Channel", lab_channels[2])

cv2.imshow("YCrCb Image", ycrcb_img)
cv2.imshow("Y Channel", ycrcb_channels[0])
cv2.imshow("Cr Channel", ycrcb_channels[1])
cv2.imshow("Cb Channel", ycrcb_channels[2])

cv2.imshow("HLS Image", hls_img)
cv2.imshow("H Channel", hls_channels[0])
cv2.imshow("L Channel", hls_channels[1])
cv2.imshow("S Channel", hls_channels[2])

cv2.imshow("Luv Image", luv_img)
cv2.imshow("L Channel", luv_channels[0])
cv2.imshow("u Channel", luv_channels[1])
cv2.imshow("v Channel", luv_channels[2])

cv2.waitKey(0)
cv2.destroyAllWindows()