import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage import feature
from skimage.transform import probabilistic_hough_line
from skimage import measure


original = io.imread('predict3.jpg')
grayscale = rgb2gray(original)
edges = feature.canny(grayscale, sigma=2)
lines = probabilistic_hough_line(edges, threshold=10, line_length=10,line_gap=3)

#contours = measure.find_contours(edges, 0.8)

fig, axes = plt.subplots(1, 2, figsize=(30, 10))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")

ax[1].imshow(edges)
ax[1].set_title("Grayscale")
for line in lines:
    p0, p1 = line
    ax[1].plot((p0[0], p1[0]), (p0[1], p1[1]))
#for contour in contours:
 #   ax.plot(contour[:, 1], contour[:, 0], linewidth=2)    
fig.tight_layout()
plt.show()