import streamlit as st
import numpy as np
import pandas as pd

# ---------------- Introduction ----------------
st.title("Step-by-Step Educational AHP Calculator")
st.markdown("""
This app explains **Analytic Hierarchy Process (AHP)** step by step.
It allows anyone to calculate AHP **while learning how the calculations are done**.

**References:**  
- [Saaty, T.L., 1980. The Analytic Hierarchy Process](https://onlinelibrary.wiley.com/doi/abs/10.1002/nav.3800010203)  
- [Wikipedia: AHP](https://en.wikipedia.org/wiki/Analytic_hierarchy_process)
""")

# ---------------- Saaty's Scale ----------------
st.subheader("Saaty's 1–9 Scale for Pairwise Comparison")
st.markdown("""
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
""")

# ---------------- Step 1: Criteria ----------------
st.header("Step 1: Enter Criteria")
st.markdown("These are the factors that influence your decision, e.g., Cost, Quality, Time.")
criteria = st.text_area("Enter criteria (comma separated):", "Cost, Quality, Time")
criteria = [c.strip() for c in criteria.split(",") if c.strip()]
n = len(criteria)

# ---------------- Step 2: Alternatives ----------------
st.header("Step 2: Enter Alternatives")
st.markdown("These are the options you are deciding between, e.g., Supplier A, Supplier B, Supplier C.")
alternatives = st.text_area("Enter alternatives (comma separated):", "Option A, Option B, Option C")
alternatives = [a.strip() for a in alternatives.split(",") if a.strip()]
m = len(alternatives)

# ---------------- Helper Function ----------------
def ahp_calculation(matrix):
    st.markdown("**Step A: Display Original Pairwise Matrix**")
    st.write(matrix)

    # Step B: Column sum
    col_sum = matrix.sum(axis=0)
    st.markdown("**Step B: Sum each column (for normalization)**")
    st.write(pd.DataFrame(col_sum, index=matrix.columns if hasattr(matrix,'columns') else None, columns=["Column Sum"]))

    # Step C: Normalize matrix
    norm_matrix = matrix / col_sum
    st.markdown("**Step C: Normalize the matrix (Divide each element by its column sum)**")
    st.write(norm_matrix)

    # Step D: Calculate priority vector
    priority_vector = norm_matrix.mean(axis=1)
    st.markdown("**Step D: Calculate Priority Vector (Average of each row in normalized matrix)**")
    st.write(pd.DataFrame(priority_vector, index=matrix.index if hasattr(matrix,'index') else None, columns=["Priority Weight"]))

    # Step E: Consistency check
    lambda_max = (col_sum * priority_vector).sum()
    n = matrix.shape[0]
    CI = (lambda_max - n) / (n - 1) if n > 1 else 0
    RI_dict = {1:0,2:0,3:0.58,4:0.9,5:1.12,6:1.24,7:1.32,8:1.41,9:1.45,10:1.49}
    RI = RI_dict.get(n,1.49)
    CR = CI / RI if RI != 0 else 0
    st.markdown("**Step E: Calculate Consistency Ratio (CR)**")
    st.markdown("""
    Formula: CR = CI / RI  
    where CI = (λ_max - n)/(n-1),  
    λ_max = Maximum eigenvalue (sum of column sums × priority vector)
    """)
    st.write(f"Lambda max (λ_max) = {lambda_max:.4f}")
    st.write(f"Consistency Index (CI) = {CI:.4f}")
    st.write(f"Random Index (RI) = {RI}")
    st.write(f"Consistency Ratio (CR) = {CR:.4f}")
    if CR>0.1:
        st.warning("CR > 0.1: Matrix may be inconsistent. Consider revising your pairwise comparisons.")

    return priority_vector, CR

# ---------------- Step 3: Pairwise Comparison ----------------
if n>1 and m>1:
    st.header("Step 3: Pairwise Comparison of Criteria")
    st.markdown("Compare criteria using the 1–9 scale explained above.")

    criteria_matrix = np.ones((n,n))
    for i in range(n):
        for j in range(i+1,n):
            val = st.number_input(f"Importance of **{criteria[i]}** vs **{criteria[j]}**:",min_value=1.0,max_value=9.0,value=1.0,step=1.0,key=f"crit_{i}_{j}")
            criteria_matrix[i,j]=val
            criteria_matrix[j,i]=1/val

    criteria_df = pd.DataFrame(criteria_matrix, index=criteria, columns=criteria)
    crit_weights, crit_CR = ahp_calculation(criteria_df)

    st.bar_chart(pd.DataFrame({"Criteria":criteria,"Weight":crit_weights}).set_index("Criteria"))

    # ---------------- Step 4: Alternatives ----------------
    st.header("Step 4: Pairwise Comparison of Alternatives under Each Criterion")
    alt_weights = {}
    for c_idx, c in enumerate(criteria):
        st.subheader(f"Criterion: {c}")
        st.markdown("Compare each pair of alternatives under this criterion using 1–9 scale.")
        alt_matrix = np.ones((m,m))
        for i in range(m):
            for j in range(i+1,m):
                val = st.number_input(f"How much more does **{alternatives[i]}** satisfy {c} than **{alternatives[j]}**?",min_value=1.0,max_value=9.0,value=1.0,step=1.0,key=f"alt_{c_idx}_{i}_{j}")
                alt_matrix[i,j]=val
                alt_matrix[j,i]=1/val

        alt_df = pd.DataFrame(alt_matrix, index=alternatives, columns=alternatives)
        weights, CR = ahp_calculation(alt_df)
        alt_weights[c] = weights
        st.bar_chart(pd.DataFrame({"Alternative":alternatives,"Weight":weights}).set_index("Alternative"))

    # ---------------- Step 5: Final Ranking ----------------
    st.header("Step 5: Final Ranking")
    final_scores = np.zeros(m)
    for c_idx, c in enumerate(criteria):
        final_scores += crit_weights[c_idx]*alt_weights[c]
    results = pd.DataFrame({"Alternative":alternatives,"Final Score":final_scores})
    results = results.sort_values("Final Score",ascending=False)
    st.write(results)
    st.bar_chart(results.set_index("Alternative")["Final Score"])

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
<strong>© 2025 Imtiaj Iqbal Mahfuj</strong><br>
Undergraduate Student, Department of Urban & Regional Planning<br>
Rajshahi University of Engineering & Technology (RUET)<br><br>
📧 <a href="mailto:imtiajiqbal.ruet@gmail.com">imtiajiqbal.ruet@gmail.com</a><br>
🌐 <a href="https://imtiajiqbalmahfuj.github.io/" target="_blank">imtiajiqbalmahfuj.github.io</a>
</div>
""",unsafe_allow_html=True)
