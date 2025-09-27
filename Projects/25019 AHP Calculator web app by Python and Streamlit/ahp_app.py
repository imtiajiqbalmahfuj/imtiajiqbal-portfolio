import streamlit as st
import numpy as np
import pandas as pd

st.title("Advanced AHP Calculator")

# Step 1: Criteria input
criteria = st.text_area("Enter criteria (comma separated):", "Cost, Quality, Time")
criteria = [c.strip() for c in criteria.split(",") if c.strip()]
n = len(criteria)

# Step 2: Alternatives input
alternatives = st.text_area("Enter alternatives (comma separated):", "Option A, Option B, Option C")
alternatives = [a.strip() for a in alternatives.split(",") if a.strip()]
m = len(alternatives)

# Function to calculate priority vector and CR
def ahp_weights(matrix):
    col_sum = matrix.sum(axis=0)
    norm_matrix = matrix / col_sum
    priority_vector = norm_matrix.mean(axis=1)

    n = matrix.shape[0]
    lambda_max = (col_sum * priority_vector).sum()
    CI = (lambda_max - n) / (n - 1) if n > 1 else 0
    RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12,
               6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    RI = RI_dict.get(n, 1.49)
    CR = CI / RI if RI != 0 else 0

    return priority_vector, CR

if n > 1 and m > 1:
    # Step 3: Criteria comparison matrix
    st.subheader("Pairwise Comparison: Criteria")
    criteria_matrix = np.ones((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            val = st.number_input(
                f"Importance of **{criteria[i]}** vs **{criteria[j]}**:",
                min_value=1.0, max_value=9.0, value=1.0, step=1.0,
                key=f"criteria_{i}_{j}"
            )
            criteria_matrix[i, j] = val
            criteria_matrix[j, i] = 1 / val

    criteria_weights, criteria_CR = ahp_weights(criteria_matrix)

    st.write("Criteria Weights")
    st.write(pd.DataFrame({"Criteria": criteria, "Weight": criteria_weights}))
    st.write(f"Criteria Consistency Ratio: {criteria_CR:.4f}")

    # Step 4: Alternatives comparisons under each criterion
    alt_weights = {}
    for c_idx, c in enumerate(criteria):
        st.subheader(f"Pairwise Comparison of Alternatives for Criterion: {c}")
        alt_matrix = np.ones((m, m))

        for i in range(m):
            for j in range(i + 1, m):
                val = st.number_input(
                    f"How much more does **{alternatives[i]}** satisfy {c} than **{alternatives[j]}**?",
                    min_value=1.0, max_value=9.0, value=1.0, step=1.0,
                    key=f"alt_{c_idx}_{i}_{j}"
                )
                alt_matrix[i, j] = val
                alt_matrix[j, i] = 1 / val

        alt_priority, alt_CR = ahp_weights(alt_matrix)
        alt_weights[c] = alt_priority

        st.write(f"Weights under {c}:")
        st.write(pd.DataFrame({"Alternative": alternatives, "Weight": alt_priority}))
        st.write(f"Consistency Ratio for {c}: {alt_CR:.4f}")

    # Step 5: Final synthesis
    st.subheader("Final Ranking of Alternatives")

    final_scores = np.zeros(m)
    for c_idx, c in enumerate(criteria):
        final_scores += criteria_weights[c_idx] * alt_weights[c]

    results = pd.DataFrame({"Alternative": alternatives, "Final Score": final_scores})
    results = results.sort_values(by="Final Score", ascending=False)
    st.write(results)

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <strong>© 2025 Imtiaj Iqbal Mahfuj</strong><br>
        Undergraduate Student, Department of Urban & Regional Planning<br>
        Rajshahi University of Engineering & Technology (RUET)<br><br>
        📧 <a href="mailto:imtiajiqbal.ruet@gmail.com">imtiajiqbal.ruet@gmail.com</a><br>
        🌐 <a href="https://imtiajiqbalmahfuj.github.io/" target="_blank">imtiajiqbalmahfuj.github.io</a>
    </div>
    """,
    unsafe_allow_html=True
)
