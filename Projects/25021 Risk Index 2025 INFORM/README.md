# 🌎 Global Risk Index 2025 (INFORM)  
### Assessing Global Vulnerability, Hazard Exposure, and Coping Capacity through HDX & INFORM Data  

![Global Risk Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25021%20Risk%20Index%202025%20INFORM/Global%20Risk%20Index%202025.png)

![Date](https://img.shields.io/badge/03/10/2025-04/10/2025-blue) 
![Location](https://img.shields.io/badge/Location-Global-red) 
![Data Source](https://img.shields.io/badge/DataSource-HDX%20%26%20INFORM%20Risk%202025-orange)

---

## 📝 Overview
The **Global Risk Index 2025** visualizes how different countries face varying degrees of disaster risk based on the **INFORM Risk Index** — a globally recognized framework that assesses risk by combining **hazard & exposure**, **vulnerability**, and **lack of coping capacity**.  

This Python-powered map highlights spatial patterns of global risk, identifying which regions are most susceptible to crises — from natural disasters like floods and droughts to human-driven factors such as conflict or poor governance.  

---

## 🛠️ Tools & Technologies
![Python](https://img.shields.io/badge/Python-Pandas%2C%20GeoPandas%2C%20Matplotlib-blue)
![Data Source](https://img.shields.io/badge/Data-HDX%2C%20INFORM%20Risk-orange)

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| **1. Data Collection** | Acquired the *INFORM Risk Index 2025* dataset from **[HDX (Humanitarian Data Exchange)](https://data.humdata.org/)**, containing country-level indicators on risk, hazard, vulnerability, and coping capacity. |
| **2. Preprocessing** | Cleaned and selected key columns including `COUNTRY`, `ISO3`, `INFORM RISK`, `RISK CLASS`, and `Rank`. Standardized country names for accurate merging with Natural Earth shapefile. |
| **3. Spatial Join** | Merged the INFORM dataset with **Natural Earth Admin 0 shapefile** using ISO3 or country name for spatial mapping. |
| **4. Visualization** | Mapped countries using **GeoPandas** with the `YlOrRd` colormap to depict INFORM Risk Index values. Added legend, title, and source credits for professional presentation. |

---

## 📊 Results & Insights
- 🌋 **Highest Risk (Very High INFORM Index):** South Sudan, Afghanistan, Somalia, Sudan, and Yemen.  
- 🌾 **Medium Risk Regions:** India, Bangladesh, Indonesia, and parts of Latin America.  
- 🕊️ **Low-Risk Nations:** Most of Western Europe, Japan, Canada, and Australia.  

The visualization reveals stark **spatial inequalities** in resilience and preparedness — especially in regions experiencing conflict or fragile governance systems.  

![Global Risk Index 2025 Map](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25021%20Risk%20Index%202025%20INFORM/Global%20Risk%20Index%202025.png)

---

## 📎 Data Sources
- [LinkedIn](https://www.linkedin.com/posts/imtiajiqbalmahfuj_can-you-spot-which-regions-are-most-at-risk-activity-7380147740376440832-OBwS?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)
- 🔗 [INFORM Risk Index 2025 – HDX](https://data.humdata.org/dataset/inform-risk-index-2025)  
- 🔗 [Natural Earth Admin Boundaries](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/)  

---

## 🔖 Tags
`GIS` `Geospatial Python` `GeoPandas` `Matplotlib` `HDX` `INFORM Risk` `Global Risk` `Humanitarian Mapping` `Spatial Data Science` `Data Visualization` `Disaster Risk`  

---

## 📌 Shoutout
Data sourced from **HDX** and **INFORM 2025** framework.  

---

## 🧭 License
This project is created for educational and research purposes. Please cite or credit appropriately when reusing visuals or methods.
