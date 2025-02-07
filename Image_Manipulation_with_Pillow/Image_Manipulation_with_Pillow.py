# Pillow is a fork of the Python Imaging Library (PIL). It will allow us to do many different things to our images
# such as: changing their file extension, resizing, cropping, changing colors, blurring, and much more.

# Pillow is extremely useful when you have multiple images you wish to process at once. For example, you can use
# Pillow to automatically create different sized thumbnails of images you upload to your web server.

from PIL import Image, ImageFilter # From package Pillow import module Image and ImageFilter
import os

im = Image.open('stinkbug.png')  # Return a PILImage object
im.show()
# im.save('stinkbug.jpg')

im_rot = im.rotate(90)  # Rotating image counterclockwise
im_rot.show()
im_rot.save('stinkbug_rot.png')

im.convert(mode='L').save('stinkbug_bw.png')  # Translating a color image to greyscale (mode "L")

im.filter(ImageFilter.GaussianBlur(15)).save('stinkbug_blur.png')  # Blurring an image with Gaussian filers


# # Convert multiple .png images to .jpg
# for f in os.listdir('.'):  # Strings of filenames in the current working directory
#     # print(f, type(f))
#     if f.endswith('.png'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#         i.save('jpgs/{}.jpg'.format(fn))


# # Resize groups of images to their thumbnails
# size_200 = (200, 200)
# size_100 = (100, 100)
#
# for f in os.listdir('.'):  # Strings of filenames in the current working directory
#     if f.endswith('.png'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#
#         i.thumbnail(size_200)  # In-place modification
#         i.save('200/{}_200{}'.format(fn, fext))
#
#         i.thumbnail(size_100)
#         i.save('100/{}_100{}'.format(fn, fext))