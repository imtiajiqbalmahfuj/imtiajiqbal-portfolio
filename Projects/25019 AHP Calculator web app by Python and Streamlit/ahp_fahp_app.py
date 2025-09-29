# ahp_fahp_full_teach.py
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="AHP & Fuzzy AHP Calculator by Imtiaj Iqbal Mahfuj", layout="wide")
st.title("Advanced AHP & Fuzzy AHP Calculator with Explanation")
st.markdown("**Developed by:** Imtiaj Iqbal Mahfuj")
st.markdown("---")

# -----------------------------
# Utility functions (AHP)
# -----------------------------
RI_VALUES = {1:0.00, 2:0.00, 3:0.58, 4:0.90, 5:1.12, 6:1.24, 7:1.32, 8:1.41, 9:1.45, 10:1.49}
SAATY = {
    1:"Equal importance",2:"Weak / slight",3:"Moderate",4:"Moderate+",5:"Strong",
    6:"Strong+",7:"Very strong",8:"Very, very strong",9:"Extreme"
}

def parse_ratio(val_str):
    """Parse values like '3', '1/3', '0.333' into float."""
    if isinstance(val_str, (int, float)):
        return float(val_str)
    s = str(val_str).strip()
    if '/' in s:
        parts = s.split('/')
        try:
            num = float(parts[0]) if parts[0] != '' else 1.0
            den = float(parts[1])
            return num / den
        except Exception:
            return float(eval(s))
    try:
        return float(s)
    except Exception:
        # fallback: eval (safe-ish for these simple inputs)
        return float(eval(s))

def eigen_weights(matrix):
    vals, vecs = np.linalg.eig(matrix)
    idx = np.argmax(vals.real)
    w = np.real(vecs[:, idx])
    w = np.abs(w)
    w = w / w.sum()
    return w

def row_mean_weights(matrix):
    norm = matrix / matrix.sum(axis=0)
    w = norm.mean(axis=1)
    w = np.array(w, dtype=float)
    w = w / w.sum()
    return w

def consistency_ratio(matrix):
    n = matrix.shape[0]
    vals, _ = np.linalg.eig(matrix)
    lambda_max = np.max(vals.real)
    CI = (lambda_max - n) / (n - 1) if n > 1 else 0.0
    RI = RI_VALUES.get(n, 1.49)
    CR = CI / RI if RI != 0 else 0.0
    return lambda_max, CI, RI, CR

# -----------------------------
# Utility functions (Fuzzy)
# -----------------------------
TFN_SCALE = {
    1:(1,1,1),2:(1,2,3),3:(2,3,4),4:(3,4,5),
    5:(4,5,6),6:(5,6,7),7:(6,7,8),8:(7,8,9),9:(9,9,9)
}

def reciprocal_tfn(t):
    l,m,u = t
    return (1.0/u, 1.0/m, 1.0/l)

def fuzzy_geometric_mean(fuzzy_mat):
    n = fuzzy_mat.shape[0]
    G = []
    for i in range(n):
        l_prod = 1.0; m_prod = 1.0; u_prod = 1.0
        for j in range(n):
            l_prod *= fuzzy_mat[i,j][0]
            m_prod *= fuzzy_mat[i,j][1]
            u_prod *= fuzzy_mat[i,j][2]
        l_g = l_prod ** (1.0 / n)
        m_g = m_prod ** (1.0 / n)
        u_g = u_prod ** (1.0 / n)
        G.append((l_g, m_g, u_g))
    return G

def normalize_fuzzy_weights(G):
    sum_l = sum([g[0] for g in G])
    sum_m = sum([g[1] for g in G])
    sum_u = sum([g[2] for g in G])
    W = [(g[0]/sum_l, g[1]/sum_m, g[2]/sum_u) for g in G]
    return W

def defuzzify_tfn(t):
    l,m,u = t
    return (l + m + u) / 3.0

# -----------------------------
# TFN overview plot (single, detailed)
# -----------------------------
def overview_tfn_plot(l=2.0, m=3.0, u=4.0):
    fig, ax = plt.subplots(figsize=(6,2.5))
    x = [l, m, u]
    y = [0, 1, 0]
    ax.plot(x, y, marker='o', linewidth=2)
    ax.fill_between(x, y, alpha=0.25)
    ax.set_xlim(l - 1.0, u + 1.0)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel("Importance scale")
    ax.set_yticks([])
    ax.set_title("Triangular Fuzzy Number (TFN): lower (l), modal (m), upper (u)")
    ax.annotate("l = lower (least plausible)", xy=(l,0), xytext=(l, -0.15), ha='center')
    ax.annotate("m = most likely", xy=(m,1), xytext=(m, 1.05), ha='center')
    ax.annotate("u = upper (most optimistic)", xy=(u,0), xytext=(u, -0.15), ha='center')
    st.pyplot(fig, clear_figure=True)

