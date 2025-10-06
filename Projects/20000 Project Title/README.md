```text
[Imtiaj.](https://imtiajiqbalmahfuj.github.io/#projects)
```
CSS Injection on the first cell (markdown) of all jupyter notebook
``` CSS
<style>
/* --- 0. CONTAINER FIX: Ensure the entire notebook is responsive --- */
body {
    overflow-x: hidden !important; /* Prevent page-level horizontal scroll */
}
div#notebook-container, .container {
    width: 100% !important; 
    max-width: 100% !important;
    min-width: 0 !important;
}

/* --- 1. HIDE PROMPTS --- */
.prompt, 
.input_prompt, 
.output_prompt, 
.jp-InputPrompt { 
    display: none !important; 
}

/* --- 2. DESKTOP/TABLET: ENFORCE HORIZONTAL SCROLL (Default for > 480px) --- */
/* Targets all code/text areas */
div.input_area pre,
.jp-InputArea-editor pre,
.code_cell pre,
.output_area pre,
div.text_cell pre {
    /* DEFAULT: Forces horizontal scroll (Laptop/Tablet) */
    white-space: pre !important; 
    overflow-x: auto !important; 
    width: 100% !important;
    max-width: 100% !important;
    padding-bottom: 10px;
}
.jp-CodeCell {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    overflow: hidden !important; 
}

/* --- 3. MOBILE OVERRIDE: FORCE WRAP/SCROLL (CSS Media Query) --- */
/* Apply these rules ONLY when the screen width is 480px or less (phone size) */
@media screen and (max-width: 480px) {
    /* Code/Text Output: Force Wrapping */
    div.input_area pre,
    .jp-InputArea-editor pre,
    .code_cell pre,
    div.text_cell pre {
        white-space: pre-wrap !important; 
        word-wrap: break-word !important;
        overflow-x: hidden !important; /* Hide scroll on the wrapped container */
    }
    
    /* UNIVERSAL AGGRESSIVE FIX: HTML Tables and Rich Outputs - Force Scroll */
    .output_subarea, 
    .output_wrapper,
    .output_html,
    .output_area table, 
    .output_area table * { 
        /* Force horizontal scroll on the outer container */
        overflow-x: auto !important;
        
        /* Ensure the content itself can stretch */
        width: auto !important;
        min-width: 100% !important;
    }
    
    /* Critical Fix for Tables */
    .output_area table {
        display: block !important; /* Allows table to be treated as a block for proper overflow */
        min-width: 100%;
    }

    /* Ensure table cells don't wrap their content */
    .output_area table td, .output_area table th {
        white-space: nowrap !important;
    }
}

/* --- 4. STYLE MARKDOWN CODE BLOCKS (Visuals) --- */
div.text_cell pre code, 
div.text_cell pre {
    background-color: var(--jp-layout-color1, #f7f7f7) !important; 
    padding: 10px; 
    border-radius: 4px; 
    border: 1px solid var(--jp-border-color2, #ccc) !important;
    max-width: 100%;
}
</style>
```

