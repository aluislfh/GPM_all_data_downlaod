#! /usr/bin/python

import numpy as np
import netCDF4
import sys, glob, os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import ListedColormap
from scipy.interpolate import griddata
import datetime
import time
import multiprocessing
import matplotlib
import h5py as h5py
import calendar


def main():

    #------------------------------------------------------------------------------
    # CPU cores number
    #------------------------------------------------------------------------------
    PROCESS_LIMIT = 8


    lista = glob.glob('3B-MO.MS.MRG.3IMERG.*.V06B.HDF5')

    for i in sorted(lista):

        print(i)

#        # serial
##        proc(i)

        # paralelo
        process=multiprocessing.Process(target=proc,args=(lista,i))
        while(len(multiprocessing.active_children()) == PROCESS_LIMIT):
            time.sleep(1)
        process.start()


def proc(lista,i):

        print("Converting: "+i)

        dataset = h5py.File(i, 'r') # Change this to the proper path
        precip1 = dataset['Grid/precipitation'][0,:,:]
        precip0 = np.transpose(precip1)

        theLats0= dataset['Grid/lat'][:]
        theLons0 = dataset['Grid/lon'][:]

        # Define the latitude and longitude data
        x, y = np.float32(np.meshgrid(theLons0, theLats0))

        xi, yi, precip, theLons, theLats = crop(x, y, theLons0, theLats0, precip0)

        # Mask the values less than 0 because there is no data to plot.
        masked_array = np.ma.masked_where(precip < 0,precip)

        hdf52nc(i, theLons, theLats, xi, yi, masked_array[:,:])



def crop(x, y, theLons0, theLats0, precip0):

    i_arch, j_arch = ([], [])

    for i in range(precip0.shape[0]):
        for j in range(precip0.shape[0]):

            # Guyana
#            if y[i,j] >= 0.48004 and y[i,j] <= 9.50421 and x[i,j] >= -62.37943 and x[i,j] <= -55.78876:
            # Cuba
            if y[i,j] >= 19.58 and y[i,j] <= 23.48 and x[i,j] >= -85.02 and x[i,j] <= -73.84:

                i_arch.append(i)
                j_arch.append(j)

    imin, imax = (int(np.min(i_arch)), int(np.max(i_arch)))
    jmin, jmax = (int(np.min(j_arch)), int(np.max(j_arch)))

    return x[imin:imax, jmin:jmax], y[imin:imax, jmin:jmax], precip0[imin:imax, jmin:jmax], theLons0[jmin:jmax], theLats0[imin:imax]


def hdf52nc(name,theLons, theLats,lons,lats,data):

    # 3B-MO.MS.MRG.3IMERG.20000601-S000000-E235959.06.V06B.HDF5
    iyy, imm, idd, ihh = (name.split('.')[4][:4], name.split('.')[4][4:6], name.split('.')[4][6:8], name.split('.')[4][10:12])
    dates = [datetime.datetime(int(iyy), int(imm), int(idd), int(ihh), 0, 0)]


    # Create the new netCDF file
#    outfilename = name[:-5]+'.nc'
    outfilename = './gpm_imerg_'+iyy+imm+'.nc'

    fid = netCDF4.Dataset(outfilename,'w', format='NETCDF4_CLASSIC')

    print(theLats,theLons)

    # Define the dimensions

    time = fid.createDimension('time', len(dates))
    lon  = fid.createDimension('lon', len(theLons))
    lat  = fid.createDimension('lat', len(theLats))

    # Create global attributes
    fid.title          = 'Monthly Gridded '+name
    fid.description    = 'GPM-IMERG Product'
    fid.institution    = "NASA"
    fid.acknowledgment = "NASA"

    # Create variable TIMES
    times = fid.createVariable('time', np.float64, ('time',))
    times.calendar = 'standard'
    times.units = 'hours since '+iyy+'-'+imm+'-01 00:00:00'

    times[:] = netCDF4.date2num(dates, units = times.units, calendar = times.calendar)

    fid.variables['time'] = times[:]
    fid.variables['time'].standard_name='time'
    fid.variables['time'].units = 'hours since '+iyy+'-'+imm+'-01 00:00:00'
    fid.variables['time'].comment='Monthly Precipitation Data'

    # Create variable LONGITUDES
    longitudes = fid.createVariable('lon', np.float32, ('lon'))
    fid.variables['lon'].standard_name='longitude'
    fid.variables['lon'].long_name='longitude'
    fid.variables['lon'].units='degrees_east'
    fid.variables['lon'].comment='Longitude'
    fid.variables['lon'].axis='X'
    fid.variables['lon'][:] = theLons

    # Create variable LATITUDES
    latitudes = fid.createVariable('lat', np.float32, ('lat'))
    fid.variables['lat'].standard_name='latitude'
    fid.variables['lat'].long_name='latitude'
    fid.variables['lat'].units='degrees_north'
    fid.variables['lat'].comment='Latitude'
    fid.variables['lat'].axis='Y'
    fid.variables['lat'][:] = theLats

    # Create variable VAR
    nc_var = fid.createVariable('precip', np.float32,('time','lat', 'lon')) 

    fid.variables['precip'][0,:,:] = data[:,:] * calendar.monthrange(int(iyy),int(imm))[1] * 24
    fid.variables['precip'].units='mm/months'
    fid.variables['precip'].missing_value=-999.0
    fid.variables['precip'].description='GPM Precipitation'


    # Closing file
    fid.close()


main()





