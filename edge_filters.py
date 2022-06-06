import numpy as np 
import matplotlib.pyplot as plt 
from scipy.signal import convolve2d
from skimage.data import shepp_logan_phantom

def filters(img, filter_name):
    '''
    Three filters: 'pewitt', 'sobel' and 'scharr'

    Parameters
    ----------
    img : 2d array
        2d image to convole with filter.
    filter_name : str
        name of filter.

    Returns
    -------
    TYPE
        2d image after filtering.

    '''
    
    p_msk = np.array([[-1,0,1], [-1,0,1], [-1,0,1]])
    s_msk=np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    sch_msk = np.array([[-3,0,3], [-10,0,10], [-3,0,3]])
    
    if filter_name.lower() == 'pewitt':
        x_axis=convolve2d(img, p_msk, 'same')
        y_axis=convolve2d(img, p_msk.T, 'same')
        return np.sqrt(y_axis**2 + y_axis**2)
    
    elif filter_name.lower() == 'sobel':
        x_axis=convolve2d(img, s_msk, 'same')
        y_axis=convolve2d(img, s_msk.T, 'same')
        return np.sqrt(x_axis**2 + y_axis**2)
    
    elif filter_name.lower() == 'scharr':
        x_axis=convolve2d(img, sch_msk, 'same')
        y_axis=convolve2d(img, sch_msk.T, 'same')
        return np.sqrt(x_axis**2 + y_axis**2)

### Loading image
img = shepp_logan_phantom()

### Filtering
filter_names = ['pewitt', 'sobel', 'scharr']
edge_images = np.array([filters(img, i) for i in filter_names])

### Results
k = 1
plt.figure(figsize = (13,4))
for i,j in enumerate(edge_images):
    plt.subplot(1,3,k)
    plt.title(filter_names[i])
    plt.imshow(j,cmap = 'jet', aspect = 'equal')
    k+=1