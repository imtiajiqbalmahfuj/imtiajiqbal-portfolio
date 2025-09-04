# Developing a Composite Soil Quality Index (SQI) for Kushtia District (2024) 

![Image](https://framerusercontent.com/images/lEJroOaLbqiE0sTyjJF4tqUSs.jpg?scale-down-to=2048&width=2550&height=3300)  

![Date](https://img.shields.io/badge/22/08/2025-22/08/2025-blue) 
![Location](https://img.shields.io/badge/Location-Rajshahi-green) 
---

## 📝 Overview
I am glad to share the successful completion of my project on the Soil Quality Index (SQI) mapping of Kushtia District for 2024, which integrates multiple soil health parameters into a single, interpretable index to assess the spatial variability of soil quality.

## 🛠️ Tools & Technologies
![GIS](https://img.shields.io/badge/GIS-ArcGIS-green) 
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Satellite%20Data-orange)  

🔎 Background

Soil health is the foundation of sustainable agriculture and ecological resilience. Yet, intensive cropping practices—particularly tobacco cultivation—often deteriorate soil quality by depleting essential nutrients and increasing compaction. To capture this complexity, I developed a Soil Quality Index (SQI) that aggregates multiple physical, chemical, and biological soil parameters into a composite indicator.

---

## ⚙️ Methodology
![1](https://framerusercontent.com/images/SsGFmSox7WzdLKh7srgG4RQ6aBE.jpg?scale-down-to=1024&width=5400&height=4800)  

## ⚙️ Soil Parameters Considered

Nine critical soil properties were selected based on their established relevance in soil science:

- Volumetric Water Content (VWC)
- Soil Organic Carbon (SOC)
- Soil Organic Carbon Stock (SOCS)
- pH (water)
- Organic Carbon Density (OCD)
- Nitrogen (N)
- Clay Content
- Cation Exchange Capacity (CEC)
- Bulk Density (BD)
![2](https://framerusercontent.com/images/MOnH6WgabonxzMDpfKCzfIVw3k.jpg?scale-down-to=2048&width=2550&height=3300) 
![1](https://framerusercontent.com/images/Bv2YSv2q1ruPFGMV8Zi03pAHfI.jpg?scale-down-to=2048&width=2550&height=3300)  
![2](https://framerusercontent.com/images/rJQs8ublU1OmwCKh1xYc69rAJ8g.jpg?scale-down-to=2048&width=2550&height=3300) 
![1](https://framerusercontent.com/images/wYpttOuIfKnmiB0cfcgF2EdHcKs.jpg?scale-down-to=2048&width=2550&height=3300)  
![2](https://framerusercontent.com/images/jk9NnSD0XLWJwLIbfkntF0eA4FA.jpg?scale-down-to=2048&width=2550&height=3300) 
![1](https://framerusercontent.com/images/oluHcW4il2YMtVuJXotLJNN97w.jpg?scale-down-to=2048&width=2550&height=3300)  
![2](https://framerusercontent.com/images/eynNA9GI5GSNwj6M0UtrTrQzgJg.jpg?scale-down-to=2048&width=2550&height=3300)
![1](https://framerusercontent.com/images/BwbJ70tcQ0N6H9Atmy8C6ivOEc.jpg?scale-down-to=2048&width=2550&height=3300)  
![2](https://framerusercontent.com/images/FsKPtmy06Hr5Ok4ni3F6K93BGw.jpg?scale-down-to=2048&width=2550&height=3300)
![1](https://framerusercontent.com/images/kV07P51a9agpM1hIacRlHFPCf8.jpg?scale-down-to=2048&width=2550&height=3300)  
---
𝐃𝐚𝐭𝐚 𝐏𝐫𝐞𝐩𝐚𝐫𝐚𝐭𝐢𝐨𝐧 & 𝐀𝐥𝐢𝐠𝐧𝐦𝐞𝐧𝐭: All parameter rasters were clipped to Kushtia District and aligned to a common grid.

𝐍𝐨𝐫𝐦𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧: Parameters were normalized to a 0–1 scale using three functions:

 ✅ More is Better (e.g., SOC, N, VWC, CEC, Clay)

``` text
Si​= (Xi​−Xmin) / (Xmax​−Xmin)​​​
```

 ✅ Less is Better (e.g., Bulk Density)

``` text
Si​= (Xmax​-Xi​) / (Xmax​−Xmin)​​​
```

 ✅ Optimum Range (pH: 6.0–7.5 considered ideal).

𝐖𝐞𝐢𝐠𝐡𝐭𝐢𝐧𝐠: Factor weights were determined using a Fuzzy AHP (Analytic Hierarchy Process) framework, combining expert judgment with structured pairwise comparisons to reflect the relative importance of each indicator.

𝐀𝐠𝐠𝐫𝐞𝐠𝐚𝐭𝐢𝐨𝐧: A weighted linear combination was applied to compute the final SQI raster using raster calculator:

``` text
SQI = Sum(weight*normalized factor)
```

Formula (based on collected & normalized weights from KII):

``` text
SQI=(0.10×"Norm_Vol_water_content")+(0.20×"Norm_Soil_organic_carbon")+(0.06×"Norm_Soil_organic_carbon_Stock_")+(0.15×"Norm_pH_Water")+(0.06×"Norm_organic_carbon_density")+(0.15×"Norm_nitogen")+(0.08×"Norm_Clay_Content”)+(0.10×"Norm_bulk_density")+(0.10×"Norm_Cation_Exchange_Capacity")
```

## 📊 Results

![1](https://framerusercontent.com/images/lEJroOaLbqiE0sTyjJF4tqUSs.jpg?scale-down-to=2048&width=2550&height=3300)  

---

## 📎 Links
- 🔗 [See more](https://www.linkedin.com/posts/imtiajiqbalmahfuj_soil-quality-index-sqi-2024-activity-7364734668937596929-IMrF?utm_source=share&utm_medium=member_desktop&rcm=ACoAAETCC3UBjMNBwycvXEm57I2FBEXCxvdKcM0)  
- 📄 [Technical Report]()

---

## 🔖 Tags
`GIS` `Remote Sensing` 
