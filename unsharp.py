#Unsharp mask enhances edges by subtracting an unsharp (smoothed) version of the image from the original.
#Effectively making the filter a high pass filter. 
#enhanced image = original + amount * (original - blurred)
#Amount of sharpening can be controlled via scaling factor, a multiplication factor
#for the sharpened signal. 
#skimage uses Gaussian smoothing for image blurring therefore the radius parameter 
#in the unsharp masking filter refers to the sigma parameter of the gaussian filter.


#This part of the code shows that unsharp mask is nothing but original + amount *(original-blurred)

from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian

img = img_as_float(io.imread("cr7.jpg"))

gaussian_img = gaussian(img, sigma=2, mode='constant', cval=0.0)

img2 = (img - gaussian_img)*2

img3 = img + img2

from matplotlib import pyplot as plt

plt.imshow(img3)

#Here we gonna use the unsharp_mask fucntion

img = io.imread("cr7.jpg")

#Radius defines the degree of blurring
#Amount defines the multiplication factor for original - blurred image

unsharped_img = unsharp_mask(img, radius=3, amount=2)

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(1,2,2)
ax2.imshow(unsharped_img, cmap='gray')
ax2.title.set_text('Unsharped Image')
plt.show()
