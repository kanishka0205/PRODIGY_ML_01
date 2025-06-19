import pickle as pk
import pandas as pd
import streamlit as st 

model = pk.load(open('D:\CODE\PriceofHouse\House_prediction_model.pkl','rb'))

st.header('House Price Predictor')
data = pd.read_csv('D:\CODE\PriceofHouse\Cleaned_data.csv')

Id = st.selectbox("Choose the ID",data['Id'].unique())
sqft = st.number_input("Enter Total Sqft")
beds = st.number_input("Enter No of Bedrooms")
baths = st.number_input("Enter No of Bathrooms")

input = pd.DataFrame([[Id,sqft,baths,beds]], columns = ['Id','LotArea','FullBath','BedroomAbvGr'])

if st.button("Predict Price"):
    output = model.predict(input)
    st.success("Price of the House is ₹{:,.2f}".format(output[0]))


