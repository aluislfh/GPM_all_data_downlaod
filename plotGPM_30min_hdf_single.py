import os, glob, sys
import netCDF4 as nc
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from datetime import datetime, timedelta
import h5py as h5py


def main():

    lista = sorted(glob.glob('3B-HHR-E.MS.MRG.3IMERG.*.V06D.HDF5'))
    rain = np.zeros(shape=(1800, 3600))

    print('GPM List:', lista)

    for i in lista:
        dataset = h5py.File(i, 'r') # Change this to the proper path
        precip = dataset['Grid/precipitationCal'][0,:,:]
        precip = np.transpose(precip)
        rain = rain + precip

        theLats= dataset['Grid/lat'][:]
        theLons = dataset['Grid/lon'][:]

        map1 = Basemap(resolution='h',llcrnrlon=-87.5, llcrnrlat=16.5, urcrnrlon=-71.5, urcrnrlat=26 , projection='cyl')

        #=====================================================================================

        fplot(map1,'cuba',theLats,theLons,rain,[i])


def fplot(map,label,theLats,theLons,rain,lista):

    plt.figure(1, dpi=300)

    # Define the latitude and longitude data
    x, y = np.float32(np.meshgrid(theLons, theLats))

    # Mask the values less than 0 because there is no data to plot.
    masked_array = np.ma.masked_where(rain < 0,rain)

    map.drawstates(color='gray', linewidth=0.1)
    map.drawcoastlines(color='k', linewidth=0.6)
    map.drawcountries(color='k', linewidth=0.6)

    if label == 'cuba':
        map.drawmeridians(range(0, 360, 2),labels=[1,0,0,1],fontsize=6, linewidth=0)
        map.drawparallels(range(-180, 180, 2),labels=[1,0,0,1],fontsize=6, linewidth=0)
    else:
        map.drawmeridians(range(0, 360, 5),labels=[1,0,0,1],fontsize=6, linewidth=0)
        map.drawparallels(range(-180, 180, 5),labels=[1,0,0,1],fontsize=6, linewidth=0)

    cmap1,norm1,clevs1 = cm_precip()

    cs = map.contourf(x,y,masked_array[:,:],clevs1,cmap=cmap1,latlon=True,extend="max")
    print(np.max(masked_array[:,:]))

    cs.cmap.set_under((1.0, 1.0, 1.0))
    cs.cmap.set_over((0.39,0,0.34)) # (100/255,0/255,86/255)

    cbar = map.colorbar(cs,location='right')

    ndate = lista[0].split('.')[4]
    sutc = datetime(int(ndate[:4]),int(ndate[4:6]),int(ndate[6:8]),int(ndate[10:12]),int(ndate[12:14]),int(ndate[14:16]))
    ndate = lista[-1].split('.')[4]
    eutc = datetime(int(ndate[:4]),int(ndate[4:6]),int(ndate[6:8]),int(ndate[18:20]),int(ndate[20:22]),int(ndate[22:24]))

    diff = sutc - eutc
    tdifout = np.abs(diff.total_seconds()/3600)    # seconds to hour 

    nh = str(int(tdifout)).zfill(2)

    plt.title('PRODUCTO DE ESTIMACION MULTISATELITE DE LA PRECIPITACION (GPM_3IMERGDE)\n ACUMULADOS EN 30 MIN (MM/30MIN) ENTRE '+str(sutc)[:-3]+' - '+str(eutc)[:-3]+ ' [UTC]',fontsize=8)

    np.savetxt('grid_lons.txt',x)
    np.savetxt('grid_lats.txt',y)
    np.savetxt('grid_rain.txt',masked_array[:,:])

    plt.savefig(lista[0][:-3]+'.png',bbox_inches='tight',dpi=300)
    plt.clf()
    plt.cla()
    plt.close('all')


# Plot every masked value as white
def cm_precip():
    """
    Range of values:
        metric: 0 to 762 millimeters
        english: 0 to 30 inches
    """

    a = [0.1,0.25,0.5,1,1.5,2,3,4,6,8,10,15,20,24,40,50,60,70,80,100]
    clevs = np.array(a)

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

    # Create a tuple for every color indicating the normalized position on the colormap and the assigned color.
    COLORS = []
    for i, n in enumerate(norm):
        COLORS.append((n, np.array(C[i])/255.))

    # Create the colormap
    cmap = colors.LinearSegmentedColormap.from_list("precipitation", COLORS)

    return cmap,norm,clevs


main()

