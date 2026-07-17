import streamlit as st
import pickle
import pandas as pd

model =pickle.load(open("model.pkl","rb"))

st.title("Myntra High Rating Prediction")

price=st.number_input("price",min_value=0.0,value=1000.0)

mrp=st.number_input("MRP",min_value=0.0,value=1500.0)

discount=st.number_input("Discount Percentage",min_value=0.0,value=20.0)

number_of_ratings=st.number_input("Number of Ratings",min_value=0,value=100)

brand=st.number_input("Brand code",min_value=0,value=1)

description=st.number_input("Description Code",min_value=0,value=1)

fashioncategory=st.number_input("Fashion Category code",min_value=0,value=1)

if st.button("predict"):
    data=pd.DataFrame(
        [[brand,
          description,
          fashioncategory,
          price,
          mrp,
          discount,
          number_of_ratings]],
        columns=["brand_name", "pants_description", "fashioncategory", "price", "MRP",
       "discount_percent", "number_of_ratings"])

    prediction=model.predict(data)
    
    if prediction[0]==1:
        st.success("High Rated Product")
    else:
        st.error("Low Rated Product")
    