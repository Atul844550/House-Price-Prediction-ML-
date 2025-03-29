import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

def predict_price(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

# Streamlit UI
st.set_page_config(page_title="California Housing Price Prediction", layout="centered")

st.markdown(
    """
    <style>
        .big-font {font-size:24px !important; font-weight: bold; text-align: center;}
        .stButton>button {width: 100%; border-radius: 12px; font-size: 18px; background-color: #4CAF50; color: white;}
        .stTextInput>div>div>input {font-size: 16px;}
        .sidebar .sidebar-content {background-color: #f0f2f6;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏡 California Housing Price Prediction")
st.markdown("<p class='big-font'>Predict the Median House Price Based on Given Features</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar input fields
st.sidebar.header("🔍 Enter Housing Features")
MedInc = st.sidebar.number_input("💰 Median Income (scaled)", min_value=0.0, max_value=20.0, value=3.0)
HouseAge = st.sidebar.number_input("🏠 House Age", min_value=0, max_value=100, value=30)
AveRooms = st.sidebar.number_input("🛏️ Average Rooms per Household", min_value=0.0, max_value=20.0, value=5.0)
AveBedrms = st.sidebar.number_input("🛌 Average Bedrooms per Household", min_value=0.0, max_value=10.0, value=1.0)
Population = st.sidebar.number_input("👨‍👩‍👧 Population", min_value=0, max_value=50000, value=1500)
AveOccup = st.sidebar.number_input("👥 Average Occupancy", min_value=0.0, max_value=10.0, value=3.0)
Latitude = st.sidebar.number_input("📍 Latitude", min_value=30.0, max_value=50.0, value=35.0)
Longitude = st.sidebar.number_input("📍 Longitude", min_value=-130.0, max_value=-110.0, value=-120.0)

input_data = [MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]

# Predict button
if st.sidebar.button("🚀 Predict Price"):
    predicted_price = predict_price(input_data)
    st.markdown(f"<p class='big-font' style='color: #4CAF50;'>🏠 Predicted Median House Price: <br> <span style='font-size:32px;'>${predicted_price * 100000:.2f}</span></p>", unsafe_allow_html=True)


