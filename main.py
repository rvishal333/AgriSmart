import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the crop recommendation data
Crop_recommendation_file_path = './Crop_recommendation.csv'
crop_data = pd.read_csv(Crop_recommendation_file_path)

# Define target variable 'y' and feature variables 'X'
y = crop_data['label']
crop_features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
X = crop_data[crop_features]

# Create and train the DecisionTreeClassifier model
crop_model = DecisionTreeClassifier(random_state=1)
X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=1)
crop_model.fit(X_train, y_train)

# Streamlit app UI
st.title("Crop Recommendation System")
st.write("Enter the soil and environmental conditions below to get the optimal crop recommendation.")

# Input fields for the user to enter data
N = st.number_input('Nitrogen content (N)', min_value=0, max_value=200, value=13)
P = st.number_input('Phosphorus content (P)', min_value=0, max_value=200, value=61)
K = st.number_input('Potassium content (K)', min_value=0, max_value=200, value=22)
temperature = st.number_input('Temperature (°C)', min_value=-10.0, max_value=60.0, value=19.0)
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, value=63.0)
ph = st.number_input('pH level', min_value=0.0, max_value=14.0, value=7.72)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, max_value=500.0, value=46.83)

# When the user clicks the button, make the prediction
if st.button('Predict Optimal Crop'):
    # Create a DataFrame from user inputs
    input_data = {
        'N': [N],
        'P': [P],
        'K': [K],
        'temperature': [temperature],
        'humidity': [humidity],
        'ph': [ph],
        'rainfall': [rainfall]
    }
    input_df = pd.DataFrame(input_data)

    # Make the prediction
    prediction = crop_model.predict(input_df)
    
    # Show the prediction result
    st.success(f"The recommended crop is: **{prediction[0]}**")

# Optionally, display the model accuracy
if st.checkbox("Show model accuracy"):
    predictions = crop_model.predict(X_valid)
    accuracy = accuracy_score(y_valid, predictions)
    st.write(f"Model accuracy: {accuracy * 100:.2f}%")