# -----------------------------
# Sidebar controls (modes + method selection)
# -----------------------------
st.sidebar.header("App controls")
mode = st.sidebar.selectbox("Choose section", ["Overview & Theory","AHP (Analytic Hierarchy Process)","FAHP (Fuzzy Analytic Hierarchy Process)","Compare AHP vs FAHP"])
# weight method selector placed in sidebar to keep main UI compact
weight_method = st.sidebar.selectbox("Weight method (AHP)", ["Eigenvector (recommended)", "Row-mean (simple)"])
st.sidebar.markdown("This app is developed by **Imtiaj Iqbal Mahfuj** to learn and calculate AHP and Fuzzy AHP, two well-known MCDM (Multi-Criteria Decision-Making) techniques in Operations Research (OR).")

# prepare select options for AHP that include reciprocals
base_vals = [str(i) for i in range(1,10)]
recip_vals = [f"1/{i}" for i in range(2,10)]
AHP_OPTIONS = base_vals + recip_vals

def format_option(x):
    s = str(x)
    if '/' in s:
        return f"{s} — reciprocal"
    try:
        k = int(float(s))
        return f"{s} — {SAATY.get(k, '')}"
    except Exception:
        return s

def tfn_from_option(opt):
    """Return TFN for option like '3' or '1/3'"""
    s = str(opt)
    if '/' in s:
        # handle "1/3" style
        parts = s.split('/')
        denom = int(parts[1])
        return reciprocal_tfn(TFN_SCALE[denom])
    else:
        idx = int(float(s))
        return TFN_SCALE[idx]

################################################################################
# Overview & Theory (detailed)
################################################################################
if mode == "Overview & Theory":
    st.header("Overview: AHP and Fuzzy AHP — detailed explanation")
    st.markdown("""
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

""")

    st.subheader("AHP formulas")
    st.markdown("**Given** pairwise matrix \(A = [a_{ij}]\) (size \(n\times n\)) where \(a_{ji} = 1/a_{ij}\).")
    st.latex(r"\text{Column sum: } c_j \;=\; \sum_{i=1}^n a_{ij}")
    st.latex(r"\text{Normalized matrix: } n_{ij} \;=\; \frac{a_{ij}}{c_j}")
    st.latex(r"\text{Row-mean weight (approx): } w_i \;=\; \frac{1}{n}\sum_{j=1}^n n_{ij}")
    st.latex(r"\lambda_{\max} \approx \sum_{j=1}^n c_j w_j")
    st.latex(r"\text{Consistency Index: } CI \;=\; \frac{\lambda_{\max} - n}{n - 1}")
    st.latex(r"\text{Consistency Ratio: } CR \;=\; \frac{CI}{RI(n)} \quad \text{(acceptable if } CR \le 0.1\text{)}")

    st.subheader("FAHP formulas")
    st.latex(r"""
\text{For FAHP using TFNs:} \quad 
a_{ij} = (l_{ij}, \; m_{ij}, \; u_{ij})
""")
    st.latex(r"""
\text{Fuzzy geometric mean for row } i: \quad
GM_i \;=\; \left( \prod_{j=1}^n \ell_{ij} \right)^{1/n}, \;
\left( \prod_{j=1}^n m_{ij} \right)^{1/n}, \;
\left( \prod_{j=1}^n u_{ij} \right)^{1/n}
""")
    st.latex(r"\text{Normalize fuzzy weights: } w_i \;=\; \left( \frac{\ell_i}{\sum \ell_k}, \frac{m_i}{\sum m_k}, \frac{u_i}{\sum u_k} \right)")
    st.latex(r"\text{Defuzzify (centroid): } w_i^* \;=\; \frac{\ell_i + m_i + u_i}{3}")
    st.markdown("Then normalize \(w_i^*\) so sums to 1 and use for synthesis.")

    st.subheader("When to use which")
    st.markdown("""
- **AHP**: use when comparisons are clear and you can pick exact values.  
- **FAHP**: use when judgments are uncertain, subjective, or you collect responses from multiple experts.
""")

