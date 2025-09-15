# 🌍 COVID-19 Daily Positive Cases Animation 

![Image]()  

![Date](https://img.shields.io/badge/01/10/2025-01/10/2025-blue) 
![Location](https://img.shields.io/badge/Location-Rajshahi-green) 
---

## 📝 Overview
This project visualizes the global spread of COVID-19 over time by creating an **animated world map** showing the **daily increase in confirmed cases** using **Geospatial Python**.

---  

---

## 🛠️ Tools & Technologies
![GeoPy](https://img.shields.io/badge/Geospatial-Python-red)  
![GIS](https://img.shields.io/badge/GIS-ArcGIS-green) 
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Satellite%20Data-orange)  
![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-GEE-red)
![Geospatial](https://img.shields.io/badge/Geospatial-Data%20Science-lightgrey)  

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| 1. Data Collection | Describe dataset (e.g., Landsat, Sentinel, NASA DEM) |
| 2. Preprocessing   | Tools used (e.g., ArcGIS Pro, QGIS, Python libraries) |
| 3. Analysis        | Explain your method (classification, regression, visualization, etc.) |
| 4. Visualization   | How results are shown (maps, charts, 3D models) |

---

## 📊 Results

![1]()  
![2]()  

---

## 📎 Links
- 🔗 [See more]()  
- 📄 [Publication / Conference Paper](https://doi.org/example)

---

## 🔖 Tags
`GIS` `Remote Sensing` `Geospatial Python` `Python` `GEE` `Spatial Data-Science`  







## 📂 Dataset
**Source:** [Johns Hopkins University CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)  
File used: `time_series_covid19_confirmed_global.csv`

This dataset contains daily cumulative confirmed case counts per country.

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

## 📸 Preview
![Animated Map Preview](demo.gif)  
*(Example of the output animation)*

---

## 🏁 How to Run
1. Clone this repository  
2. Place `time_series_covid19_confirmed_global.csv` inside the project folder  
3. Run the main Python script:

```bash
python covid_animation.py

