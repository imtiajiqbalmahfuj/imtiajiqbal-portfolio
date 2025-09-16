# 🌍 Global Carbon Dioxide Emissions 2018
### Mapping the World’s Carbon Dioxide Emissions Using Geospatial Python  

![Map Preview](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/_co2_emissions_final_map.png)  

![Date](https://img.shields.io/badge/16/09/2025-16/09/2025-blue) 
![Location](https://img.shields.io/badge/Location-Global-green) 
---

## 📝 Overview
This project visualizes **global carbon dioxide (CO₂) emissions for 2018** using high-resolution gridded data from the **EDGAR v6.0 dataset** (Crippa et al., 2021).  
Each dot represents a 0.1° x 0.1° grid cell with an emission value (in tons/year).  
The visualization highlights global hotspots like **China, India, North America, and Europe**, while even showing **major shipping lanes and air traffic routes** as glowing streaks on the map.

---

## 🛠️ Tools & Technologies
![GeoPy](https://img.shields.io/badge/Geospatial-Python-red)  
![GIS](https://img.shields.io/badge/GIS-Cartopy-green) 
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib-blue)  
![Geospatial](https://img.shields.io/badge/Geospatial-Data%20Science-lightgrey)  

**Main Libraries:**  
- `pandas` — For reading and cleaning the CSV dataset  
- `geopandas` — For creating GeoDataFrame and handling spatial geometry  
- `shapely` — To convert latitude/longitude to Point geometries  
- `matplotlib` — For plotting, colorbars, and figure styling  
- `cartopy` — To reproject data into Robinson projection  
- `BoundaryNorm` — For custom color scale based on scientific thresholds

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| 1. Data Collection | Downloaded `v50_CO2_excl_short-cycle_org_C_2018.txt` from EDGAR v6.0 (Crippa et al., 2021). |
| 2. Preprocessing   | Read CSV into pandas, renamed columns, sorted values, and explored emission ranges. |
| 3. Analysis        | Created scatter plots of emission intensity, applied `LogNorm` scaling to handle skewed data. |
| 4. Visualization   | Converted to GeoDataFrame, applied `Robinson` projection using Cartopy, applied custom `afmhot` color scheme with `BoundaryNorm` for clear emission classification. |

---

## 📊 Codes & Results

Install packages
``` python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import geopandas as gpd
from shapely.geometry import Point
from cartopy import crs as ccrs
from matplotlib import cm
from matplotlib.colors import ListedColormap
```
Read Data
``` python
data = "Data/v50_CO2_excl_short-cycle_org_C_2018.txt"
co2 = pd.read_csv(data, sep=";", skiprows=2)

co2
```
<img width="298" height="203" alt="image" src="https://github.com/user-attachments/assets/11715a72-95ef-4732-a1ce-e82fba48f50b" />

Refine Data
``` python
# Rename the column
co2 = co2.rename(columns={"emission 2018 (tons)": "emission"})
# Lowest and highest
co2 = co2.sort_values('emission', ascending=False)
co2.head(10)
```
<img width="241" height="333" alt="image" src="https://github.com/user-attachments/assets/d6cc6c2f-a5e1-46d8-8d5b-069578310baa" />

Initial plotting with matplotlib
``` python
fig, ax = plt.subplots(figsize = (10,6))
ax.scatter(co2['lon'], co2['lat'], s=0.05,  edgecolors='none')

fig.savefig("1_outline_map.png", dpi=300, bbox_inches='tight')

plt.show()
```

![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/1_outline_map.png)

Colorbar
``` python
fig, ax = plt.subplots(figsize = (12,6))
plot = ax.scatter(co2['lon'], co2['lat'], c=co2['emission'], s=0.05,  edgecolors='none')
plt.colorbar(plot)

fig.savefig("2_colorbar_map.png", dpi=300, bbox_inches='tight')

plt.show()
```

![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/2_colorbar_map.png)

``` python
print(co2.emission.value_counts())
print()
print("Min value: ", np.amin(co2.emission))
print("Max value: ", np.amax(co2.emission))
```
<img width="766" height="270" alt="image" src="https://github.com/user-attachments/assets/e6b409b6-ce83-4791-8a5d-a0cfe3fe0658" />

Plotting the data with logarithmic calc
``` Python
fig, ax = plt.subplots(figsize = (12,6))
plot = ax.scatter(co2['lon'], co2['lat'], c=co2['emission'], norm=colors.LogNorm(),  s=0.05,  edgecolors='none')
plt.colorbar(plot)

fig.savefig("3_AFTERLOG_MAP.png", dpi=300, bbox_inches='tight')

plt.show()
```
![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/3_AFTERLOG_MAP.png)

Plotting
``` python
fig, ax = plt.subplots(figsize = (12,6))
plot = ax.scatter(co2['lon'], co2['lat'], c=co2['emission'], 
                  norm=colors.LogNorm(),  s=0.05,  edgecolors='none',
                 cmap='afmhot_r')
plt.colorbar(plot)

fig.savefig("4_plot1.png", dpi=300, bbox_inches='tight')

plt.show()
```

![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/4_plot1.png)

Plotting with beautification and saving
``` python
# Plot
fig, ax = plt.subplots(figsize = (12,6))

# Scatter with log color scaling
plot = ax.scatter(co2['lon'], co2['lat'], c=co2['emission'], 
                  norm=colors.LogNorm(),  s=0.05,  edgecolors='none',
                 cmap='afmhot_r')

# Colorbar
cbar = plt.colorbar(plot, ax=ax, orientation='vertical', shrink=0.7, pad=0.02)
cbar.set_label('Emission (tons)', fontsize=10)

# Title and credit
ax.set_title('Global CO₂ Emissions (2018)', fontsize=16, pad=15)
ax.text(0.5, -.09, 'Created by: Imtiaj Iqbal Mahfuj', ha='center', 
        fontsize=9, color='gray', transform=ax.transAxes)

# Clean up map appearance
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
#ax.set_facecolor('black')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
ax.grid(False)

fig.savefig("5_beautyplot.png", dpi=300, bbox_inches='tight')

plt.show()
```

![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/5_beautyplot.png)

Reprojected Map
``` python
#import geopandas as gpd
#from shapely.geometry import Point

geometry = [Point(xy) for xy in zip(co2['lon'], co2['lat'])]
geodata = gpd.GeoDataFrame(co2, crs="EPSG:4326", geometry=geometry)

# Reprojection

#from cartopy import crs as ccrs
fig, ax = plt.subplots(figsize = (12,6), facecolor='black', 
                       subplot_kw={'projection': ccrs.Robinson()})
ax.patch.set_facecolor('black')

ax = geodata.plot(ax=ax, column='emission', transform=ccrs.PlateCarree(),
                  cmap='afmhot', norm=colors.LogNorm(), s=0.05, edgecolors='none')

plt.setp(ax.spines.values(), color='black')
plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')
ax.set_ylim(-8000000, 9000000)

# Title and credit
ax.set_title('Global CO₂ Emissions (2018)', fontsize=16, pad=15, color = 'white')
txt = ax.text(0.5, .02, 'Created by: Imtiaj Iqbal Mahfuj', ha='center', 
              size=6,
              color='white',
              transform = ax.transAxes)

fig.savefig("6_reprojected_map.png", dpi=300, bbox_inches='tight')

plt.show()
```

![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/6_reprojected_map.png)

Design Colors
``` python
# Design colors

#from matplotlib import cm
#from matplotlib.colors import ListedColormap

our_cmap = cm.get_cmap('afmhot', 11)
newcolors = our_cmap(np.linspace(0, 1, 11))
newcolors = newcolors[1:]

black = np.array([0.0, 0.0, 0.0, 1.0])
#newcolors[:1, :] = black
our_cmap = ListedColormap(newcolors)
bounds = [0.0, 0.06, 6, 60, 600, 3000, 6000, 24000, 45000, 120000]
norm = colors.BoundaryNorm(bounds, our_cmap.N)

gradient = np.linspace(0, 1, 10)
gradient = np.vstack((gradient, gradient))
plt.imshow(gradient, aspect='auto', cmap=our_cmap)
plt.axis('off')

fig.savefig("7_new colors.png", dpi=300, bbox_inches='tight')

plt.show()
```
Plotting with New Colors
``` python
# Plotting with new color

#from cartopy import crs as ccrs
fig, ax = plt.subplots(figsize = (12,6), facecolor='black', 
                       subplot_kw={'projection': ccrs.Robinson()})
ax.patch.set_facecolor('black')

ax = geodata.plot(ax=ax, column='emission', transform=ccrs.PlateCarree(),
                  cmap=our_cmap, norm=norm, s=0.05, alpha=1, edgecolors='none')

plt.setp(ax.spines.values(), color='black')
plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')
ax.set_ylim(-8000000, 9000000)

# Title and credit
ax.set_title('Global CO₂ Emissions (2018)', fontsize=16, pad=15, color = 'white')
txt = ax.text(0.5, .02, 'Created by: Imtiaj Iqbal Mahfuj', ha='center', 
              size=6,
              color='white',
              transform = ax.transAxes)

fig.savefig("8_newcolor_map.png", dpi=300, bbox_inches='tight')

plt.show()
```

![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/8_newcolor_map.png)

Final Map Plotting
``` python
# Final plotting

#from cartopy import crs as ccrs
fig, ax = plt.subplots(figsize = (12,6), facecolor='black', 
                       subplot_kw={'projection': ccrs.Robinson()})
ax.patch.set_facecolor('black')

ax = geodata.plot(ax=ax, column='emission', transform=ccrs.PlateCarree(),
                  cmap=our_cmap, norm=norm, s=0.05, alpha=1, edgecolors='none')

plt.setp(ax.spines.values(), color='black')
plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')
ax.set_ylim(-8000000, 9000000)

# Title and credit
ax.set_title('Global CO₂ Emissions (2018)', fontsize=16, pad=15, color = 'white')
txt = ax.text(0.5, .01, 'Created by: Imtiaj Iqbal Mahfuj', ha='center', 
              size=6,
              color='white',
              transform = ax.transAxes)

cax = fig.add_axes([0.36, 0.16, 0.33, 0.01])
sm = plt.cm.ScalarMappable(cmap=our_cmap, norm=norm)
sm._A = []

cb = fig.colorbar(sm, cax=cax, orientation="horizontal", pad=0.2, format='%.1e',
                  ticks=[0.03, 3, 33, 330, 1800, 4500, 15000, 34500, 82500],
                  drawedges=True)
cb.outline.set_visible(False)
#cb.outline.set_linewidth(0.00001)
#cb.outline.set_color('white')
cb.ax.tick_params(labelsize=2, width=0.5, length=0.5, color='white')
cbytick_obj = plt.getp(cb.ax, 'xticklabels' ) #Set y tick label color
plt.setp(cbytick_obj, color='white')
cb.ax.set_xlabel('CO$_2$ Tons/Year', fontsize=4, color='white', labelpad=-16)

#save
fig.savefig("_co2_emissions_final_map.png", dpi=300, bbox_inches='tight')

plt.show()
```

![Scatter Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25014%20World%E2%80%99s%20Carbon%20Dioxide%20Emissions%202018%2C%20Visualizing%20with%20Python/Exports/8_newcolor_map.png)


**Highlights:**
- Hotspots in **China, India, Russia, Western Europe, and the US**
- **Shipping lanes** (China–Singapore–Suez Canal) and **air routes** glow clearly
- Emissions around the **Nile** show dense population correlation

---

## 📎 Links
- 🌐 [Portfolio Website](https://imtiajiqbalmahfuj.github.io)
- 📎 [LinkedIn](https://www.linkedin.com/posts/imtiajiqbalmahfuj_visualizing-global-co%E2%82%82-emissions-2018-activity-7373666235596619776-gEkj?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)
- 📊 [EDGAR v6.0 Dataset](https://edgar.jrc.ec.europa.eu/dataset_ghg60)  
- 📄 [Crippa et al., 2021 - EDGAR Global Emissions](https://doi.org/10.5194/essd-13-5301-2021)

---

## 🔖 Tags
`GIS` `Remote Sensing` `Geospatial Python` `Python` `Climate Change` `Spatial Data-Science`  

