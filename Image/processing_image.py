from matplotlib.pyplot import imshow, plot, show
from tifffile import imread

answer = input('Type 1, 2, or 3\n')

if int(answer) == 1:
    IM = imread('2016_summer_XPD/Image/CdSeNP_000.tif')
elif int(answer) == 2:
    IM = imread('2016_summer_XPD/Image/CdSeNP_001.tif')
else:
    IM = imread('2016_summer_XPD/Image/Ni300K.tif')


imshow(IM)

show()
