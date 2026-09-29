import streamlit as st
import pandas as pd 
import joblib

# loading the model
model = joblib.load("fraud_detection_pipeline.pkl")

# setting the title
st.title("Fraud Detection Prediction App")

st.markdown("PLease enter the transaction details and use predict button")

st.divider()   # a horizontal line to separate sections

# creating dropdown menu
transaction_type = st.selectbox("Transaction_type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])


amount = st.number_input("Amount",min_value = 0.0,value=1000.0)
oldbalanceOrg = st.number_input("Old Balance(Sender),min_values=0.0,value=10000.0")
newbalanceOrig = st.number_input("New Balance(Sender)",min_value=0.0,value = 9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)",min_value=0.0,value = 0.0)
newbalanceDest = st.number_input("New Balance(Receiver)",min_value=0.0,value = 0.0)


if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])   # }] properly closes the dictionary

    #prediction = model.predict(input_data())[0]
    prediction = model.predict(input_data)

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1 :
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")


# run on terminal : streamlit run fraud_detection.py
