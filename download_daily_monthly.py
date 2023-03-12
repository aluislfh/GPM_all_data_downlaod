import os, sys, math
import datetime as dt
import multiprocessing
import time


# Download GPM_IMERG monthly and daily data

# To run put:

# python download_daily_monthly.py user password


#------------------------------------------------------------------------------
# CPU cores number
#------------------------------------------------------------------------------

PROCESS_LIMIT = 8

wdir = '/home/adrian/NWP/GPM/download_scripts'

os.system('mkdir -p '+wdir+'/monthly')
os.system('mkdir -p '+wdir+'/daily')


def start(PROCESS_LIMIT,wdir):

    date = dt.datetime(2000,6,1,0)
    date1 = date + dt.timedelta(hours=24)
    date2 = dt.datetime(2023,3,12,0)

    for i in range(31*12*24): # dd, mm, yyyy

        dates=str(date).split()
        dates=str(dates[0] + '_' + dates[1])
        
        YYYY0 = str(dates[0:4])
        MM0   = str(dates[5:7])
        DD0   = str(dates[8:10])
        HH0   = str(dates[11:13])

        dates=str(date1).split()
        dates=str(dates[0] + '_' + dates[1])

        YYYY1 = str(dates[0:4])
        MM1   = str(dates[5:7])
        DD1   = str(dates[8:10])
        HH1   = str(dates[11:13])

        # # serial
        # main(YYYY0+MM0+DD0, sys.argv[1], sys.argv[2], wdir)  # date, user, password

        # paralelo
        process=multiprocessing.Process(target=main,args=(YYYY0+MM0+DD0, sys.argv[1], sys.argv[2], wdir))
        while(len(multiprocessing.active_children()) == PROCESS_LIMIT):
            time.sleep(1)
        process.start()
        
        date += dt.timedelta(hours=24)
        date1 = date + dt.timedelta(hours=24)

        if date == date2:
            break


def main(fecha, huser, hpass, wdir):

    yyyy = fecha[:4]
    mes = fecha[4:6]
    day = fecha[6:]
    dj = str(datestdtojd(fecha))

    print(fecha, dj)

    #================================================================
    # diarios
    #================================================================

    # https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDL.06/2023/03/3B-DAY-L.MS.MRG.3IMERG.20230311-S000000-E235959.V06.nc4

    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" -O "+wdir+"/daily"+"/3B-DAY-L.MS.MRG.3IMERG."+fecha+"-S000000-E235959.V06.nc4 https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDL.06/"+yyyy+"/"+mes+"/3B-DAY-L.MS.MRG.3IMERG."+fecha+"-S000000-E235959.V06.nc4")


    #================================================================
    # mensuales
    #================================================================

    # https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGM.06/ 2000/3B-MO.MS.MRG.3IMERG.20000601-S000000-E235959.06.V06B.HDF5

    if day == '01':

        os.system("wget -c --http-user="+huser+" --http-password="+hpass+" -O "+wdir+"/monthly"+"/3B-MO.MS.MRG.3IMERG."+fecha+"-S000000-E235959."+mes+".V06B.HDF5 https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGM.06/"+yyyy+"/3B-MO.MS.MRG.3IMERG."+fecha+"-S000000-E235959."+mes+".V06B.HDF5")
 



def datestdtojd(fecha):
    fmt='%Y%m%d'
    sdtdate = dt.datetime.strptime(fecha, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    return(jdate)




if __name__ == '__main__':
    start(PROCESS_LIMIT, wdir)