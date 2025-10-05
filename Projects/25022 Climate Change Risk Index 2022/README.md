# 🌎 Global Climate Change Risk Index 2022 (INFORM)  
### Assessing Global CC Vulnerability, Hazard Exposure, and Coping Capacity through HDX & INFORM Data  

![Global Risk Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25022%20Climate%20Change%20Risk%20Index%202022/Climate%20Change%20Risk%20Index%202022.png)

![Date](https://img.shields.io/badge/04/10/2025-05/10/2025-indigo) 
![Location](https://img.shields.io/badge/Location-Global-purple) 
![Data Source](https://img.shields.io/badge/DataSource-HDX%20%26%20INFORM%20Risk%202025-orange)

---

## 📝 Overview
The **Global CC Risk Index 2025** visualizes how different countries face varying degrees of climate change risk, based on the **INFORM CC Risk Index** — a globally recognized framework combining:  
- 🌋 **Hazard & Exposure** (natural and human-made CC threats)  
- 🌾 **Vulnerability** (socio-economic and infrastructural susceptibility)  
- 🕊️ **Lack of Coping Capacity** (institutional and emergency response limitations)  

This Python-powered visualization reveals global disparities in disaster preparedness and resilience — emphasizing which regions are most exposed to crises and least capable of coping.

---

## 🛠️ Tools & Technologies
![Python](https://img.shields.io/badge/Python-Pandas%2C%20GeoPandas%2C%20Matplotlib-blue)
![Cartography](https://img.shields.io/badge/Cartography-Geospatial%20Mapping-green)
![Data Source](https://img.shields.io/badge/Data-HDX%2C%20INFORM%20Risk-orange)
![Visualization](https://img.shields.io/badge/Visualization-YlOrRd%20Color%20Scale-red)

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| **1. Data Collection** | Acquired *INFORM CC Risk Index 2025* dataset from **[HDX (Humanitarian Data Exchange)](https://data.humdata.org/)**, including indicators for hazard, vulnerability, and coping capacity. |
| **2. Preprocessing** | Selected and cleaned key variables (`Country`, `ISO3`, `INFORM CC RISK`, `RISK CLASS`, `Rank`) and standardized country names for merging. |
| **3. Spatial Join** | Combined INFORM dataset with **Natural Earth Admin 0 shapefile** to create a global geospatial layer. |
| **4. Visualization** | Created a choropleth map using **GeoPandas** and **Matplotlib** with the `Plasma` colormap, adding a clean legend, title, and credits. |

---

## 📊 Results & Insights
- 🔴 **Very High Risk:** South Sudan, Afghanistan, Somalia, Sudan, Yemen.  
- 🟠 **Medium Risk:** India, Bangladesh, Indonesia, Myanmar, parts of Latin America.  
- 🟢 **Low Risk:** Western Europe, Japan, Canada, Australia.  

This map highlights how **fragile governance, conflict, and climate vulnerability** intersect to shape global disaster risk patterns.  
It serves as an analytical and visual tool for policymakers, researchers, and planners in humanitarian and environmental risk assessment.

![Global Risk Index 2025 Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25022%20Climate%20Change%20Risk%20Index%202022/Climate%20Change%20Risk%20Index%202022.png)

---

## 🗂️ Data Sources
- [LinkeIn](https://www.linkedin.com/posts/imtiajiqbalmahfuj_ive-created-a-new-map-titled-global-climate-activity-7380574038110212096-te7C?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)
- 🔗 [Natural Earth Admin Boundaries](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/)  

---

## 💡 Key Takeaways
- INFORM bridges **humanitarian data and geospatial science** for better disaster preparedness.  
- Areas with **weak infrastructure or governance** are most vulnerable to crises.  
- Mapping such risks helps direct **resilience-building and resource allocation** effectively.  

---

## 🔖 Tags
`GIS` `Geospatial` `Python` `GeoPandas` `Matplotlib` `HDX` `INFORM Risk`  
`Global Risk` `Humanitarian Mapping` `Spatial Data Science` `Data Visualization` `Disaster Risk`

---

## 📌 Shoutout
Data sourced from **HDX** and **INFORM 2025 Risk Index**.  

---

## 🧭 License
This project is intended for **educational and research purposes**.  
Please cite the author and data sources if used for academic or professional work.

---

## 🌍 Author
**Imtiaj Iqbal**  
📍 Rajshahi, Bangladesh  
🔗 [imtiajiqbal.github.io](https://imtiajiqbal.github.io)  
🌱 Exploring GIS, Remote Sensing & Climate Risk Analytics

