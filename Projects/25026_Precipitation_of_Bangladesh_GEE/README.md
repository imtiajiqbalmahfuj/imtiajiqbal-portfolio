# 🌧️ Precipitation Mapping of Bangladesh (2015–2016)
### Mapping Annual Rainfall Patterns using GEE (Python API) and PERSIANN-CDR Dataset  

![Project Preview](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25026_Precipitation_of_Bangladesh_GEE/Precipitation%20of%20Bangladesh%202015-16%20with%20GEE%20(Python).png)  

![Date](https://img.shields.io/badge/03/11/2025-04/11/2025-blue)
![Location](https://img.shields.io/badge/Location-Bangladesh-purple)
![Platform](https://img.shields.io/badge/Platform-Google%20Earth%20Engine-green)
---
> **Author:** Imtiaj Iqbal Mahfuj  
---

## 📝 Overview
Bangladesh, a riverine country highly influenced by monsoon rainfall, experiences significant spatial and temporal variations in precipitation. Understanding these variations is crucial for **flood risk management, agricultural planning, and climate adaptation**.

This project visualizes **precipitation distribution across Bangladesh during 2015–2016** using the **PERSIANN-CDR dataset** — a satellite-based precipitation product integrating **infrared observations** and **artificial neural networks**.  
Using **Google Earth Engine’s Python API**, I extracted, processed, and visualized spatial rainfall intensity to identify areas with **higher rainfall concentration** and **potential hydrological impacts**.

The map highlights the heavy rainfall zones in **Sylhet, Chattogram, and Cox’s Bazar**, which often correlate with flash flood-prone areas, while **northwestern regions** show relatively lower precipitation intensity.

---

## 🛠️ Tools & Technologies
![Python](https://img.shields.io/badge/Python-3.10-blue)
![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-Python%20API-green)
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-PERSIANN--CDR-orange)

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| **1. Data Collection** | The **PERSIANN-CDR dataset** was accessed from NOAA’s Climate Data Record via Google Earth Engine (`NOAA/CDR/PERSIANN-CDR`). It provides global daily precipitation data from 1983–present. |
| **2. Preprocessing** | The dataset was clipped to the **Bangladesh boundary**. Timeframe filtered for 2015–2016. Units converted and scaled appropriately. |
| **3. Analysis** | Calculated total precipitation and generated yearly mean composites to visualize inter-annual variability. |
| **4. Visualization** | Used **Google Earth Engine (Python API)** to display spatial distribution and exported the results for further refinement in Python using **Matplotlib**. |

---

## 📊 Results & Insights
- 🌧️ **Highest Precipitation:** Observed over **Sylhet and southeastern coastal regions**.
- ☁️ **Moderate Rainfall:** Central and southwestern districts.
- 🌤️ **Lowest Rainfall:** Northwest and western parts of Bangladesh.
- 🔹 The visualization confirms **strong monsoonal influence** and **orographic effects** in northeastern regions.

---

## ❓ Why this Project?
- Bangladesh is among the most **climate-vulnerable** nations globally.
- Rainfall variability plays a direct role in **flooding, drought, and agricultural productivity**.
- This analysis helps **researchers and policymakers** identify **rainfall patterns and anomalies**, contributing to **disaster resilience planning**.

---

## ✨ Features
- ✅ Full GEE-Python workflow for precipitation mapping.  
- 🌍 Uses open-source, long-term climate data (PERSIANN-CDR).  
- 🗺️ Exportable, publication-quality maps.  
- 💡 Easy reproducibility for temporal or regional modifications.  

---

## 📎 Links
- 🔗 [Project Website / Portfolio](https://imtiajiqbalmahfuj.github.io/)
- 🔗 [Dataset: PERSIANN-CDR (NOAA CDR)](https://developers.google.com/earth-engine/datasets/catalog/NOAA_CDR_PERSIANN_CDR)
- 💻 [Google Earth Engine Python API Docs](https://developers.google.com/earth-engine/python_install)

---

## 🔖 Tags
`GIS` `Remote Sensing` `Python` `Google Earth Engine` `Climate Data` `PERSIANN-CDR` `Precipitation` `Hydrology` `Spatial Analysis` `Bangladesh`

---

## 📌 Credits & Shoutouts
- 👨‍💻 **Author:** [Imtiaj Iqbal Mahfuj](https://imtiajiqbalmahfuj.github.io/)  
- 🙌 **Inspiration:** Special thanks to *Amirhossein Ahrari* for inspiration.  
- 🗂️ **Data Source:** [NOAA Climate Data Record – PERSIANN-CDR](https://data.noaa.gov/dataset/dataset/cdr-precipitation-persiann-cdr)  

---
