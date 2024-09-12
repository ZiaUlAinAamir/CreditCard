import streamlit as st
import pickle
import pandas as pd

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaller.pkl', 'rb') as file:
    scaller = pickle.load(file)


st.set_page_config(
    page_title="Credit Card"




)

st.title("Credit Card")


# Define the form to take inputs from the user
st.title('Customer Data Input Form')

# Input fields for customer data
CUST_ID = st.text_input("Customer ID", "C12345")
BALANCE = st.number_input("Balance", 2500.75)
BALANCE_FREQUENCY = st.number_input("Balance Frequency", 0.9)
PURCHASES = st.number_input("Purchases", 1500.00)
ONEOFF_PURCHASES = st.number_input("One-off Purchases", 1000.00)
INSTALLMENTS_PURCHASES = st.number_input("Installments Purchases", 500.00)
CASH_ADVANCE = st.number_input("Cash Advance", 1200.00)
PURCHASES_FREQUENCY = st.number_input("Purchases Frequency", 0.8)
ONEOFF_PURCHASES_FREQUENCY = st.number_input("One-off Purchases Frequency", 0.6)
PURCHASES_INSTALLMENTS_FREQUENCY = st.number_input("Purchases Installments Frequency", 0.7)
CASH_ADVANCE_FREQUENCY = st.number_input("Cash Advance Frequency", 0.5)
CASH_ADVANCE_TRX = st.number_input("Cash Advance Transactions", 10, step=1)
PURCHASES_TRX = st.number_input("Purchases Transactions", 25, step=1)
CREDIT_LIMIT = st.number_input("Credit Limit", 5000.00)
PAYMENTS = st.number_input("Payments", 2000.00)
MINIMUM_PAYMENTS = st.number_input("Minimum Payments", 300.00)
PRC_FULL_PAYMENT = st.number_input("Percentage of Full Payment", 0.85)
TENURE = st.number_input("Tenure", 10, step=1)

# Button to submit the form
if st.button('Submit'):
    # Create dictionary with the user inputs
    customer_data = {
        "CUST_ID": [CUST_ID],
        "BALANCE": [BALANCE],
        "BALANCE_FREQUENCY": [BALANCE_FREQUENCY],
        "PURCHASES": [PURCHASES],
        "ONEOFF_PURCHASES": [ONEOFF_PURCHASES],
        "INSTALLMENTS_PURCHASES": [INSTALLMENTS_PURCHASES],
        "CASH_ADVANCE": [CASH_ADVANCE],
        "PURCHASES_FREQUENCY": [PURCHASES_FREQUENCY],
        "ONEOFF_PURCHASES_FREQUENCY": [ONEOFF_PURCHASES_FREQUENCY],
        "PURCHASES_INSTALLMENTS_FREQUENCY": [PURCHASES_INSTALLMENTS_FREQUENCY],
        "CASH_ADVANCE_FREQUENCY": [CASH_ADVANCE_FREQUENCY],
        "CASH_ADVANCE_TRX": [CASH_ADVANCE_TRX],
        "PURCHASES_TRX": [PURCHASES_TRX],
        "CREDIT_LIMIT": [CREDIT_LIMIT],
        "PAYMENTS": [PAYMENTS],
        "MINIMUM_PAYMENTS": [MINIMUM_PAYMENTS],
        "PRC_FULL_PAYMENT": [PRC_FULL_PAYMENT],
        "TENURE": [TENURE]
    }

    # Convert dictionary to DataFrame
    data = pd.DataFrame(customer_data)


    data.MINIMUM_PAYMENTS = data.MINIMUM_PAYMENTS.astype(float)
    data.CUST_ID = data.CUST_ID.str.replace("C", "").astype(int)

    scaled_data = scaller.transform(data)
    cluster_prediction = model.predict(scaled_data)

    st.success(f"The new data belongs to cluster: {cluster_prediction[0]}")