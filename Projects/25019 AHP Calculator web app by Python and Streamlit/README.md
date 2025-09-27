# Advanced AHP Calculator for Operations Research🌐📊
### Learn and calculate Analytic Hierarchy Process (AHP) interactively

![AHP Calculator](path_to_your_app_image.png)

![Date](https://img.shields.io/badge/Date-28/09/2025-blue)
![Location](https://img.shields.io/badge/Location-Rajshahi-green)
---

## 📝 Overview
The **Step-by-Step AHP Calculator** is an interactive Python web application built using **Streamlit**.  
It allows users to **learn the Analytic Hierarchy Process** while performing real-time calculations for any multi-criteria decision-making problem.  

This app is designed for **beginners and professionals alike**, explaining:  
- Saaty's 1–9 scale and how to assign pairwise comparisons  
- Matrix normalization and calculation of priority vectors  
- Consistency check using the Consistency Ratio (CR)  
- Synthesis of final global priorities to rank alternatives  

The app also provides **visualizations, step-by-step explanations, and formulas** so users can **fully understand AHP**.

---

## 🛠️ Tools & Technologies
![Python](https://img.shields.io/badge/Python-NumPy%2CPandas%2CStreamlit-blue)  
![Data Science](https://img.shields.io/badge/Data%20Science-Python-lightgrey)  
![Visualization](https://img.shields.io/badge/Visualization-Interactive%20Charts-green)  
![Web App](https://img.shields.io/badge/Web%20App-Streamlit-red)  

---

## ⚙️ Methodology
| Step | Description |
|------|-------------|
| 1. **Input Criteria** | Enter all the decision criteria (e.g., Cost, Quality, Time). Each criterion represents a factor affecting the decision. |
| 2. **Input Alternatives** | Enter all alternatives (e.g., Supplier A, Supplier B). Each alternative is a possible option to choose from. |
| 3. **Pairwise Comparisons** | Compare each pair of criteria using **Saaty's 1–9 scale**. Repeat for alternatives under each criterion. |
| 4. **Normalize Matrix & Calculate Priority Vector** | Divide each element by its column sum to normalize the matrix. Then, calculate the priority vector (average of rows) to find local weights. |
| 5. **Consistency Check** | Compute λ_max, Consistency Index (CI), and Consistency Ratio (CR) to verify the reliability of the comparisons. CR ≤ 0.1 is acceptable. |
| 6. **Synthesize Global Priorities** | Multiply each alternative’s local weights by the corresponding criteria weights and sum across all criteria to get final scores. |
| 7. **Visualize & Rank Alternatives** | Display final rankings and bar charts for easy interpretation. |

---

## 📊 Example Use Case
**Decision Problem:** Selecting the best supplier based on three criteria: Cost, Quality, Time.  

- Criteria: Cost, Quality, Time  
- Alternatives: Supplier A, Supplier B, Supplier C  

**Steps:**  
1. Enter criteria and alternatives  
2. Fill pairwise comparisons using the 1–9 scale  
3. Review normalized matrices and priority vectors  
4. Check CR for consistency  
5. See final global priorities and ranking  

**Visualization:**  
![Stepwise AHP Example](path_to_example_image.png)  

---

## 📎 Links
- 🔗 [Try the live app](https://imtiajiqbalmahfuj-ahp-calculator.streamlit.app/)  
- 📄 [Project Website](https://imtiajiqbalmahfuj.github.io/)  

---

## 🔖 Tags
`AHP` `Decision Making` `Multi-Criteria Decision Analysis` `Python` `Streamlit` `Interactive Web App` `Data Visualization` `Educational`  

---

## 📌 Credit
Developed by **Imtiaj Iqbal Mahfuj**  
Undergraduate Student, Department of Urban & Regional Planning, RUET  
📧 [imtiajiqbal.ruet@gmail.com](mailto:imtiajiqbal.ruet@gmail.com)  
🌐 [imtiajiqbalmahfuj.github.io](https://imtiajiqbalmahfuj.github.io/)  

© 2025 Imtiaj Iqbal Mahfuj

