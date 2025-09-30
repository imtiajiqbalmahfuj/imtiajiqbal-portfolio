# Global Air & Sea Connectivity 🌍✈️🚢
### Visualizing Flight Routes & Shipping Lanes with Python  

![Air & Sea Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25020%20Global%20Air%20%26%20Sea%20Connectivity/Global_ShippingLanes_Flights_w.png)  

![Date](https://img.shields.io/badge/30/09/2025-30/09/2025-cyan) 
![Location](https://img.shields.io/badge/Location-Global-red) 
---

## 📝 Overview
This project visualizes the **global transportation network** by combining **international flight routes** and **shipping lanes** in a single map.  
The map highlights how air and sea routes interconnect and form the invisible highways that drive global trade, mobility, and connectivity.  

---

## 🛠️ Tools & Technologies
![Python](https://img.shields.io/badge/Python-Pandas%2C%20GeoPandas%2C%20Matplotlib-blue)  
![Cartopy](https://img.shields.io/badge/Visualization-Cartopy-red)  
![Shapely](https://img.shields.io/badge/Geometry-Shapely-green)  
![GeoData](https://img.shields.io/badge/Data-Geospatial-lightgrey)  

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| 1. Data Collection | **OpenFlights dataset** for airports & flight routes; **Marine Regions** dataset for global shipping lanes (GeoJSON/SHP). |
| 2. Preprocessing   | Cleaned and merged flight data with airport coordinates. Converted routes into `LineString` geometries. Ensured CRS alignment (EPSG:4326). |
| 3. Analysis        | Constructed a **GeoDataFrame of flight routes**; processed shipping lanes as separate layers. |
| 4. Visualization   | Plotted with **Cartopy (Robinson projection)**. Styled background black, flight routes in white, shipping lanes in red, and airports as white points. Added custom legend. |

---

## 📊 Results
- **Dense Air Traffic**: Europe, East Asia, and North America light up with heavy flight networks.  
- **Shipping Corridors**: Red lines reveal critical trade arteries like the Suez Canal and Panama Canal.  
- **Overlay View**: Clear intersections of air and sea dominance in global connectivity.  

![Flights & Shipping Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25020%20Global%20Air%20%26%20Sea%20Connectivity/Global_ShippingLanes_Flights.png) 
![Flights & Shipping Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25020%20Global%20Air%20%26%20Sea%20Connectivity/Global_ShippingLanes_Flights_w.png) 

---

## 📎 Links
- 🔗 [LinkedIn](https://www.linkedin.com/posts/imtiajiqbalmahfuj_global-air-sea-connectivity-activity-7378752270555029518-JKjr?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)  
- 🔗 [OpenFlights Data](https://openflights.org/data.html)  
- 🔗 [Marine Regions Shipping Lanes Dataset](https://www.marineregions.org/)  
- 📄 [Cartopy Documentation](https://scitools.org.uk/cartopy/docs/latest/)  

---

## 🔖 Tags
`GIS` `Python` `GeoPandas` `Cartopy` `Matplotlib` `Shapely` `Geospatial Visualization` `Data Visualization` `Flight Routes` `Shipping Lanes` `Spatial Data Science`  

---

## 📌 Shoutout
Big thanks to the **open-data providers (OpenFlights & Marine Regions)** that make projects like this possible.  

