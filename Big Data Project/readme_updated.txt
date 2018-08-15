For this project we used uber and taxi data from May 2015. The files were obtained 
from:

Taxi: https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2015-05.csv
uber: https://github.com/fivethirtyeight/uber-tlc-foil-response
taxi zones: http://www.nyc.gov/html/exit-page.html?url=https://s3.amazonaws.com/nyc-tlc/misc/taxi_zones.zip
Map Notebook: map_analysis.ipynbfile.txt: combined output file for the processed uber data, saved in hive_combine on hdfs
Merge notebook: to merge the 5 output files for uber data, obtained from running the map-reducer during the pre-processing time.

In python the taxi zones were combined with the yellow taxi data. The uber file 
is uber-raw-data-janjune-15.zip.csv. I converted the days to a datetime and filtered
for the month of May. This file was then combined with a taxi zone .lookup csv in 
the same repository. The Uber data was analyzed in the similar way. The data was aggregated by the hour and then transferred it to HDFS. The files were saved as taxi_mn and uber_mn.

In hdfs we created a project folder where the data files were placed. Based on the taxi zones, taxi ride count, uber ride count and the ratio of the two were aggregated and added to a new table. In addition to that we analyzed the output data from Hive analysis and used it for creating maps in Python using Geopandas. The maps essentially tell you a compelling story of how many trip are taken from each taxi zone. 
