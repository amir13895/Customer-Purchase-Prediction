
import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Purchase Intelligence",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(145deg, #0b1220, #111c30);
    color: #e5edf7;
}

[data-testid="stSidebar"] {
    background-color: #101a2b;
    border-right: 1px solid #263750;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #f1f5f9;
    letter-spacing: -1px;
}

.subtitle {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 25px;
}

.section-title {
    color: #67e8f9;
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 12px;
}

div[data-testid="stMetric"] {
    background: #17253a;
    border: 1px solid #2a405c;
    padding: 20px;
    border-radius: 14px;
}

div[data-testid="stForm"] {
    background: #142238;
    padding: 22px;
    border: 1px solid #293e59;
    border-radius: 16px;
}

.stButton button, 
.stFormSubmitButton button {
    background: linear-gradient(90deg, #0891b2, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 45px;
}

.stButton button:hover,
.stFormSubmitButton button:hover {
    border: 1px solid #67e8f9;
    color: white;
}

div[data-testid="stProgressBar"] > div > div {
    background-color: #22d3ee;
}

</style>
""", unsafe_allow_html=True)


# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    data = joblib.load("purchase_model_compressed.joblib")
    return data["model"], data["threshold"]


try:
    model, threshold = load_model()
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 🛍️ Purchase Intelligence")

    st.caption("Machine Learning Prediction System")

    st.divider()

    st.markdown("### About Project")

    st.write("""
    This application uses a Random Forest
    machine learning model to predict
    online customer purchase behavior.
    """)

    st.divider()

    st.markdown("### Model Information")

    st.write("**Algorithm:** Random Forest")
    st.write("**Estimators:** 300")
    st.write("**Class Weight:** Balanced")
    st.write(f"**Threshold:** {threshold * 100:.0f}%")

    st.divider()

    st.caption("Customer Purchase Prediction | 2026")


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">Customer Purchase Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze visitor behavior and estimate the probability of purchase.'
    '</div>',
    unsafe_allow_html=True
)

# ---------------- TOP METRICS ----------------

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("AI Algorithm", "Random Forest")

with m2:
    st.metric("Model Estimators", "300")

with m3:
    st.metric("Decision Threshold", f"{threshold * 100:.0f}%")

st.divider()


# ---------------- INPUT FORM ----------------

st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

st.write("Enter the customer's browsing and session information.")

with st.form("prediction_form"):

    # PAGE ACTIVITY

    st.markdown("#### 📄 Page Activity")

    c1, c2, c3 = st.columns(3)

    with c1:
        administrative = st.number_input(
            "Administrative Pages",
            min_value=0,
            value=0,
            step=1
        )

        informational = st.number_input(
            "Informational Pages",
            min_value=0,
            value=0,
            step=1
        )

    with c2:
        administrative_duration = st.number_input(
            "Administrative Duration",
            min_value=0.0,
            value=0.0
        )

        informational_duration = st.number_input(
            "Informational Duration",
            min_value=0.0,
            value=0.0
        )

    with c3:
        product_related = st.number_input(
            "Product Related Pages",
            min_value=0,
            value=10,
            step=1
        )

        product_related_duration = st.number_input(
            "Product Related Duration",
            min_value=0.0,
            value=100.0
        )

    st.divider()

    # SESSION METRICS

    st.markdown("#### 📊 Session Metrics")

    c1, c2, c3 = st.columns(3)

    with c1:
        bounce_rates = st.number_input(
            "Bounce Rates",
            min_value=0.0,
            max_value=1.0,
            value=0.02,
            format="%.4f"
        )

    with c2:
        exit_rates = st.number_input(
            "Exit Rates",
            min_value=0.0,
            max_value=1.0,
            value=0.05,
            format="%.4f"
        )

    with c3:
        page_values = st.number_input(
            "Page Values",
            min_value=0.0,
            value=0.0
        )

    c1, c2 = st.columns(2)

    with c1:
        special_day = st.number_input(
            "Special Day",
            min_value=0.0,
            max_value=1.0,
            value=0.0
        )

    with c2:
        month = st.selectbox(
            "Month",
            [
                "Feb", "Mar", "May", "June", "Jul",
                "Aug", "Sep", "Oct", "Nov", "Dec"
            ]
        )

    st.divider()

    # VISITOR INFORMATION

    st.markdown("#### 🌐 Visitor Information")

    c1, c2, c3 = st.columns(3)

    with c1:
        operating_systems = st.selectbox(
            "Operating Systems",
            list(range(1, 9)),
            index=1
        )

    with c2:
        browser = st.selectbox(
            "Browser",
            list(range(1, 14)),
            index=1
        )

    with c3:
        region = st.selectbox(
            "Region",
            list(range(1, 10)),
            index=0
        )

    c1, c2, c3 = st.columns(3)

    with c1:
        traffic_type = st.selectbox(
            "Traffic Type",
            list(range(1, 21)),
            index=1
        )

    with c2:
        visitor_type = st.selectbox(
            "Visitor Type",
            [
                "Returning_Visitor",
                "New_Visitor",
                "Other"
            ]
        )

    with c3:
        weekend = st.selectbox(
            "Weekend",
            [False, True],
            format_func=lambda x: "Yes" if x else "No"
        )

    st.divider()

    submitted = st.form_submit_button(
        "🚀 Predict Customer Purchase",
        use_container_width=True
    )


# ---------------- PREDICTION ----------------

if submitted:

    input_data = pd.DataFrame([{
        "Administrative": administrative,
        "Administrative_Duration": administrative_duration,
        "Informational": informational,
        "Informational_Duration": informational_duration,
        "ProductRelated": product_related,
        "ProductRelated_Duration": product_related_duration,
        "BounceRates": bounce_rates,
        "ExitRates": exit_rates,
        "PageValues": page_values,
        "SpecialDay": special_day,
        "Month": month,
        "OperatingSystems": operating_systems,
        "Browser": browser,
        "Region": region,
        "TrafficType": traffic_type,
        "VisitorType": visitor_type,
        "Weekend": weekend
    }])

    try:
        probability = model.predict_proba(input_data)[0, 1]

        prediction = probability >= threshold

        st.divider()

        st.markdown(
            '<div class="section-title">📈 Prediction Results</div>',
            unsafe_allow_html=True
        )

        r1, r2 = st.columns([1, 1])

        with r1:

            st.metric(
                "Purchase Probability",
                f"{probability * 100:.2f}%"
            )

            st.progress(float(probability))

            st.caption(
                f"Probability: {probability * 100:.2f}%"
            )

        with r2:

            st.markdown("#### Prediction Status")

            if prediction:
                st.success(
                    "🟢 Likely to Purchase"
                )

                st.write(
                    "The model predicts that this visitor "
                    "is likely to make a purchase."
                )

            else:
                st.warning(
                    "🟠 Unlikely to Purchase"
                )

                st.write(
                    "The model predicts that this visitor "
                    "is unlikely to make a purchase."
                )

        # Probability comparison

        st.markdown("#### Probability Analysis")

        chart_data = pd.DataFrame({
            "Category": ["Purchase", "No Purchase"],
            "Probability (%)": [
                probability * 100,
                (1 - probability) * 100
            ]
        })

        st.bar_chart(
            chart_data,
            x="Category",
            y="Probability (%)",
            color="#22d3ee"
        )

        with st.expander("View submitted customer data"):

            st.dataframe(
                input_data,
                use_container_width=True
            )

        st.caption(
            "Note: Predictions are estimates, not guarantees "
            "of actual customer behavior."
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")


# ---------------- FOOTER ----------------

st.markdown("""
<style>
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    padding: 25px 0 10px 0;
    margin-top: 40px;
    border-top: 1px solid rgba(148, 163, 184, 0.15);
    letter-spacing: 1px;
}

.footer strong {
    color: #22d3ee;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    Developed by <strong>AMIR SEDGHI</strong>
</div>
""", unsafe_allow_html=True)