# Tropical Storm Detector: 
## Analyzing NOAA Offshore Florida Buoy Data to Find Past Hurricanes
### COP 3530 Data Structures and Algorithms Final Project

__Problem:__
The National Oceanic and Atmospheric Administration’s (NOAA) moored buoys are essentially
sea weather stations. These stations collect a massive amount of data on the hourly oceanographic environment. They transit data on the wave height and period, barometric pressure, temperatures, and wind. As you can imagine, this data is essential to meteorology, environmental studies, and climate sciences. One valuable data set is wind gust recordings. Wind gusts are great indicators of tropical storms. If there are recorded wind gusts greater than 75mph (65 knots) then the buoy is likely in a hurricane. The wind data from the buoy is recorded real time approximately every ten minutes. There is an archive of this data (2015-2021) on The National Data Buoy Center, and the goal is to capture the k greatest recorded wind gusts (maybe greater than 75mph) from the Cape Canaveral coast buoy. The dates of these records may be days there was a tropical storm passing the Florida coast.  


__Motivation:__
It is very valuable to detect tropical storms offshore before they hit land masses because it allows
time for safety preparations. While this detection is only being performed on a static past data set, this application is a proof-of-concept for an advanced application that receives real-time streamed data from the buoy. The more advanced application could also theoretically analyze data from multiple Florida buoys on The National Data Buoy Center. 


__Features:__
The application should be able to load in the wind data and return the k top datetimes with the highest wind gust using two different data structures/algorithms.

__Data:__  
National Data Buoy Center (NDBC) 41010 - CANAVERAL EAST - 120NM East of Cape Canaveral
http://erddap.secoora.org/erddap/tabledap/wmo_41010.html

__Tools:__
* Python 
* Miniconda
* Pandas
* Flask
* HTML
* CSS
* Bootstrap


