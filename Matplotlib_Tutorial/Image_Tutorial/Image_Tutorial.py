# Here we use Matplotlib's imperative-style plotting interface, pyplot.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# ---Importing image data into Numpy arrays---
img = mpimg.imread('stinkbug.png')
print(img)
print(type(img))
print(img.shape, img.size)
print(img.dtype, img.itemsize)

# ---Rendering numpy arrays as images---
imgplot = plt.imshow(img)  # Return an AxesImage object
# plt.show()

# ---Applying pseudocolor schemes to image plots.---
# Pseudocolor is only relevant to single-channel, grayscale, luminosity images.
lum_img = img[:, :, 0]  # Slicing first channel of the img array
# plt.imshow(lum_img)  # A luminosity (2D, no color) image with viridis colormap
plt.imshow(lum_img, cmap="hot")
# plt.colorbar()
# plt.show()

imgplot = plt.imshow(lum_img)  # Return an AxesImage object (Object-oriented interface)
imgplot.set_cmap('nipy_spectral')
# plt.colorbar()
# plt.show()

# ---Array Interpolation schemes---
im = Image.open('stinkbug.png')
im.thumbnail((64, 64))  # resizes image in-place
plt.imshow(im)  # Data gets blown up to the size on the screen after shrinking the image
plt.show()

plt.imshow(im, interpolation="nearest")
plt.imshow(im, interpolation="bicubic")  # Override the previous state of the imported plt object
# Bicubic interpolation is often used when blowing up photos - people tend to prefer blurry over pixelated.
plt.show()
