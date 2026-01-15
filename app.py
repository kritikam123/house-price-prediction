import streamlit as st
import pickle
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="HomeWorth",
    page_icon="🏡",
    layout="centered"
)

# ---------- LOAD MODEL ----------
with open("bangalore_home_prices_model.pickle", "rb") as f:
    model = pickle.load(f)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #fafafa;
}
.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    color: #2c2c2c;
}
.subtitle {
    text-align: center;
    color: #6c6c6c;
    font-size: 18px;
    margin-bottom: 30px;
}
.result-box {
    background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    font-size: 24px;
    color: #2e7d32;
    font-weight: 600;
}
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🏡 HomeWorth</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">An aesthetic ML-powered real estate price predictor</div>',
    unsafe_allow_html=True
)

# ---------- SIDEBAR INPUT ----------
st.sidebar.header("🏠 Property Details")

location = st.sidebar.number_input(
    "📍 Location (Encoded)",
    min_value=0,
    help="Encoded value used during model training"
)

sqft = st.sidebar.slider(
    "📐 Total Area (sqft)",
    min_value=300,
    max_value=5000,
    step=50
)

bhk = st.sidebar.selectbox(
    "🛏️ BHK",
    options=[1, 2, 3, 4, 5]
)

bath = st.sidebar.selectbox(
    "🛁 Bathrooms",
    options=[1, 2, 3, 4]
)

st.sidebar.markdown("---")
st.sidebar.caption("✨ Built with Machine Learning")

# ---------- PREDICTION ----------
if st.button("✨ Predict Home Value"):
    input_data = np.array([[location, sqft, bath, bhk]])
    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="result-box">
            Estimated Property Value<br><br>
            ₹ {prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- FOOTER ----------
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Made with 💚 using Streamlit & Machine Learning")
