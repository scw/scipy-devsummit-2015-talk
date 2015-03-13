import netCDF4
nc = netCDF4.Dataset('data/test.nc', 'r', format='NETCDF4')
print nc.file_format
# outputs: NETCDF3_CLASSIC
nc.close()
