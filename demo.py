#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:57:46 2018

@author: asem
"""

from PIL import Image
import numpy as np
import scipy.fftpack as fp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def multi_view( images ):
    images_count = len( images )
    fig = plt.figure(figsize=(10,20))
    for row in range( images_count  ):
        ax1 = fig.add_subplot( images_count , 1 , row + 1)    
        ax1.imshow( images[ row ] )
        
## Functions to go from image to frequency-image and back
def im2freq( data ):
    return fp.fft2( data )

def freq2im( f ): 
    return fp.ifft2( f )

def rgb2gray(rgb_image):
    return np.dot(rgb_image[...,:3], [0.299, 0.587, 0.114])

def frequency_image( x ):
#    x = np.fft.fftshift(x)
    x = 20 * np.log10( np.abs( x ))
    return ( x - x.min() ) / ( x.max() - x.min() )

images_files = ['img1.jpg','img2.jpg']
images = [ rgb2gray( np.array(Image.open( file ))) for file in images_files ]

freq_images = [ im2freq(img) for img in images ]
freq_images_normalized = [ frequency_image( fi ) for fi in freq_images ]
back = [ np.real( freq2im(freq)) for freq in freq_images ] 


[ multi_view( comb ) for comb in zip( images ,freq_images_normalized , back )]

