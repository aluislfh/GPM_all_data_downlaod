<strong> GPM IMERG products </strong>

Link:
https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3

</br>

Download all GPM_IMERG data for specific day (accumulated precipitation in 24 hours and every 30 minutes)

To run put:

python download_30min_to_daily.py YYYYMMDD user password


</br>


Download GPM_IMERG monthly and daily data

To run put:

python download_daily_to_monthly.py user password


</br>


<strong>convert_gpm_hdf5_to_nc.py</strong> script is a tool to convert GPM monthly data in HDF5 format to NetCDF4 format (compatible with Climate Data Tools (IRI - https://github.com/rijaf-iri/CDT/))

</br>

<strong>convert_gpm_nc4_to_nc.py</strong> script is a tool to convert GPM daily data in NetCDF4 format to standard NetCDF4 format (compatible with Climate Data Tools (IRI - https://github.com/rijaf-iri/CDT/))
