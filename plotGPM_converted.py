#!/usr/bin/env python
#-*- coding: utf-8 -*-
# encoding: utf-8
from __future__ import unicode_literals

import matplotlib
matplotlib.use('agg')
from matplotlib.colors import LinearSegmentedColormap
import sys,getopt
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid import make_axes_locatable
import matplotlib.axes as maxes
import glob, os
import matplotlib.colors as mcolors
import matplotlib as mpl
import matplotlib.colors as colors
import multiprocessing
import time
from matplotlib.patches import Polygon
from wrf import getvar, interplevel, to_np, get_basemap, latlon_coords
from mpl_toolkits.basemap import Basemap, addcyclic
from scipy.ndimage.filters import minimum_filter, maximum_filter


def main(): 

    flist = sorted(glob.glob('*.nc'))


    for fs in flist:

        nc = Dataset(fs,'r')
        precip_tend = nc.variables['precip'][:]
        lon = nc.variables['Lon'][:]
        lat = nc.variables['Lat'][:]
        xlon, xlat = np.meshgrid(lon,lat)

        np.savetxt('xlon.txt',xlon)
        np.savetxt('xlat.txt',xlat)

        m = Basemap(llcrnrlon=np.min(xlon),llcrnrlat=np.min(xlat),urcrnrlon=np.max(xlon),urcrnrlat=np.max(xlat), resolution='h', projection='cyl')

        # This sets the standard grid point structure at full resolution
        x,y = m(xlon,xlat)

        # Set universal figure margins
        width = 10
        height = 8

        plt.figure(figsize=(width,height),dpi=300)
    #    plt.tight_layout()
        plt.rc("figure.subplot", left = .001)
        plt.rc("figure.subplot", right = .999)
        plt.rc("figure.subplot", bottom = .001)
        plt.rc("figure.subplot", top = .999)

        m.drawmeridians(range(0, 360, 4),labels=[1,0,0,1],fontsize=8, linewidth=0)
        m.drawparallels(range(-180, 180, 4),labels=[1,0,0,1],fontsize=8, linewidth=0)

        m.drawstates(color='gray', linewidth=0.25)
        m.drawcoastlines(color='k', linewidth=0.9)
        m.drawcountries(color='k', linewidth=0.9)

        cmap1,norm1,clevs1 = cm_precip()

        PRECIP=m.contourf(x,y,precip_tend,clevs1,cmap=cmap1,extend="max")

        PRECIP.cmap.set_under((1.0, 1.0, 1.0))
        PRECIP.cmap.set_over((100/255,0/255,86/255))

        m.colorbar(PRECIP)

        plt.savefig(fs[:-3]+'.png', dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close('all')
        plt.clf()
        plt.cla()



def cm_precip():

    a = [0.1,0.25,0.5,1,1.5,2,3,4,5,6,8,10,12,16,20,24,30,36,42,60]
    
    clevs = np.array(a)*12
    # Normalize the bin between 0 and 1 (uneven bins are important here)
    norm = [(float(i)-min(a))/(max(a)-min(a)) for i in a]

    C = np.array([[255,255,255],
                [0,250,76],
                [0,227,69],
                [0,203,61],
                [0,180,54],
                [0,156,47],
                [0,133,40],
                [0,109,32],
                [0,86,25],
                [254,250,79],
                [254,198,70],
                [254,146,62],
                [254,93,53],
                [254,41,44],
                [115,6,34],
                [128,5,44],
                [140,5,55],
                [180,3,110],
                [207,1,154],
                [234,0,199]])

#        print 'precip',len(a),len(C)
    # Create a tuple for every color indicating the normalized position on the colormap and the assigned color.
    COLORS = []
    for i, n in enumerate(norm):
        COLORS.append((n, np.array(C[i])/255.))

    # Create the colormap
    cmap = colors.LinearSegmentedColormap.from_list("precipitation", COLORS)

    return cmap,norm,clevs



def cnv_to_rgb(clist):

    newcolors = []
    for i in range(len(clist)):
        newcolors.append((float(clist[i][0])/255,float(clist[i][1])/255,float(clist[i][2])/255))

    return newcolors


    
if __name__ == '__main__':
    main()

