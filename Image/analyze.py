#This file will allow for some simply analysis of the diffaction
#images provided

import matplotlib.pyplot as plt
from tifffile import imread

Cd = imread('2016_summer_XPD/Image/CdSeNP_000.tif')

#This function displays the region observed
def show_region(rb, re, cb, ce):
    plt.imshow(Cd)
    plt.axhline(y = rb)
    plt.axhline(y = re)
    plt.axvline(x = cb)
    plt.axvline(x = ce)
    plt.title('Region of intersection shows analyzed area')

    plt.show()

#This function calculates the average value
def average(rb, re, cb, ce):
    x = 0
    num = (re - rb)*(ce - cb)
    print('The number of pixels observed is ' + str(num))

    for i in range(rb, re + 1):
        for j in range(cb, ce + 1):
            x += Cd[i][j]

    print('The average intensity is ' + str(x/num))
    return x/num, num

#This function will find the standard deviation
def stan_dev(rb, re, cb, ce, avg, num):
    x = 0
    for i in range(rb, re + 1):
        for j in range(cb, ce + 1):
            x += (avg - Cd[i][j])**2
    
    std = (x/num)**0.5
    print('The standard deviation of this region is ' + str(std))

#This function finds the minimum value of the region and position
def find_min(rb, re, cb, ce):
    z = Cd[rb][cb]
    x = rb
    y = cb

    for i in range(rb + 1, re + 1):
        for j in range(cb + 1, ce + 1):
            if Cd[i][j] < z:
                z = Cd[i][j]
                x = i
                y = j
    
    print('The minimum is ' + str(z) + ' at ' + str(x) + 'x' + str(y))

#This function finds the maximum value of the region and position
def find_max(rb,re,cb,ce):
    z = Cd[rb][cb]
    x = rb
    y = cb

    for i in range(rb + 1, re + 1):
        for j in range(cb + 1, ce + 1):
            if Cd[i][j] > z:
                z = Cd[i][j]
                x = i
                y = j

    print('The maximum is ' + str(z) + ' at ' + str(x) + 'x' + str(y))

#This function initiates the entire process
def main():
    print('This file will give a 5 number printout for a certain region.')
    row_begin = int(input('Please input pixel row to begin at: '))
    row_end = int(input('Please input pixel row to end at: '))
    col_begin = int(input('Please input pixel column to begin at: '))
    col_end = int(input('Please input pixel column to end at: '))

    avg, num = average(row_begin, row_end, col_begin, col_end)
    stan_dev(row_begin, row_end, col_begin, col_end, avg, num)
    find_min(row_begin, row_end, col_begin, col_end)
    find_max(row_begin, row_end, col_begin, col_end)
    show_region(row_begin, row_end, col_begin, col_end)

main()