################################################################################
# AHP Teaching + Calculator
################################################################################
if mode == "AHP (Analytic Hierarchy Process)":
    st.header("AHP — Step-by-step Calculator")
    st.markdown("Read the short explanation before each step. The app shows intermediate matrices and formulas applied.")

    st.subheader("Step 0 — Enter criteria and alternatives (comma separated)")
    criteria_txt = st.text_area("Criteria", "Cost, Quality, Time")
    alternatives_txt = st.text_area("Alternatives", "Option A, Option B, Option C")
    criteria = [c.strip() for c in criteria_txt.split(",") if c.strip()]
    alternatives = [a.strip() for a in alternatives_txt.split(",") if a.strip()]
    n = len(criteria); m = len(alternatives)

    st.info("Recommendation: start with ≤ 6 items for clear step-by-step displays.")

    if n >= 2:
        st.subheader("A — Pairwise comparisons for criteria (Saaty 1–9 or reciprocals)")
        st.markdown("**Instruction:** For each pair choose a value from the dropdown. You may choose reciprocals like `1/3`. The reciprocal of your input is filled automatically for the opposite cell.")
        crit_inputs = {}
        cols = st.columns(3)
        for i in range(n):
            for j in range(i+1, n):
                key = f"crit_{i}_{j}"
                crit_inputs[(i,j)] = cols[(i+j) % 3].selectbox(
                    f"{criteria[i]} vs {criteria[j]}",
                    options=AHP_OPTIONS,
                    format_func=format_option,
                    key=key,
                    index=0
                )

        # build pairwise matrix parsing reciprocals
        crit_mat = np.ones((n,n), dtype=float)
        for (i,j), v_str in crit_inputs.items():
            v = parse_ratio(v_str)
            crit_mat[i,j] = v
            crit_mat[j,i] = 1.0 / v

        st.write("Pairwise matrix (criteria):")
        st.dataframe(pd.DataFrame(crit_mat, index=criteria, columns=criteria).round(6))

        # step-by-step AHP calculations with clear text
        st.markdown("**Step B — Why sum columns?**  We scale comparisons so columns are comparable. Then we divide each entry by its column sum to normalize.")
        st.markdown("**Compute column sums:**")
        colsum = crit_mat.sum(axis=0)
        st.write(pd.DataFrame(colsum, index=criteria, columns=["Column sum"]).round(6))

        st.markdown("**Step C — Normalize matrix:** divide each element by its column sum so columns sum to 1.")
        norm = crit_mat / colsum
        st.dataframe(pd.DataFrame(norm, index=criteria, columns=criteria).round(6))

        st.markdown("**Step D — Priority vector (weights):** average each row of normalized matrix or use eigenvector.")
        w_eig = eigen_weights(crit_mat)
        w_row = row_mean_weights(crit_mat)
        st.write("Eigenvector weights (principal eigenvector):")
        st.dataframe(pd.DataFrame({"Criterion":criteria, "Weight": w_eig}).set_index("Criterion").round(6))
        st.write("Row-mean weights (normalized row averages):")
        st.dataframe(pd.DataFrame({"Criterion":criteria, "Weight": w_row}).set_index("Criterion").round(6))
        w_used = w_eig if weight_method.startswith("Eigenvector") else w_row

        st.markdown("**Step E — Consistency check:** compute λ_max, CI, and CR.")
        lambda_max, CI, RI, CR = consistency_ratio(crit_mat)
        st.latex(r"\text{CI} = \frac{\lambda_{\max} - n}{n-1} \quad,\quad \text{CR} = \frac{CI}{RI(n)}")
        st.write(f"λ_max = {lambda_max:.6f}")
        st.write(f"CI = {CI:.6f} ; RI(n) = {RI} ; CR = {CR:.6f}")
        if CR > 0.1:
            st.warning("CR > 0.1: Judgments may be inconsistent. Revise pairwise comparisons.")
        else:
            st.success("CR ≤ 0.1: Consistency acceptable.")

        # Alternatives pairwise under each criterion
        if m >= 2:
            st.subheader("B — Pairwise comparisons for alternatives under each criterion")
            alt_local_weights = {}
            for c_idx, c_name in enumerate(criteria):
                st.markdown(f"**Under criterion: {c_name}**")
                st.markdown("Choose pairwise comparisons (integers 1..9 or reciprocals) comparing alternatives for this criterion.")
                alt_inputs = {}
                cols2 = st.columns(3)
                for i in range(m):
                    for j in range(i+1, m):
                        key = f"alt_{c_idx}_{i}_{j}"
                        alt_inputs[(i,j)] = cols2[(i+j) % 3].selectbox(
                            f"{alternatives[i]} vs {alternatives[j]} (for {c_name})",
                            options=AHP_OPTIONS,
                            format_func=format_option,
                            key=key,
                            index=0
                        )
                # build matrix
                alt_mat = np.ones((m,m), dtype=float)
                for (i,j), v_str in alt_inputs.items():
                    v = parse_ratio(v_str)
                    alt_mat[i,j] = v
                    alt_mat[j,i] = 1.0/v
                st.write("Pairwise matrix (alternatives):")
                st.dataframe(pd.DataFrame(alt_mat, index=alternatives, columns=alternatives).round(6))
                # compute weights (use chosen method)
                w_alt = eigen_weights(alt_mat) if weight_method.startswith("Eigenvector") else row_mean_weights(alt_mat)
                st.write("Local weights (for this criterion):")
                st.dataframe(pd.DataFrame({"Alternative":alternatives, "Weight": w_alt}).set_index("Alternative").round(6))
                lambda_max_a, CI_a, RI_a, CR_a = consistency_ratio(alt_mat)
                st.write(f"CR for this matrix = {CR_a:.6f}")
                if CR_a > 0.1:
                    st.warning("CR > 0.1: revise comparisons for this criterion.")
                alt_local_weights[c_name] = w_alt

            # Synthesis
            st.subheader("C — Synthesis: global priorities and final ranking")
            st.markdown("Multiply each alternative's local weight by the corresponding criterion weight, then sum across criteria for each alternative.")
            st.markdown("FinalScore(alt_i) = sum_over_criteria ( weight_criterion_j * local_weight_alt_i_under_j )")
            final_scores = np.zeros(m)
            for idx, c in enumerate(criteria):
                final_scores += w_used[idx] * alt_local_weights[c]
            final_scores = final_scores / final_scores.sum()
            results = pd.DataFrame({"Alternative":alternatives, "Final Score": final_scores})
            results = results.sort_values("Final Score", ascending=False).reset_index(drop=True)
            st.write("Final ranking (higher is better):")
            st.dataframe(results.round(6))
            st.bar_chart(results.set_index("Alternative")["Final Score"])
        else:
            st.info("Enter at least 2 alternatives to perform alternative comparisons.")

    else:
        st.warning("Enter at least 2 criteria to proceed.")

