import cv2
import numpy as np

def cartoonize_image(img, ksize=5, sketch_mode=False):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    gray = cv2.medianBlur(gray, ksize)

    # Detect edges using adaptive threshold
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    if sketch_mode:
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Apply bilateral filter for color smoothing
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine the edges and the color image
    cartoon = cv2.bitwise_and(color, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

    return cartoon

# Read the image
input_image = "input.jpg"
output_image = "output.jpg"
img = cv2.imread(input_image)

# Apply the cartoonization
cartoon_img = cartoonize_image(img)

# Save the output image
cv2.imwrite(output_image, cartoon_img)

# Display the original and cartoonized images side by side
cv2.imshow("Original Image", img)
cv2.imshow("Cartoonized Image", cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
