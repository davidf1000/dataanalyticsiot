#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 17:17:00 2020

@author: davidfauzi
"""

import Adafruit_IO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import cv2
# set the filepath and load in a shapefile
fp = "ESRI/London_Borough_Excluding_MHW.shp"

map_df = gpd.read_file(fp)
print(map_df.head())
map_df.plot()
df= pd.read_csv("london-borough-profile.csv",header=0,engine='python')
df = df[['borough','Happiness_score_2011-14_(out_of_10)', 'Anxiety_score_2011-14_(out_of_10)', 'Population_density_(per_hectare)_2017', 'Mortality_rate_from_causes_considered_preventable_2012/14']]

# those are really terrible column names. let's rename them to something simpler
score = df.rename(index=str, columns={"Happiness_score_2011-14_(out_of_10)": "happiness",
                                      "Anxiety_score_2011-14_(out_of_10)": "anxiety",
                                      "Population_density_(per_hectare)_2017": "pop_density_per_hectare",
                                      "Mortality_rate_from_causes_considered_preventable_2012/14": 'mortality'})

# check dat dataframe
print("test")
print(score.head())


# join the geodataframe with the cleaned up csv dataframe
merged = map_df.set_index('NAME').join(score.set_index('borough'))


merged.head()
# set a variable that will call whatever column we want to visualise on the map
variable = 'pop_density_per_hectare'

# set the range for the choropleth
vmin, vmax = 120, 220

# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

# create map1024
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')

# Now we can customise and add annotations

# remove the axis
ax.axis('off')

# add a title
ax.set_title('Preventable death rate in London', \
              fontdict={'fontsize': '25',
                        'fontweight' : '3'})

# create an annotation for the  data source
ax.annotate('Source: London Datastore, 2014',
           xy=(0.1, .08), xycoords='figure fraction',
           horizontalalignment='left', verticalalignment='top',
           fontsize=10, color='#555555')

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)

# this will save the figure as a high-res png. you can also save as svg
fig.savefig('testmap.png', dpi=100)
img=cv2.imread('testmap.png')
resized=cv2.resize(img,(800,600))
cv2.imwrite("send.jpg",resized)
