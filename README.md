# HWITW: How Weird is the Weather?

- Project: How Weird is the Weather?
- Authors: John McInnes <jamcinnes2@gmail.com>, Matt Jones <jones@nceas.ucsb.edu>
- License: Apache License 2.0

This is the general repository for managing files from How Weird is the Weather. It includes tools for downloading ERA5 reanalysis data from the Copernicus Data Service, and tools for statistical summarization of that data.

## Downloading CDS data

Download data from the Copernicus Climate Data Service (CDS)

This is a simple python utility for downloading data from Copernicus using their CDS API via the python client.

Dependencies include:

- cdsapi
- NetCDF4

CDS ERA5 data are broken into two products:

- 1950-1978: ERA 5 Back extension (28 years, at about 156GB per year, totalling around 4,368 GB)
- 1979-2021: ERA 5 (42 years, at about 136GB per year, totlling aroung 5,712 GB)

## Checksums

I also generated checksums for all downloaded files usinfg openssl and recorded those in `cds-checksums.csv` using a command like this:

```sh
fn="cds_era5_backext/1953/global-1953-2m_dewpoint_temperature.nc" openssl dgst -sha256 $fn | awk -F'[()=]' '{print $2 ",",  $1 "," $4}' >> cds-checksums.csv
```