Readme Template
``` text
# Project Title Here
### Subtitle / One-liner about the project  
> *Can you spot [something interesting/region name] from this map?* 👀

![Project Preview]()  

![Date](https://img.shields.io/badge/01/10/2025-01/10/2025-blue) 
![Location](https://img.shields.io/badge/Location-Rajshahi-purple) 
---
> **Author:** Imtiaj Iqbal Mahfuj
---

## 📝 Overview
Detailed description (3–6 paragraphs) covering:
- Problem statement / motivation: Example: This project explores **spatial patterns**, integrates **remote sensing datasets**, and applies **geospatial Python tools** to visualize and analyze [specific phenomenon]. It aims to uncover key insights that support data-driven decision-making for [field/region]. 
- Main objectives
- Who benefits (researchers, planners, students, policy-makers)
- Short summary of approach and main findings  

---

## 🛠️ Tools & Technologies
![GeoPy](https://img.shields.io/badge/Geospatial-Python-magenta)  
![GIS](https://img.shields.io/badge/GIS-ArcGIS-cyan) 
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Satellite%20Data-indigo)  
![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-GEE-purple) 

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| 1. Data Collection | Describe dataset (e.g., Landsat, Sentinel, NASA DEM) |
| 2. Preprocessing   | Tools used (e.g., ArcGIS Pro, QGIS, Python libraries) |
| 3. Analysis        | Explain your method (classification, regression, visualization, etc.) |
| 4. Visualization   | How results are shown (maps, charts, 3D models) |

---

## 📊 Results & Insights  
- 🔹 Key finding or pattern from data.  
- 🔹 Significant regions or hotspots.  
- 🔹 Statistical or spatial observation.  

![1]()  
![2]()  
*Caption: Description of the above visualization.*  

---

## ❓ Why this project?
- Explain the gap or need addressed.
- Provide context (domain background, dataset limitations, prior works).
- One or two bullets on impact / use-cases.

---

## ✨ Features
- Feature 1 — short explanation.
- Feature 2 — short explanation.
- Exportable maps/plots (PNG, SVG, GeoTIFF)
- Notebook-ready examples (Jupyter / Colab)
- Optional interactive dashboard (Streamlit / Dash / Voila)
- Pre-trained models or analysis outputs (if applicable)

---

## 📎 Links
- 🔗 [See more in LinkedIn]()  
- 📄 [Publication / Conference Paper]()

---

## 🔖 Tags
`GIS` `Remote Sensing` `Geospatial Python` `Python` `GEE` `Spatial Data-Science`

---

## 📌 Credits & Shoutouts  
- 👨‍💻 **Author:** [Imtiaj iqbal Mahfuj](https://imtiajiqbalmahfuj.github.io/)  
- 🙌 **Inspiration:** Special thanks to [Mentor/Influencer Name] (e.g., *Adam Symington*, *Milos Makes Maps*) for creative influence and styling inspiration.  
- 🗂️ **Data Sources:** [Dataset Name 1], [Dataset Name 2]  

---

## 🧾 Citation (if academic/research-based)  
If you use or refer to this work, please cite as:  
> *Imtiaj Iqbal Mahfuj (2025). "Project Title." GitHub Repository. Available at:* [https://imtiajiqbalmahfuj.github.io/]  

---

## 💬 Connect with Me  
📧 Email: imtiajiqbal.ruet@gmail.com 
🌐 Portfolio: [https://imtiajiqbalmahfuj.github.io/](https://imtiajiqbalmahfuj.github.io/)  

```



# Project Title Here
### Subtitle / One-liner about the project  
> *Can you spot [something interesting/region name] from this map?* 👀
> 
![Project Preview]()  

