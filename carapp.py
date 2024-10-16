import pickle
import pandas as pd
import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="Cardheko Used Car Price Prediction", page_icon="🚗", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        color: #fff;
        background-color: #2C2F33;
    }
    .css-18e3th9 {
        background-color: #2C2F33;
    }
    h1 {
        color: #ffffb3 !important;
        text-align: center;
    }
    h2, h4 {
        color: #ff0066 !important;
    }
    h3 {
        color: #990099 !important;
    }
    .stSelectbox, .stSlider {
        background-color: #202225;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section
st.markdown("<h1>🚗 Car Dekho Used Car Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Used Car Resale Value Estimator!</h4>", unsafe_allow_html=True)
st.write("---")

# Sidebar for car selection input
st.sidebar.header("🚘 Select Car Specifications")

# Load data
df = pd.read_csv("D:\MDE94\capstoneprojects\CarDheko_Used_Car_Price_Prediction\df.csv")

# Sidebar inputs
Ft = st.sidebar.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'])
Bt = st.sidebar.selectbox("Body Type", ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans',
                                         'Convertibles', 'Hybrids', 'Wagon', 'Pickup Trucks'])
Tr = st.sidebar.selectbox("Transmission", ['Manual', 'Automatic'])
Owner = st.sidebar.selectbox("Owner Count", [0, 1, 2, 3, 4, 5])
Brand = st.sidebar.selectbox("Brand", options=df['Brand'].unique())

# Filter models based on selected Brand, Body Type, and Fuel Type
filtered_models = df[(df['Brand'] == Brand) & (df['body type'] == Bt) & (df['Fuel type'] == Ft)]['model'].unique()
Model = st.sidebar.selectbox("Model", options=filtered_models)

Model_year = st.sidebar.selectbox("Model Year", options=sorted(df['modelYear'].unique()))
IV = st.sidebar.selectbox("Insurance Validity", ['Third Party insurance', 'Comprehensive', 'Third Party',
                                                  'Zero Dep', 'Not Available'])
Km = st.sidebar.slider("Kilometers Driven", min_value=100, max_value=100000, step=1000)
ML = st.sidebar.number_input("Mileage (kmpl)", min_value=5, max_value=50, step=1)
Seats = st.sidebar.selectbox("Seats", options=sorted(df['Seats'].unique()))
Color = st.sidebar.selectbox("Color", df['Color'].unique())
City = st.sidebar.selectbox("City", options=df['City'].unique())

# Main layout for displaying selected data and predictions
col1, col2 = st.columns(2)

# Display the selected car details
with col1:
    st.subheader("📝 Selected Car Details")
    st.markdown(
        f"""
        - **Fuel Type**: {Ft}
        - **Body Type**: {Bt}
        - **Transmission**: {Tr}
        - **Owner Count**: {Owner}
        - **Brand**: {Brand}
        - **Model**: {Model}
        - **Model Year**: {Model_year}
        - **Insurance Validity**: {IV}
        - **Kilometers Driven**: {Km}
        - **Mileage**: {ML}
        - **Seats**: {Seats}
        - **Color**: {Color}
        - **City**: {City}
        """
    )

# Prediction section
with col2:
    st.subheader("💡 Price Prediction")
    st.markdown("Click below to predict the resale value of the car:")

    if st.button("Predict Car Price"):
        # Load the model pipeline
        with open('D:\MDE94\capstoneprojects\CarDheko_Used_Car_Price_Prediction\pipeline.pkl', 'rb') as f:
            pipeline = pickle.load(f)

        # Prepare the input data for the model
        input_data = pd.DataFrame({
            'Fuel type': [Ft],
            'body type': [Bt],
            'transmission': [Tr],
            'ownerNo': [Owner],
            'Brand': [Brand],
            'model': [Model],
            'modelYear': [Model_year],
            'Insurance Validity': [IV],
            'Kms Driven': [Km],
            'Mileage': [ML],
            'Seats': [Seats],
            'Color': [Color],
            'City': [City]
        })

        # Predict the price using the pipeline
        prediction = pipeline.predict(input_data)

        # Display the prediction result
        st.markdown(f"### 🏷️ Estimated Resale Value: **₹ {round(prediction[0], 2)}** lakhs")

# Footer with additional information
st.write("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p>🔧 Developed by <strong>Rameez J</strong> | Data Science Enthusiast 🚀</p>
    </div>
    """, 
    unsafe_allow_html=True
)