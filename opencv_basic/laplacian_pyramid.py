import cv2

# Load an image
img = cv2.imread('HBD.jpg')

# Create a Gaussian pyramid
G = img.copy()
gp = [G]
for i in range(3):
    G = cv2.pyrDown(G)
    gp.append(G)

# Create a Laplacian pyramid
lp = [gp[2]]
for i in range(2, 0, -1):
    GE = cv2.pyrUp(gp[i])
    L = cv2.subtract(gp[i-1], GE[:gp[i-1].shape[0], :gp[i-1].shape[1]])
    lp.append(L)

# Display the Laplacian pyramid
for i in range(3):
    cv2.imshow('Laplacian Pyramid Level {}'.format(i), lp[i])
    cv2.waitKey(0)

cv2.destroyAllWindows()