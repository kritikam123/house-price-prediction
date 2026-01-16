import streamlit as st
import pickle
import numpy as np
import json

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="HomeWorth",
    page_icon="🏡",
    layout="centered"
)

# ---------- LOAD MODEL ----------
with open("bangalore_home_prices_model.pickle", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)

locations = data_columns[3:]  # first 3 are sqft, bath, bhk


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
    '<div class="subtitle">A ML-powered real estate price predictor</div>',
    unsafe_allow_html=True
)

# ---------- SIDEBAR INPUT ----------
st.sidebar.header("Property Details")

location = st.sidebar.selectbox(
    " Location",
    sorted(locations)
)


sqft = st.sidebar.slider(
    " Total Area (sqft)",
    min_value=300,
    max_value=5000,
    step=50
)

bhk = st.sidebar.selectbox(
    " BHK",
    options=[1, 2, 3, 4, 5]
)

bath = st.sidebar.selectbox(
    " Bathrooms",
    options=[1, 2, 3, 4]
)

st.sidebar.markdown("---")

if st.button("Predict Home Value"):
    x = np.zeros(len(data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    prediction = model.predict([x])[0]

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
