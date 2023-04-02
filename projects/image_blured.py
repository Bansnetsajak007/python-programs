# from PIL import Image, ImageFilter

# # Open an image and apply a Gaussian blur filter
# image = Image.open('OIP.jpg')
# blurred_image = image.filter(ImageFilter.GaussianBlur(radius=10))
# # blurred_image = image.filter(ImageFilter.Color3DLUT(size=10,table=8))

# # Save the blurred image
# blurred_image.save('example_.jpg')

# from PIL import Image

# # Create a new transparent image
# image = Image.new('RGBA', (400, 400), color=(40, 60, 100, 50))

# # Save the image
# image.save('new_transparent_image.png')

import cv2

# Load the image
image = cv2.imread('example.jpg')

# Resize the image to a width of 500 pixels
new_width = 500
height, width = image.shape[:2]
new_height = int(new_width * height / width)
resized_image = cv2.resize(image, (new_width, new_height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imwrite('output.png', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

