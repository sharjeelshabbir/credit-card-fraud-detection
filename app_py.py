# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E6xYyAz6L5Q2LvChTbbBodPWiUB-2sRF
"""

pip install streamlit

import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

credit_card_data = pd.read_csv("creditcard.csv")

# Define the Streamlit app
def main():
    st.title("Credit Card Fraud Detection Interface")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile streamlit_app.py
# 
# # Define the Streamlit app
# def run_streamlit_app():
#     st.title("Credit Card Fraud Detection Interface")
# 
#     # Sidebar for user input
#     st.sidebar.header("User Input Parameters")
# 
#     # Display dataset
#     if st.sidebar.checkbox("Show Dataset"):
#         st.write(credit_card_data)
# 
#     # Split data into features (X) and target variable (y)
#     X = credit_card_data.drop("Class", axis=1)
#     y = credit_card_data["Class"]
# 
#     # Train-test split
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 
#     # Scale the features
#     scaler = StandardScaler()
#     X_train_scaled = scaler.fit_transform(X_train)
#     X_test_scaled = scaler.transform(X_test)
# 
#     # Train Logistic Regression model
#     model = LogisticRegression()
#     model.fit(X_train_scaled, y_train)
# 
#     # User input for prediction
#     user_input = {}
#     for col in X.columns:
#         user_input[col] = st.sidebar.number_input(f"Enter {col}", value=X[col].mean())
# 
#     # Make prediction
#     scaled_input = scaler.transform(pd.DataFrame(user_input, index=[0]))
#     prediction = model.predict(scaled_input)
# 
#     # Display prediction
#     st.subheader("Prediction")
#     if prediction[0] == 0:
#         st.write("No Fraud Detected")
#     else:
#         st.write("Fraud Detected")
# 
# # Run the Streamlit app
# if __name__ == "__main__":
#     run_streamlit_app()
# 
#

!streamlit run streamlit_app.py