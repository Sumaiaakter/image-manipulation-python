# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:14:11 2022

@author: Farhan
"""

import numpy as np
from astropy.io import fits, os

import matplotlib.pyplot as plt
from astropy.visualization import MinMaxInterval, PercentileInterval, ZScaleInterval, SqrtStretch, AsinhStretch, LogStretch, LinearStretch, ImageNormalize

from astropy.table import Table



#---------Image manipulation with python (-------task------IV--------)

fits_file=fits.open('C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/Gemini/MOO_0917-0700_gmos_r.fits',memmap=True)

image_data=fits_file[0].data
image_header=fits_file[0].header
fits_file.close()

x_axes=plt.axes()
x_axes.imshow(image_data, origin='lower', cmap='Greys_r')
x_axes.imshow(np.log10(image_data), origin='lower', cmap='Greys')
normalisation=ImageNormalize(image_data, interval=ZScaleInterval(), stretch=LinearStretch())
x_axes.imshow(image_data, origin='lower', cmap='Greys', norm=normalisation)

#-------------------END-------------------------------------

image_data=fits.getdata('C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/Gemini/MOO_0917-0700_gmos_r.fits')


image_header=fits.getheader('C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/Gemini/MOO_0917-0700_gmos_r.fits')



# ------------------------task-5---------------------------------

data='C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/Gemini/'

r_band=Table.read(data+'r_new_file.cat',format='ascii.sextractor')
z_band=Table.read(data+'z_new_file.cat',format='ascii.sextractor')

r_and_z_cat=Table()

r_and_z_cat.add_columns()

'''

def create_r_cat(measuring_image,detection_image,config_file,cat_name,ZP):
    cat = f'sex {measuring_image}.fits,{detection_image}.fits -c {config_file}.sex -CATALOG_NAME {cat_name}.cat -MAG_ZEROPOINT {ZP}'
    create_r_cat = os.system(cat)
    return create_r_cat


#--------------create r_band catalog
create_r_cat('C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/MOO_1506+5136_gmos_r','C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/MOO_1506+5136_gmos_r','C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/T3_default','C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/r_band_cat',32.0)
r_band_cat = ascii.read('C:/Users/Farhan/Desktop/TUTORIAL-499-PDF/Tutorial_V/data/r_band_cat.cat')
print(r_band_cat)
'''




