# 🌍 COVID-19 Daily Positive Cases Animation 


![Image](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25013%20Global%20spread%20of%20COVID-19%20over%20time/Dynamic%20COVID%2019%20Map%20small.gif)  

![Date](https://img.shields.io/badge/16/09/2025-17/09/2025-blue) 
![Location](https://img.shields.io/badge/Location-Rajshahi-green) 
---

## 📝 Overview
This project visualizes the global spread of COVID-19 over time by creating an **animated world map** showing the **daily increase in confirmed cases** using **Geospatial Python**.

---  

## 🛠️ Tools & Technologies
![GeoPy](https://img.shields.io/badge/Geospatial-Python-red)  
![GIS](https://img.shields.io/badge/GIS-ArcGIS-green) 

---
## 📂 Dataset
**Source:** [Johns Hopkins University CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)  
File used: `time_series_covid19_confirmed_global.csv`

This dataset contains daily cumulative confirmed case counts per country.
---
## 🐍 Code

Import libraries
``` python
import pandas as pd
import geopandas as gpd
import PIL
import io
import matplotlib.pyplot as plt
```
import data and process them
``` python
data = pd.read_csv("time_series_covid19_confirmed_global.csv")
data1 = data.drop(['Province/State','Lat','Long'], axis=1).groupby('Country/Region').sum()
data_transposed = data1.T
print(data_transposed.columns)
```
4 Countries comparison data
``` python
ax = data_transposed.plot(y = ['Australia', 'China', 'US', 'India', 'Bangladesh'], figsize = (12,8))



# Map beautification
ax.set_title("Confirmed Coronavisus Cases Comparison", 
             fontdict = {'fontsize':18}, pad = 12.5)
# remove axis
#ax.set_axis_off()

# move legend
#ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

# Get the figure from the axes
fig = ax.get_figure()
# Save the figure
fig.savefig("4 country comparison.png", dpi=300, bbox_inches='tight')

```
![2](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25013%20Global%20spread%20of%20COVID-19%20over%20time/4%20country%20comparison.png)  
Import World shapefile

``` python
# Read shapefile
world = gpd.read_file('World_Map.shp')
world.plot()

# Plot
ax = world.plot(figsize=(12,8), edgecolor='black', color='lightblue')

# Optional: add title
ax.set_title("World Map", fontsize=18, pad=12)

# Optional: remove axes
ax.set_axis_off()

# Get figure object
fig = ax.get_figure()
fig.savefig("World_Map.png", dpi=300, bbox_inches='tight')

```
Edit before join
``` python
world.set_index('NAME')
print(world.columns)
world.replace('Viet Nam','Vietnam', inplace = True)
world.replace('Brunei Darussalam','Brunei', inplace = True)
world.replace('Cape Verde', 'Cabo Verde', inplace = True)
world.replace('Democratic Republic of the Congo', 'Congo (Kinshasa)', inplace = True)
world.replace('Congo','Congo (Brazzaville)', inplace = True)
world.replace('Iran (Islamic Republic of)','Iran ', inplace = True)
world.replace('Korea, Republic of', 'Korea, South', inplace = True)
world.replace('United States','US', inplace = True)
world.replace('Palestine', 'West Bank and Gaza', inplace = True)
```
Join data
``` python
#merge
merge = world.join(data1, on = "NAME", how = "right" )
merge.head()
```
Plot a day
``` python
ax = merge.plot(column = "6/15/20",
               cmap = 'OrRd',
               figsize = (10,10),
               legend = True,
               edgecolor = 'black',
               linewidth = 0.4,
               scheme = 'user_defined',
               classification_kwds = {'bins': [10,20,50,100,500,1000,5000,10000,500000]})

# Map beautification
ax.set_title("Total Confirmed Coronavisus Cases (15/06/20)", 
             fontdict = {'fontsize':18}, pad = 12.5)
# remove axis
ax.set_axis_off()

# move legend
ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

# Save figure
fig = ax.get_figure()
fig.savefig("COVID_Map_6_15_20.png", dpi=300, bbox_inches='tight')
```
![1](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25013%20Global%20spread%20of%20COVID-19%20over%20time/COVID_Map_6_15_20.png)  
Plot and save gif
``` python
# empty list
image_frames = []


for dates in merge.columns.to_list()[2:366]:

    #plot
    ax1 = merge.plot(column = dates,
                   cmap = 'OrRd',
                   figsize = (14,14),
                   legend = True,
                   edgecolor = 'black',
                   linewidth = 0.4,
                   scheme = 'user_defined',
                   classification_kwds = {'bins': [10,20,50,100,500,1000,5000,10000,500000]})
    
    # Map beautification
    ax1.set_title("Total Confirmed Coronavisus Cases: " + dates, 
                 fontdict = {'fontsize':18}, pad = 12.5)
    
    ax1.text(0.5, -0.05, "Imtiaj Iqbal Mahfuj", fontsize=10, ha='center', transform=ax1.transAxes)
    
    # remove axis
    ax1.set_axis_off()
    
    # move legend
    ax1.get_legend().set_bbox_to_anchor((0.18, 0.6))

    img = ax1.get_figure()

    f = io.BytesIO()
    img.savefig(f, format = 'png', bbox_inches = 'tight', dpi=300)
    f.seek(0)
    image_frames.append(PIL.Image.open(f))


# Create GIF
image_frames[0].save("Dynamic COVID 19 Map.gif", format = "GIF",
                    append_images = image_frames[1:],
                    save_all = True, duration = 100, 
                    loop = 1)

f.close()
```
![2](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25013%20Global%20spread%20of%20COVID-19%20over%20time/Dynamic%20COVID%2019%20Map%20small.gif)  
---

## ⚙️ Tools & Libraries
- **pandas** – for data manipulation and time series handling  
- **geopandas** – for handling country geometries and geospatial operations  
- **matplotlib** – for plotting and creating map frames  
- **PIL (Pillow)** – for combining frames into a smooth GIF animation  
- **io** – for in-memory image handling

---

## 🧠 What It Does
- Loads the daily confirmed COVID-19 data  
- Calculates the daily increase in positive cases  
- Joins data with world country boundaries using GeoPandas  
- Creates a series of daily choropleth maps  
- Compiles the images into an animated GIF showing how the pandemic spread globally over time


---

## 📎 Links
- 🔗 [See more](https://www.linkedin.com/posts/imtiajiqbalmahfuj_johnsabrhopkins-activity-7373465359313649666-vE4t?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)  

---


## 🏁 How to Run
1. Clone this repository  
2. Place `time_series_covid19_confirmed_global.csv` inside the project folder  
3. Run the main Python script:

---

```bash
python covid_animation.py
```

## 🔖 Tags
`Geospatial Python` `Python`





