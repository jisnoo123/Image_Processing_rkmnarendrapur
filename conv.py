# Convolution code
import numpy as np
import matplotlib.pyplot as plt
import cv2

def convolution(img, kernel):
    # First padding the image
    padded_img = np.pad(img, pad_width=1, mode='constant', constant_values=0)

    result = np.zeros(img.shape)
    
    f = padded_img.copy()
    w = kernel.copy()

    responses = list()
    
    # Applying convolution
    for x in range(1, padded_img.shape[0]-1):
        for y in range(1, padded_img.shape[1]-1):
            response = f[x-1][y-1]*w[0][0] + f[x-1][y]*w[0][1] + f[x-1][y+1]*w[0,2] + \
                       f[x][y-1]*w[1][0] + f[x][y]*w[1][1] + f[x][y]*w[1][2] + \
                       f[x+1][y-1]*w[2][0] + f[x+1][y]*w[2][1] + f[x+1][y+1]*w[2][2]
            responses.append(response)

    # Place the response in the resulting image
    c = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            result[x][y] = responses[c]
            c += 1

    return result