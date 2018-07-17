#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:14:16 2018

@author: priyanka
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

#Convolution
def gaussialBLur(img):
    kernel = np.array([[1,4,7,4,1],
                       [4,40,46,40,4],
                       [7,46,61,46,7],
                       [4,40,46,40,4],
                       [1,4,7,4,1]])
    filter_map = np.zeros((img.shape[0],img.shape[1]))
    for i in range(gray_img.shape[0] - kernel.shape[0]):
        for j in range(gray_img.shape[1] - kernel.shape[1]):
            receptive_field = img[i:i+kernel.shape[0],j:j+kernel.shape[1]]
            filter_map[i:i+kernel.shape[0],j:j+kernel.shape[1]] = np.dot(kernel,receptive_field) 
    return filter_map     
   
#Convert image to grayscale
def rgb2gray(img):
    gray_img = (img[:,:,0]+img[:,:,1]+img[:,:,2])/2
    return gray_img

#Convert image to bw
def rgb2bw(gray_img): 
    bw_img = np.zeros((gray_img.shape[0],gray_img.shape[1]))
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]): 
            if (gray_img[i][j]) >= 100:
                bw_img[i][j] = 255
            else:
                bw_img[i][j] = 0
    return bw_img


img = Image.open('my_image.png')
img_arr = np.asarray(img)

plt.imshow(img_arr)
plt.show()

gray_img = rgb2gray(img_arr)
plt.imshow(gray_img,cmap='gray', vmin = 0, vmax = 255)
plt.show()
#print(g_img.shape)
bw_img = rgb2bw(gray_img)
plt.imshow(bw_img,cmap='gray', vmin = 0, vmax = 255)
plt.show()

filter_map = gaussialBLur(gray_img)
plt.imshow(filter_map,cmap='gray')
plt.show()
#cv2.imshow("test",filter_map)
#cv2.waitKey(500)


