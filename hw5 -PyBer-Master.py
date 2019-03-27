#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)

city_data_to_load = "city_data.csv"

ride_data_to_load = "ride_data.csv"

# Read the City and Ride Data

city_data = pd.read_csv(city_data_to_load)

city_data.head()


# In[3]:


ride_data = pd.read_csv(ride_data_to_load)

ride_data.head()


# In[4]:


# Combine the data into a single dataset

ride_data_complete = pd.merge(city_data, ride_data, how="left", on=["city"])  

# Display the data table for preview

ride_data_complete.head()


# In[5]:


#our objective is to build a Bubble Plot that showcases the relationship between four key variables:

#Average Fare ($) Per City
#Total Number of Rides Per City
#Total Number of Drivers Per City
#City Type (Urban, Suburban, Rural)


# In[6]:



# Obtain the x and y coordinates for each of the three city types

# X-ccordinate is total # of rides per city e.g. urban_trips
# y-coordinate is average fare e.g. urban_fare
# s (bubble size) -coordinate is the # of drivers for each city e.g. urban_drivers

# Calculate the number of trips, the average ride fare and the avg. # drivers
# for all 3 city types: Urban, Suburban & rural

urban_data = ride_data_complete.loc[ride_data_complete["type"] == "Urban"]

urban_trips=urban_data.groupby(["city"]).count()["ride_id"]

urban_fare=urban_data.groupby(["city"]).mean()["fare"]

urban_drivers=urban_data.groupby(["city"]).mean()["driver_count"]


suburban_data = ride_data_complete.loc[ride_data_complete["type"] == "Suburban"]

suburban_trips=suburban_data.groupby(["city"]).count()["ride_id"]

suburban_fare=suburban_data.groupby(["city"]).mean()["fare"]

suburban_drivers=suburban_data.groupby(["city"]).mean()["driver_count"]


rural_data = ride_data_complete.loc[ride_data_complete["type"] == "Rural"]

rural_trips=rural_data.groupby(["city"]).count()["ride_id"]

rural_fare=rural_data.groupby(["city"]).mean()["fare"]

rural_drivers=rural_data.groupby(["city"]).mean()["driver_count"]


# Build the scatter plots for each city types

plt.scatter(urban_trips, urban_fare, s=urban_drivers*5, alpha=0.40, label="Urban", edgecolors="black")

plt.scatter(suburban_trips, suburban_fare, s=suburban_drivers*5, alpha=0.40, label="Suburban", edgecolors="black")

plt.scatter(rural_trips, rural_fare, s=rural_drivers*5, alpha=0.40, label="Rural", edgecolors="black")

# Calculate axis limits

plt.xlim(0, 40)

#plt.ylim(0, y_limit)

# Incorporate the other graph properties

plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides per city")
plt.ylabel("Average Fare ($)")

           
# Create a legend

lgnd = plt.legend(fontsize="small", mode="Expanded",
                 numpoints=1, scatterpoints=1,
                 loc="best", title="City Types",
                 labelspacing=0.5)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
lgnd.legendHandles[2]._sizes = [30]


# Incorporate a text label regarding circle size

plt.text(12,42, 'Larger circles mean more drivers', size='small', weight='light')

# Save Figure

plt.savefig("Pyber_ride_sharing_data.png")

plt.show()


# In[7]:


#Total Fares by City Type

# Calculate Type Percents

total_urban_fares=urban_data.groupby(["type"]).sum()["fare"]
#total_urban_fares
total_suburban_fares=suburban_data.groupby(["type"]).sum()["fare"]
#total_suburban_fares
total_rural_fares=rural_data.groupby(["type"]).sum()["fare"]
#total_rural_fares

# Build Pie Chart

# labels - Urban, Rural, Suburban

labels = ["Urban", "Rural", "Suburban"]

# The values of each section of the pie chart

sizes = [total_urban_fares, total_rural_fares, total_suburban_fares]

# The colors of each section of the pie chart
colors = ["red", "yellow", "lightcoral"]
          
# Tells matplotlib to separate the "Urban" section from the others

explode = (0, 0.1, 0.1)
          
plt.title("% of Total Fares by City Type")


plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.2f%%", shadow=False, startangle=90)

plt.axis("equal")

# Save Figure

plt.savefig("%Total_fares_city_type.png")
          
plt.show()


# In[8]:


#Total Rides by City Type

#Calculate Type Percents

total_urban_rides=urban_data.groupby(["type"]).count()["ride_id"]
                                                      
total_suburban_rides=suburban_data.groupby(["type"]).count()["ride_id"]

total_rural_rides=rural_data.groupby(["type"]).count()["ride_id"]

#Build Pie Chart

#Labels - Urban, Rural, Suburban

labels = ["Urban", "Rural", "Suburban"]
          
sizes = [total_urban_rides, total_rural_rides, total_suburban_rides] 
          
#The colors of each section of the pie chart
colors = ["red", "yellow", "lightcoral"]
          
#Tells matplotlib to seperate the "Urban" section from the others
explode = (0, 0.1, 0.1)
          
plt.title("% of Total Rides by City Type")
          
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.2f%%", shadow=False, startangle=90)
          
plt.axis("equal")
          
# Save Figure

plt.savefig("%Total_rides_city_type.png")
          
plt.show()
          


# In[8]:


#Total Drivers by City Type

## Calculate Type Percents

urban_drivers=urban_data.groupby(["type", "city"]).mean()["driver_count"]
total_urban_drivers = urban_drivers.sum()
total_urban_drivers

suburban_drivers=suburban_data.groupby(["type","city"]).mean()["driver_count"]
total_suburban_drivers = suburban_drivers.sum()
total_suburban_drivers

rural_drivers=rural_data.groupby(["type", "city"]).mean()["driver_count"]
total_rural_drivers = rural_drivers.sum()
total_rural_drivers


# Build Pie Chart

# labels - Urban, Rural, Suburban

labels = ["Urban", "Rural", "Suburban"]

# Build Pie Charts

labels = ["Urban", "Rural", "Suburban"]

# The values of each section of the pie chart

sizes = [total_urban_drivers, total_rural_drivers, total_suburban_drivers]

# The colors of each section of the pie chart
colors = ["red", "yellow", "lightcoral"]


# Tells matplotlib to seperate the "Urban" section from the others
explode = (0, 0.1, 0.1)
          
plt.title("% of Total Drivers by City Type")

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.2f%%", shadow=False, startangle=90)

plt.axis("equal")
        
# Save Figure

plt.savefig("%Total_drivers_city_type.png")
          
plt.show()

