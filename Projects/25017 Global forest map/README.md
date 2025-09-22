# Project: Visualizing the World's Forests with Python

![World Forests Visualization](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25017%20Global%20forest%20map/Global%20forest%20map.png)

---
🌳 **Can you locate the Amazon rainforest on this map?** 

## 🌳 Introduction
Forests and vegetation have always been central to human survival on Earth. They provide the air we breathe, the food we eat, and the materials for constructing homes. With numerous fascinating open-source datasets available, we can explore the distribution of forests and vegetation worldwide.  

This project demonstrates how to use **Python** to analyze, manipulate, and visualize forest data, producing insightful and eye-catching maps. While data visualization is the ultimate goal, the core focus is on **data manipulation and reprojection**. Libraries like **rasterio** and **rioxarray** are used to handle raster data and generate visualizations like the one above.

---

## 📊 Data Exploration
For this project, we use the **Percent Tree Coverage (PTC) dataset** from the Geospatial Information Authority of Japan, Chiba University, and collaborating organizations.  

- **Data Year:** 2003  
- **Resolution:** 30 arcseconds (~1 km²)  
- **Grid Values:** 0–100 = percentage tree coverage, 254 = water bodies, 255 = no data  

While this dataset is older, the methods are fully applicable to newer or higher-resolution datasets. Some newer datasets are broken into multiple TIFF files representing 90x60° chunks of the world; combining them is out of scope for this tutorial.

---

## 🛠️ Tools & Libraries
![GeoPy](https://img.shields.io/badge/Geospatial-Python-red)  
![GIS](https://img.shields.io/badge/GIS-ArcGIS-green) 
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Satellite%20Data-orange)  

- **Matplotlib** – for plotting and visualizations ([Link](https://matplotlib.org/))  
- **NumPy** – numerical computing ([Link](https://numpy.org/))  
- **Rasterio** – raster data I/O ([Link](https://rasterio.readthedocs.io/en/latest/))  
- **rioxarray** – raster reprojection & manipulation ([Link](https://corteva.github.io/rioxarray/stable/))  
- **pyproj** – coordinate transformations & projections ([Link](https://pyproj4.github.io/pyproj/stable/))  

---

## 🔍 Methodology
1. **Loading the Data**  
   - Raster data is loaded using **rasterio**.  
   - Minimum and maximum values are checked with **NumPy** to confirm the range (0–254).  

2. **Initial Visualization**  
   - The raw data is plotted using `imshow` with the **Greens colormap**.  
   - Water bodies appear green because their values (254) are outside the 0–100 tree coverage range.  

3. **Color Map Adjustment**  
   - Values >100 are set to 0 to represent oceans.  
   - A **custom colormap** is created using `ListedColormap`, with the first color representing areas with 0% tree coverage.  
4. **Final Visualization**  
   - The map is plotted using the adjusted colormap.  
   - Additional exploration using alternative colormaps (e.g., gnuplot) helps visualize areas with minimal forest cover.  

---

## 🌍 Results
- Major rainforests (Amazon, Congo, Southeast Asia) appear in deep green.  
- Northern Hemisphere deciduous forests are visible as lighter green areas.  
- Small forest patches, rivers, and deltas (e.g., Nile) are distinguishable with alternative colormaps.  
- The Robinson projection provides a realistic and aesthetically pleasing global view.

![World Forests Visualization](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25017%20Global%20forest%20map/Global%20forest%20map.png)

![World Forests Visualization](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25017%20Global%20forest%20map/Global%20forest%20map%20gnuplot.png)

---

## 📂 Data Source
- **Percent Tree Coverage (PTC) dataset** – [https://globalmaps.github.io/ptc.html](https://globalmaps.github.io/ptc.html)  
- License: Open-source, provided by the Geospatial Information Authority of Japan, Chiba University, and collaborators.

---

## 📌 References & Libraries
- **Matplotlib** – [https://matplotlib.org/](https://matplotlib.org/)  
- **NumPy** – [https://numpy.org/](https://numpy.org/)  
- **Rasterio** – [https://rasterio.readthedocs.io/en/latest/](https://rasterio.readthedocs.io/en/latest/)  
- **rioxarray** – [https://corteva.github.io/rioxarray/stable/](https://corteva.github.io/rioxarray/stable/)  
- **pyproj** – [https://pyproj4.github.io/pyproj/stable/](https://pyproj4.github.io/pyproj/stable/)

---
## 📎 Links
- 🔗 [See more](https://www.linkedin.com/posts/imtiajiqbalmahfuj_forest-activity-7375962081419964417-WTSE?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)  
---

## 🎨 Acknowledgements
This project was inspired by **Adam Symington**, whose work on geospatial visualizations motivated this exploration.  

---

## 🔖 Tags
`GIS` `Remote Sensing` `Python` `rasterio` `rioxarray` `Forest Mapping` `Data Visualization` `Robinson Projection` `Spatial Data Science`  

