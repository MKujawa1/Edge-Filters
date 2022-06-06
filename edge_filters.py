import numpy as np 
import matplotlib.pyplot as plt 
from scipy.signal import convolve2d
from skimage.data import shepp_logan_phantom

img = shepp_logan_phantom()

p_msk = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
x_axis=convolve2d(img, p_msk, 'same')
y_axis=convolve2d(img, p_msk.T, 'same')
pewitt=np.sqrt(y_axis**2 + y_axis**2)

s_msk=np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
x_axis=convolve2d(img, s_msk, 'same')
y_axis=convolve2d(img, s_msk.T, 'same')
sobel=np.sqrt(x_axis**2 + y_axis**2)

sch_msk = np.array([[-3,0,3], [-10,0,10], [-3,0,3]])
x_axis=convolve2d(img, sch_msk, 'same')
y_axis=convolve2d(img, sch_msk.T, 'same')
scharr=np.sqrt(x_axis**2 + y_axis**2)