![Date](https://img.shields.io/badge/01/10/2025-01/10/2025-blue) 
![Location](https://img.shields.io/badge/Location-Rajshahi-green) 
---
> **Author:** Imtiaj Iqbal Mahfuj
---

## 📝 Overview
Detailed description (3–6 paragraphs) covering:
- Problem statement / motivation: Example: This project explores **spatial patterns**, integrates **remote sensing datasets**, and applies **geospatial Python tools** to visualize and analyze [specific phenomenon]. It aims to uncover key insights that support data-driven decision-making for [field/region]. 
- Main objectives
- Who benefits (researchers, planners, students, policy-makers)
- Short summary of approach and main findings  

---

## 🛠️ Tools & Technologies
![GeoPy](https://img.shields.io/badge/Geospatial-Python-magenta)  
![GIS](https://img.shields.io/badge/GIS-ArcGIS-cyan) 
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Satellite%20Data-indigo)  
![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-GEE-purple) 

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| 1. Data Collection | Describe dataset (e.g., Landsat, Sentinel, NASA DEM) |
| 2. Preprocessing   | Tools used (e.g., ArcGIS Pro, QGIS, Python libraries) |
| 3. Analysis        | Explain your method (classification, regression, visualization, etc.) |
| 4. Visualization   | How results are shown (maps, charts, 3D models) |

---

## 📊 Results & Insights  
- 🔹 Key finding or pattern from data.  
- 🔹 Significant regions or hotspots.  
- 🔹 Statistical or spatial observation.  

![1]()  
![2]()  
*Caption: Description of the above visualization.*  

---

## ❓ Why this project?
- Explain the gap or need addressed.
- Provide context (domain background, dataset limitations, prior works).
- One or two bullets on impact / use-cases.

---

## ✨ Features
- Feature 1 — short explanation.
- Feature 2 — short explanation.
- Exportable maps/plots (PNG, SVG, GeoTIFF)
- Notebook-ready examples (Jupyter / Colab)
- Optional interactive dashboard (Streamlit / Dash / Voila)
- Pre-trained models or analysis outputs (if applicable)

---

## 📎 Links
- 🔗 [See more in LinkedIn]()  
- 📄 [Publication / Conference Paper]()

---

## 🔖 Tags
`GIS` `Remote Sensing` `Geospatial Python` `Python` `GEE` `Spatial Data-Science`

---

## 📌 Credits & Shoutouts  
- 👨‍💻 **Author:** [Imtiaj iqbal Mahfuj](https://imtiajiqbalmahfuj.github.io/)  
- 🙌 **Inspiration:** Special thanks to [Mentor/Influencer Name] (e.g., *Adam Symington*, *Milos Makes Maps*) for creative influence and styling inspiration.  
- 🗂️ **Data Sources:** [Dataset Name 1], [Dataset Name 2]  

---

## 🧾 Citation (if academic/research-based)  
If you use or refer to this work, please cite as:  
> *Imtiaj Iqbal Mahfuj (2025). "Project Title." GitHub Repository. Available at:* [https://imtiajiqbalmahfuj.github.io/]  

---

## 💬 Connect with Me  
📧 Email: imtiajiqbal.ruet@gmail.com 
🌐 Portfolio: [https://imtiajiqbalmahfuj.github.io/](https://imtiajiqbalmahfuj.github.io/)  

---

## 📎 Links
- 📂 [Dataset](https://example-dataset-link.com)  
- 💻 [Project GitHub Repo](https://github.com/your-repo)  
- 📄 [Publication / Conference Paper](https://doi.org/example)  

---

## 🏆 Achievements
- ✅ Presented at *ICERIE 2024*  
- 🏅 Shortlisted in *BIP World Town Planning Day Competition*  
- 📌 Featured in *XYZ Research Journal*  

---

## 🔖 Tags
`#GIS` `#RemoteSensing` `#Python` `#GEE` `#DataScience`  

---

## 📚 Citation (if applicable)
```bibtex
@inproceedings{yourpaper2024,
  title={Your Paper Title},
  author={Your Name},
  booktitle={Conference Name},
  year={2024}
}
```

# Examples 
```text


Use # to ###### for headings
# Main Title
## Section Heading
### Sub-heading

Text Formatting
*italic* or _italic_  
**bold**  
~~strikethrough~~  
`inline code`  
> Blockquote

List
- GIS
- Remote Sensing
- Python

Ordered List
1. Collect elevation data
2. Process in ArcGIS
3. Visualize in Blender

Task List
- [x] Data collected
- [ ] Analysis ongoing
- [ ] Paper writing

Links
[Google Scholar](https://scholar.google.com/)

Images
![Alt text](image.png)

Table
| Tool | Use |
|------|-----|
| ArcGIS Pro | Data Processing |
| Blender | 3D Visualization |
| Python | Analysis |

For showing code:

<pre> ```python import geopandas as gpd data = gpd.read_file("map.shp") data.plot() ``` </pre>

Badges (Fancy labels)

Use shields.io to add badges.
![Python](https://img.shields.io/badge/Python-3.9-blue)
![GIS](https://img.shields.io/badge/GIS-ArcGIS-green)

<details>
<summary>Click to expand full methodology</summary>

1. Data collection  
2. Data processing  
3. Visualization  

</details>

Embedding YouTube or External Media
[![Watch Demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://youtu.be/VIDEO_ID)

---
## Python 
<pre> ```python 
  import geopandas as gpd 
  import matplotlib.pyplot as plt 
  # Load shapefile 
  data = gpd.read_file("bangladesh.shp") 
  # Plot 
  data.plot(edgecolor="black", facecolor="lightblue") 
  plt.title("Bangladesh Map") plt.show() ``` 
</pre>
---
## JavaScript
<pre> ```javascript 
  // Google Earth Engine example 
  var dataset = ee.ImageCollection("COPERNICUS/S2") .filterDate('2024-01-01', '2024-02-01') .filterBounds(ee.Geometry.Point(90.4125, 23.8103)); Map.centerObject(dataset, 8); Map.addLayer(dataset.mean(), {bands:['B4','B3','B2'], min:0, max:3000}, "True Color"); ``` </pre>
---
###General Rules
- Use triple backticks ``` before and after code.
- Add the language name right after the first backticks (python, javascript, r, sql, bash, html, css, etc.).
- GitHub automatically applies syntax highlighting.
---
```

Template
``` text
# 🌍Project Title Here
### Subtitle / One-liner about the project  

![Banner or Demo Image](demo.png)  
*(Optional: Add a GIF or a screenshot of results)*  

![Date](https://img.shields.io/badge/01/10/2024-01/10/2024-blue) 
![Location](https://img.shields.io/badge/Location-Rajshahi-green) 
---
---

> **TL;DR:** Short paragraph (2–3 lines) summarizing what the project does, who it is for, and one key outcome or insight.

---

## 📚 Table of Contents
1. [Overview](#overview)
2. [Why this project?](#why-this-project)
3. [Features](#features)
4. [Demo / Screenshots](#demo--screenshots)
5. [Quick Start](#quick-start)
6. [Installation](#installation)
7. [Usage](#usage)
   - [CLI examples](#cli-examples)
   - [Python API / Notebook usage](#python-api--notebook-usage)
8. [Data & Inputs](#data--inputs)
9. [Methodology](#methodology)
10. [Outputs & Results](#outputs--results)
11. [Project Structure](#project-structure)
12. [Testing & CI](#testing--ci)
13. [Reproducibility & Environment](#reproducibility--environment)
14. [How to cite / Credits](#how-to-cite--credits)
15. [Contributing](#contributing)
16. [Roadmap](#roadmap)
17. [Changelog](#changelog)
18. [License](#license)
19. [Contact](#contact)
20. [Acknowledgements](#acknowledgements)
21. [FAQ](#faq)

---
## 📝 Overview
A short description (3–4 lines) about what the project does, why it’s important, and what tools/data you used.  

---

## 🛠️ Tools & Technologies
![Python](https://img.shields.io/badge/Python-3.9-blue) 
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
- Add **maps, graphs, or figures** here.  
- You can include multiple images:

![Result 1](result1.png)  
![Result 2](result2.png)  

---

## 🎥 Demo / Presentation
[![Watch Demo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://youtu.be/VIDEO_ID)  
*(Replace VIDEO_ID with YouTube link if you have a demo video)*  

---

## 📎 Links
- 📂 [Dataset](https://example-dataset-link.com)  
- 💻 [Project GitHub Repo](https://github.com/your-repo)  
- 📄 [Publication / Conference Paper](https://doi.org/example)  

---

## 🏆 Achievements
- ✅ Presented at *ICERIE 2024*  
- 🏅 Shortlisted in *BIP World Town Planning Day Competition*  
- 📌 Featured in *XYZ Research Journal*  

---

## 🔖 Tags
`#GIS` `#RemoteSensing` `#Python` `#GEE` `#DataScience`  

---

## 📚 Citation (if applicable)
```bibtex
@inproceedings{yourpaper2024,
  title={Your Paper Title},
  author={Your Name},
  booktitle={Conference Name},
  year={2024}
}
```














