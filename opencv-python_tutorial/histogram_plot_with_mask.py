import numpy as np
import matplotlib.pyplot as plt

import cv2


img = cv2.imread('home.jpg', 0)
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask=mask)

# calculate histogram with mask and mask
# check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221)
plt.imshow(img,'gray')
plt.subplot(222)
plt.imshow(mask,'gray')
plt.subplot(223)
plt.imshow(masked_img,'gray')
plt.subplot(224)
plt.plot(hist_full)
plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()