################################################################################
# Fuzzy AHP Teaching + Calculator (without per-pair triangles)
################################################################################
if mode == "FAHP (Fuzzy Analytic Hierarchy Process)":
    st.header("Fuzzy AHP — Step-by-step Calculator")
    st.markdown("This page mirrors the AHP page but uses Triangular Fuzzy Numbers (TFNs). Explanations accompany each arithmetic step.")

    st.subheader("Step 0 — Enter criteria & alternatives")
    fcrit_txt = st.text_area("Criteria", "Knowledge, Character, Beauty, Religion")
    falt_txt = st.text_area("Alternatives", "Partner A, Partner B, Partner C")
    fcriteria = [c.strip() for c in fcrit_txt.split(",") if c.strip()]
    falt = [a.strip() for a in falt_txt.split(",") if a.strip()]
    n = len(fcriteria); m = len(falt)
    st.info("You may input TFNs per expert. The app supports multi-expert aggregation (averaging TFN components).")

    if n >= 2:
        st.subheader("TFN mapping (default common mapping)")
        st.write(pd.DataFrame([(k,) + TFN_SCALE[k] for k in TFN_SCALE], columns=["Crisp","l","m","u"]).set_index("Crisp"))

        st.markdown("**Note:** The detailed TFN triangle and explanation are in Overview. Here we collect numbers; the app will show aggregated TFNs and all arithmetic steps.")

        # multi-expert
        num_experts = st.number_input("Number of experts to input (for aggregation)", min_value=1, max_value=5, value=1, step=1)
        use_custom = st.checkbox("Allow custom TFN entries per pair (unchecked uses mapped TFN selection)", value=False)

        # collect experts' TFNs into list of matrices
        expert_matrices = []
        for ex in range(int(num_experts)):
            st.markdown(f"### Expert {ex+1} inputs (criteria comparisons)")
            fmat = np.empty((n,n), dtype=object)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        fmat[i,j] = (1.0,1.0,1.0)
            for i in range(n):
                for j in range(i+1, n):
                    if use_custom:
                        cols = st.columns(3)
                        l = cols[0].number_input(f"E{ex+1} lower l for {fcriteria[i]} vs {fcriteria[j]}",
                                                 min_value=0.01, max_value=999.0, value=1.0, key=f"el_{ex}_{i}_{j}")
                        m = cols[1].number_input(f"E{ex+1} middle m for {fcriteria[i]} vs {fcriteria[j]}",
                                                 min_value=0.01, max_value=999.0, value=1.0, key=f"em_{ex}_{i}_{j}")
                        u = cols[2].number_input(f"E{ex+1} upper u for {fcriteria[i]} vs {fcriteria[j]}",
                                                 min_value=0.01, max_value=999.0, value=1.0, key=f"eu_{ex}_{i}_{j}")
                        fmat[i,j] = (l,m,u)
                        fmat[j,i] = reciprocal_tfn((l,m,u))
                    else:
                        sel = st.selectbox(f"E{ex+1} {fcriteria[i]} vs {fcriteria[j]}", options=AHP_OPTIONS,
                                           format_func=format_option, key=f"es_{ex}_{i}_{j}", index=0)
                        fmat[i,j] = tfn_from_option(sel)
                        fmat[j,i] = reciprocal_tfn(fmat[i,j])
            expert_matrices.append(fmat)

        # Aggregate experts: average l,m,u per cell
        st.subheader("Aggregated fuzzy pairwise matrix (averaged across experts)")
        agg = np.empty((n,n), dtype=object)
        for i in range(n):
            for j in range(n):
                if i == j:
                    agg[i,j] = (1.0,1.0,1.0)
                else:
                    ls = [expert_matrices[e][i,j][0] for e in range(int(num_experts))]
                    ms = [expert_matrices[e][i,j][1] for e in range(int(num_experts))]
                    us = [expert_matrices[e][i,j][2] for e in range(int(num_experts))]
                    agg[i,j] = (sum(ls)/len(ls), sum(ms)/len(ms), sum(us)/len(us))
        def tfn_str(t): return f"({t[0]:.3g},{t[1]:.3g},{t[2]:.3g})"
        agg_df = pd.DataFrame([[tfn_str(agg[i,j]) for j in range(n)] for i in range(n)], index=fcriteria, columns=fcriteria)
        st.dataframe(agg_df)

        # Step-by-step fuzzy calculations
        st.subheader("Step A — Fuzzy geometric mean (GM) per criterion")
        st.markdown("We multiply TFNs across the row then take the nth root component-wise.")
        GMs = fuzzy_geometric_mean(agg)
        gm_df = pd.DataFrame([{"Criterion":fcriteria[i], "l":GMs[i][0], "m":GMs[i][1], "u":GMs[i][2]} for i in range(n)]).set_index("Criterion")
        st.dataframe(gm_df.round(6))

        st.subheader("Step B — Normalize fuzzy weights (wi = GM_i / sum(GM))")
        st.markdown("Divide each GM component by the sum across criteria of that component (l by sum_l, m by sum_m, u by sum_u).")
        W = normalize_fuzzy_weights(GMs)
        w_df = pd.DataFrame([{"Criterion":fcriteria[i], "l":W[i][0], "m":W[i][1], "u":W[i][2]} for i in range(n)]).set_index("Criterion")
        st.dataframe(w_df.round(6))

        st.subheader("Step C — Defuzzify (centroid) to get crisp criteria weights")
        st.markdown("Defuzzify each fuzzy weight: w* = (l + m + u) / 3, then normalize w* so they sum to 1.")
        defuzz = np.array([defuzzify_tfn(W[i]) for i in range(n)])
        defuzz_norm = defuzz / defuzz.sum()
        st.dataframe(pd.DataFrame({"Criterion":fcriteria, "Defuzzified":defuzz.round(6), "Normalized":defuzz_norm.round(6)}).set_index("Criterion"))

        # Alternatives under each criterion (FAHP local weights)
        if m >= 2:
            st.subheader("Alternatives: fuzzy pairwise comparisons under each criterion & local weights")
            alt_local = {}
            for c_idx, c_name in enumerate(fcriteria):
                st.markdown(f"**Under criterion: {c_name}**")
                ex_count = int(num_experts)
                expert_alt_mats = []
                for ex in range(ex_count):
                    st.markdown(f"Expert {ex+1} (alternatives under {c_name})")
                    amat = np.empty((m,m), dtype=object)
                    for i in range(m):
                        for j in range(m):
                            if i==j:
                                amat[i,j] = (1.0,1.0,1.0)
                    for i in range(m):
                        for j in range(i+1,m):
                            if use_custom:
                                cols = st.columns(3)
                                l = cols[0].number_input(f"E{ex+1} lower for {falt[i]} vs {falt[j]} under {c_name}", min_value=0.01, max_value=999.0, value=1.0, key=f"al_{ex}_{c_idx}_{i}_{j}")
                                mval = cols[1].number_input(f"E{ex+1} mid for {falt[i]} vs {falt[j]} under {c_name}", min_value=0.01, max_value=999.0, value=1.0, key=f"am_{ex}_{c_idx}_{i}_{j}")
                                u = cols[2].number_input(f"E{ex+1} upper for {falt[i]} vs {falt[j]} under {c_name}", min_value=0.01, max_value=999.0, value=1.0, key=f"au_{ex}_{c_idx}_{i}_{j}")
                                amat[i,j] = (l,mval,u)
                                amat[j,i] = reciprocal_tfn((l,mval,u))
                            else:
                                sel = st.selectbox(f"E{ex+1} {falt[i]} vs {falt[j]} under {c_name}", options=AHP_OPTIONS,
                                                   format_func=format_option, key=f"asel_{ex}_{c_idx}_{i}_{j}")
                                amat[i,j] = tfn_from_option(sel)
                                amat[j,i] = reciprocal_tfn(amat[i,j])
                    expert_alt_mats.append(amat)

                # aggregate alt matrices across experts
                agg_alt = np.empty((m,m), dtype=object)
                for i in range(m):
                    for j in range(m):
                        if i==j:
                            agg_alt[i,j] = (1.0,1.0,1.0)
                        else:
                            ls = [expert_alt_mats[e][i,j][0] for e in range(ex_count)]
                            ms = [expert_alt_mats[e][i,j][1] for e in range(ex_count)]
                            us = [expert_alt_mats[e][i,j][2] for e in range(ex_count)]
                            agg_alt[i,j] = (sum(ls)/len(ls), sum(ms)/len(ms), sum(us)/len(us))

                # compute GM, normalize, defuzzify and normalize
                alt_GMs = fuzzy_geometric_mean(agg_alt)
                alt_W = normalize_fuzzy_weights(alt_GMs)
                alt_def = np.array([defuzzify_tfn(t) for t in alt_W])
                alt_def_norm = alt_def / alt_def.sum()
                st.write(pd.DataFrame({"Alternative":falt, "Defuzzified":np.round(alt_def,6), "Local weight":np.round(alt_def_norm,6)}).set_index("Alternative"))
                alt_local[c_name] = alt_def_norm

            # Final synthesis
            st.subheader("Synthesis: final FAHP ranking")
            crit_weights = defuzz_norm
            final_scores = np.zeros(m)
            for idx, c in enumerate(fcriteria):
                final_scores += crit_weights[idx] * alt_local[c]
            final_scores = final_scores / final_scores.sum()
            out = pd.DataFrame({"Alternative": falt, "Final Score": np.round(final_scores,6)}).sort_values("Final Score", ascending=False).reset_index(drop=True)
            st.write(out)
            st.bar_chart(out.set_index("Alternative")["Final Score"])
        else:
            st.info("Enter at least 2 alternatives to compute FAHP local & global weights.")
    else:
        st.warning("Enter at least 2 criteria to use FAHP.")

