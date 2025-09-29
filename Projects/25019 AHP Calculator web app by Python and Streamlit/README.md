# Multifunctional AHP & Fuzzy AHP Calculator for OR
### Learn and calculate the Analytic Hierarchy Process (AHP) & Fuzzy AHP interactively

![AHP Calculator](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25019%20AHP%20Calculator%20web%20app%20by%20Python%20and%20Streamlit/ahpfahpss.png)

![Date](https://img.shields.io/badge/27/09/25-29/09/2025-blue)
![Location](https://img.shields.io/badge/Location-Rajshahi-green)
---

## 📝 Overview
Suppose you are selecting the best partner to get married. The factors might include: knowledge, character/personality/values, beauty, and religion. Then which partner will be the best fit for you? Here comes MCDM (Multi-Criteria Decision Making). And the most famous techniques of MCDA (Multi-Criteria Decision Analysis) are AHP (Analytic Hierarchy Process) and Fuzzy AHP. 

This application teaches and performs the **Analytic Hierarchy Process (AHP)** and **Fuzzy AHP (FAHP)** calculation.
It allows anyone to calculate AHP & Fuzzy AHP while learning how the calculations are done developed by Imtiaj Iqbal Mahfuj.

---
## **Analytic Hierarchy Process (AHP)**

The Analytic Hierarchy Process (AHP), also called the Analytical Hierarchy Process, is a structured technique for organizing and analyzing complex decisions. It combines elements of mathematics and psychology.

AHP was developed in the 1970s by Thomas L. Saaty, who later partnered with Ernest Forman in 1983 to develop the Expert Choice software. Since then, AHP has been extensively studied, validated, and refined.

The method provides a systematic framework to quantify the weights of decision criteria and compare alternatives. Experts or decision-makers express their judgments through pairwise comparisons, which reflect how much more important or preferable one element is over another. Saaty’s 1–9 scale is typically used for this purpose.

**Steps in AHP include:**
- Structuring the problem into goal → criteria → sub-criteria (if any) → alternatives.
- Pairwise comparisons between criteria and alternatives.
- Deriving priority weights using eigenvector or row-mean methods.
- Checking consistency using the Consistency Ratio (CR).
- Synthesizing results to identify the best alternative.

Through this process, AHP helps identify the alternative that best satisfies the decision criteria.

### Saaty's 1–9 Scale for Pairwise Comparison
| Value | Meaning | Explanation |
|-------|---------|-------------|
| 1     | Equal importance | Both elements are equally important |
| 2     | Weak importance | Slight preference of one over the other |
| 3     | Moderate importance | Moderate preference of one over the other |
| 4     | Moderate+ importance | Between moderate and strong preference |
| 5     | Strong importance | Strong preference of one over the other |
| 6     | Strong+ importance | Between strong and very strong |
| 7     | Very strong | Very strong preference |
| 8     | Very very strong | Between very strong and extreme |
| 9     | Extreme | Absolutely preferred |

Use reciprocals for inverse comparisons. For example, if B is moderately preferred over A, then A vs B = 1/3.

---
## **Fuzzy Analytic Hierarchy Process (Fuzzy AHP or FAHP)**

While AHP is powerful, it assumes that decision-makers can give precise numerical judgments (like 3, 5, 7). In practice, human judgments are often uncertain, vague, or imprecise. To address this limitation, researchers extended AHP into the Fuzzy Analytic Hierarchy Process (FAHP).

FAHP uses Fuzzy Set Theory, introduced by Lotfi A. Zadeh in 1965, to better capture uncertainty in human decision-making. Instead of assigning a single crisp value for importance, FAHP represents judgments with a **Triangular Fuzzy Number (TFN)** defined as:

TFN=(l,m,u)

- l: the lowest possible value (pessimistic)
- m: the most likely or modal value
- u: the highest possible value (optimistic)

> For example, instead of saying “criterion A is exactly 3 times more important than criterion B,” an expert might say “between 2 and 4 times, but most likely 3,” represented as (2,3,4).

**Steps in FAHP include:**
- Constructing fuzzy pairwise comparison matrices using TFNs.
- Computing the fuzzy geometric mean for each criterion.
- Normalizing fuzzy weights.
- Defuzzifying (converting fuzzy weights into crisp values, often by centroid method).
- Synthesizing results to identify the best alternative.

### TFNs — concept
A Triangular Fuzzy Number is ( l, m, u ):
- ( l ): lower bound (least plausible value),
- ( m ): modal / most likely value,
- ( u ): upper bound (most optimistic).
The TFN represents uncertainty in a single comparison. A crisp 3 (moderate) often maps to (2,3,4).
---
### TFN Pairwise Comparison
| Crisp | (l,m,u) | Meaning | Explanation |
|-------|---------|---------|-------------|
| 1     | (1,1,1) | Equal importance | Both elements are equally important |
| 2     | (1,2,3) | Weak importance | Slight preference of one over the other |
| 3     | (2,3,4) | Moderate importance | Moderate preference of one over the other |
| 4     | (3,4,5) | Moderate+ importance | Between moderate and strong preference |
| 5     | (4,5,6) | Strong importance | Strong preference of one over the other |
| 6     | (5,6,7) | Strong+ importance | Between strong and very strong |
| 7     | (6,7,8) | Very strong | Very strong preference |
| 8     | (7,8,9) | Very very strong | Between very strong and extreme |
| 9     | (9,9,9) | Extreme | Absolutely preferred |
---
## Why use AHP / FAHP?
**Decision problems** often involve multiple criteria. AHP provides a structured way to:
- break a decision into goal → criteria → alternatives,
- compare elements pairwise,
- compute weights and a final ranking.

**Limitation of classic AHP**: it requires exact numeric judgments (Saaty's 1–9). Humans are often uncertain.  
**FAHP** solves this by allowing **ranges** of values using **Triangular Fuzzy Numbers (TFNs)**.

---

## High-level workflow
1. Define **criteria** and **alternatives**.  
2. For criteria: perform **pairwise comparisons** (AHP: integer 1–9 or reciprocals, FAHP: TFNs (l,m,u)).  
3. For each criterion: compare **alternatives** pairwise (same scale).  
4. Compute **local weights** (per criterion) and **global synthesis** (final scores).  
5. Check **consistency** in AHP and interpret results.  

---

## 🛠️ Tools & Technologies
![Python](https://img.shields.io/badge/Python-NumPy%2CPandas%2CStreamlit-blue)  
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
![Stepwise AHP Example](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25019%20AHP%20Calculator%20web%20app%20by%20Python%20and%20Streamlit/ahpfahpss.png)  
![Stepwise AHP Example](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25019%20AHP%20Calculator%20web%20app%20by%20Python%20and%20Streamlit/Screenshot%202025-09-28%20035207.png)  
![Stepwise AHP Example](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25019%20AHP%20Calculator%20web%20app%20by%20Python%20and%20Streamlit/Screenshot%202025-09-28%20035219.png)  
![Stepwise AHP Example](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25019%20AHP%20Calculator%20web%20app%20by%20Python%20and%20Streamlit/Screenshot%202025-09-28%20041341.png)  
![Stepwise AHP Example](https://raw.githubusercontent.com/imtiajiqbalmahfuj/imtiajiqbal-portfolio/refs/heads/main/Projects/25019%20AHP%20Calculator%20web%20app%20by%20Python%20and%20Streamlit/Screenshot%202025-09-28%20041401.png)  
 

---

## 📎 Links
- 🔗 [Try the live app_ahp & fahp](https://ahp-fahp-calculator-imtiajiqbalmahfuj.streamlit.app/)  
- 🔗 [Try the live app_old_only ahp](https://imtiajiqbalmahfuj-ahp-calculator.streamlit.app/)  
- 📄 [Project Website](https://imtiajiqbalmahfuj.github.io/)  

---

## 🔖 Tags
`AHP` `Decision Making` `Multi-Criteria Decision Analysis` `Python` `Streamlit` `Interactive Web App` `Data Visualization` `Educational`  

---

## 📌 Credit
Developed by **Imtiaj Iqbal Mahfuj**  
📧 [imtiajiqbal.ruet@gmail.com](mailto:imtiajiqbal.ruet@gmail.com)  
🌐 [imtiajiqbalmahfuj.github.io](https://imtiajiqbalmahfuj.github.io/)  

© 2025 Imtiaj Iqbal Mahfuj

