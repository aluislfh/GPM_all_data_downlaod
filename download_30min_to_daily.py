import os, sys, math, datetime

# Download GPM data (daily and 30 mins files)

def main(fecha,huser,hpass):

    yyyy = fecha[:4]
    mes = fecha[4:6]
    dj = str(datestdtojd(fecha))

    print(fecha, dj)

    # 24 horas
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDE.06/"+yyyy+"/"+mes+"/3B-DAY-E.MS.MRG.3IMERG."+fecha+"-S000000-E235959.V06.nc4")

    # 30 minutos
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S000000-E002959.0000.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S000000-E002959.0000.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S003000-E005959.0030.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S003000-E005959.0030.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S010000-E012959.0060.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S010000-E012959.0060.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S013000-E015959.0090.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S013000-E015959.0090.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S020000-E022959.0120.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S020000-E022959.0120.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S023000-E025959.0150.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S023000-E025959.0150.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S030000-E032959.0180.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S030000-E032959.0180.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S033000-E035959.0210.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S033000-E035959.0210.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S040000-E042959.0240.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S040000-E042959.0240.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S043000-E045959.0270.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S043000-E045959.0270.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S050000-E052959.0300.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S050000-E052959.0300.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S053000-E055959.0330.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S053000-E055959.0330.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S060000-E062959.0360.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S060000-E062959.0360.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S063000-E065959.0390.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S063000-E065959.0390.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S070000-E072959.0420.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S070000-E072959.0420.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S073000-E075959.0450.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S073000-E075959.0450.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S080000-E082959.0480.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S080000-E082959.0480.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S083000-E085959.0510.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S083000-E085959.0510.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S090000-E092959.0540.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S090000-E092959.0540.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S093000-E095959.0570.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S093000-E095959.0570.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S100000-E102959.0600.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S100000-E102959.0600.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S103000-E105959.0630.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S103000-E105959.0630.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S110000-E112959.0660.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S110000-E112959.0660.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S113000-E115959.0690.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S113000-E115959.0690.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S120000-E122959.0720.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S120000-E122959.0720.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S123000-E125959.0750.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S123000-E125959.0750.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S130000-E132959.0780.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S130000-E132959.0780.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S133000-E135959.0810.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S133000-E135959.0810.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S140000-E142959.0840.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S140000-E142959.0840.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S143000-E145959.0870.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S143000-E145959.0870.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S150000-E152959.0900.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S150000-E152959.0900.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S153000-E155959.0930.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S153000-E155959.0930.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S160000-E162959.0960.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S160000-E162959.0960.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S163000-E165959.0990.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S163000-E165959.0990.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S170000-E172959.1020.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S170000-E172959.1020.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S173000-E175959.1050.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S173000-E175959.1050.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S180000-E182959.1080.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S180000-E182959.1080.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S183000-E185959.1110.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S183000-E185959.1110.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S190000-E192959.1140.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S190000-E192959.1140.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S193000-E195959.1170.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S193000-E195959.1170.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S200000-E202959.1200.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S200000-E202959.1200.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S203000-E205959.1230.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S203000-E205959.1230.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S210000-E212959.1260.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S210000-E212959.1260.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S213000-E215959.1290.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S213000-E215959.1290.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S220000-E222959.1320.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S220000-E222959.1320.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S223000-E225959.1350.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S223000-E225959.1350.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S230000-E232959.1380.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S230000-E232959.1380.V06D.HDF5.xml")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S233000-E235959.1410.V06D.HDF5")
    os.system("wget -c --http-user="+huser+" --http-password="+hpass+" https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/"+yyyy+"/"+dj+"/3B-HHR-E.MS.MRG.3IMERG."+fecha+"-S233000-E235959.1410.V06D.HDF5.xml")

    
def datestdtojd(fecha):
    
    fmt='%Y%m%d'
    sdtdate = datetime.datetime.strptime(fecha, fmt)
    sdtdate = sdtdate.timetuple()
    jdate = sdtdate.tm_yday
    
    return(jdate)



if __name__ == '__main__':

    fecha = sys.argv[1]
    huser = sys.argv[2]
    hpass = sys.argv[3]
    
    main(fecha,huser,hpass)

