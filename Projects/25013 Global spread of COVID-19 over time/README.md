# 🌍 COVID-19 Daily Positive Cases Animation 


![Image]()  

![Date](https://img.shields.io/badge/01/10/2025-01/10/2025-blue) 
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

## 📊 Results

![1](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25013%20Global%20spread%20of%20COVID-19%20over%20time/COVID_Map_6_15_20.png)  
![2](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/blob/main/Projects/25013%20Global%20spread%20of%20COVID-19%20over%20time/Dynamic%20COVID%2019%20Map.gif?raw=true)  

---

## 📎 Links
- 🔗 [See more]()  

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





