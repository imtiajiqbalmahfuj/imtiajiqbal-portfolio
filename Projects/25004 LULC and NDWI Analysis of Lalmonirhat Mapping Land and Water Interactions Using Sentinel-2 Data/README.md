# LULC and NDWI Analysis of Lalmonirhat: Mapping Land and Water Interactions Using Sentinel-2 Data

![Image](https://framerusercontent.com/images/cTHb3EEMpeMX3sr1UC7mKdzwDQ.png?scale-down-to=1024&width=1514&height=978)  

![Date](https://img.shields.io/badge/15/03/2025-15/03/2025-blue) 
![Location](https://img.shields.io/badge/Location-Rajshahi-green) 
---

## 📝 Overview
Lalmonirhat, one of the most flood-prone districts in Bangladesh, experiences recurrent flooding due to its proximity to major rivers like the Teesta, Dharla, and Brahmaputra. To better understand the flood dynamics, I have created:



✅ Land Use Land Cover (LULC) Map – Derived using unsupervised classification of Sentinel-2 data to analyze land categories such as agricultural land, water bodies, built-up areas, and vegetation. This helps identify flood-prone zones and potential water retention areas.

✅ Normalized Difference Water Index (NDWI) Map – Using Green (Band 3) and Near-Infrared (Band 8) bands, the NDWI map precisely identifies existing water bodies and helps monitor seasonal variations in flood extent.

✅ Extracted Waterbody Map – Highlights rivers, wetlands, and flood retention areas, offering crucial insights into the main sources of floodwater during extreme weather events.



🛠️ 𝗠𝗲𝘁𝗵𝗼𝗱𝗼𝗹𝗼𝗴𝘆:

📌 Data Source: Downloaded Sentinel-2 MSI imagery covering three granules of Lalmonirhat.
📌 Preprocessing: Mosaicked and atmospherically corrected imagery to remove radiometric inconsistencies.
📌 LULC Classification: Applied K-Means clustering (unsupervised classification) to categorize land use types.
📌 NDWI Calculation: Used Raster Calculator in ArcGIS Pro with the formula:

𝙽𝙳𝚆𝙸=(𝙱𝟹+𝙱𝟾)(𝙱𝟹−𝙱𝟾)​

📌 Waterbody Extraction: Thresholded NDWI values to extract permanent water bodies from seasonal flood zones.  

---

## 🛠️ Tools & Technologies
![GIS](https://img.shields.io/badge/GIS-ArcGIS-green) 
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Satellite%20Data-orange)  

---

## 📊 Results

![1](https://framerusercontent.com/images/cTHb3EEMpeMX3sr1UC7mKdzwDQ.png?scale-down-to=1024&width=1514&height=978)  
🚀 𝗞𝗲𝘆 𝗙𝗶𝗻𝗱𝗶𝗻𝗴𝘀 & 𝗦𝗶𝗴𝗻𝗶𝗳𝗶𝗰𝗮𝗻𝗰𝗲:

- The LULC map reveals key land types influencing floodwater retention and drainage.
- NDWI analysis confirms major floodwater sources and potential flood expansion zones.
- The study can support flood hazard mapping, disaster risk reduction, and urban planning for sustainable flood management in the region.

By leveraging geospatial analysis, we can improve flood preparedness and urban resilience in Bangladesh. 🌍



💬 I’d love to hear your thoughts! How can we further enhance flood prediction and management using remote sensing?  

---

## 📎 Links
- 🔗 [See more](https://www.linkedin.com/posts/imtiajiqbalmahfuj_geospatial-remotesensing-lulc-activity-7306719738426966016-3i86?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)  

---

## 🔖 Tags
`GIS` `Remote Sensing` 