################################################################################
# Compare AHP vs FAHP
################################################################################
if mode == "Compare AHP vs FAHP":
    st.header("Compare AHP vs Fuzzy AHP (summary + when to use)")
    st.markdown("""
**AHP**
- Uses crisp pairwise judgments (Saaty 1–9 or reciprocals). Simpler and computationally light.
- Produces weights via eigenvector or row-mean. Check consistency (CR).

**Fuzzy AHP**
- Uses TFNs to capture uncertainty and range of possible judgments.
- Aggregates multiple experts by averaging TFN components.
- More robust to human vagueness but more steps (GM, normalize, defuzzify).

**Guideline**
- Use AHP when you have clear, confident judgments.
- Use FAHP when judgments are subjective, fuzzy, or when combining multiple experts' opinions.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; font-size:12px'>
<strong>© 2025 Imtiaj Iqbal Mahfuj</strong> — Undergraduate Student, Dept. of Urban & Regional Planning, RUET  
📧 <a href="mailto:imtiajiqbal.ruet@gmail.com">imtiajiqbal.ruet@gmail.com</a> • 🌐 <a href="https://imtiajiqbalmahfuj.github.io/" target="_blank">imtiajiqbalmahfuj.github.io</a>
</div>
""", unsafe_allow_html=True)
