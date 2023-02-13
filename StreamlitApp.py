import streamlit as st
import numpy as np
import pandas as pd
import joblib
import time

model = joblib.load('rfc.joblib')
st.title('Will it rain tomorrow? :umbrella_with_rain_drops:')
col1, col2, col3 = st.columns(3)

# ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine','WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm','WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm','Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm', 'RainToday']
MinTemp = col1.number_input("Minimum temperature", 0,100) 
MaxTemp = col1.number_input("Maximum temperature", 0,100) 
Rainfall = col1.number_input("Amount of rain", 0,400)
Evaporation =col1.number_input("Amount of evaporation ", 0, 100)
Sunshine = col1.number_input('For how many hours sun was out today', 0,10)
WindGustDir = col1.selectbox("Direction of the strongest wind", ['SW', 'NNE', 'NNW', 'SSE', 'W', 'S', 'NW', 'E', 'ENE', 'N', 'WSW','SE', 'ESE', 'WNW', 'SSW', 'NE'])
WindGustSpeed = col2.number_input("Speed of the strongest wind ", 0, 150)
WindDir9am = col2.selectbox("Wind direction at 9am",['SSW', 'SW', 'N', 'SE', 'NW', 'W', 'ENE', 'NNE', 'WNW', 'SSE','NE', 'E', 'WSW', 'S', 'NNW', 'ESE'])
WindDir3pm = col2.selectbox("Wind direction at 3pm", ['SSW', 'SW', 'N', 'SE', 'NW', 'W', 'ENE', 'NNE', 'WNW', 'SSE','NE', 'E', 'WSW', 'S', 'NNW', 'ESE'])
WindSpeed9am = col2.number_input("Wind speed at 9am", 0,100)
WindSpeed3pm = col2.number_input("Wind speed at 3pm", 0,100)
Humidity9am = col2.number_input("Humidity at 9am", 0,100)
Humidity3pm = col3.number_input("Humidity at 3pm", 0,100)
Pressure9am = col3.number_input("Pressure at 9am", 0,100)
Pressure3pm = col3.number_input("Pressure at 3pm", 0,100)
Temp9am = col3.number_input("Temperature at 9am", 0,100) 
Temp3pm = col3.number_input("Temperature at 3pm ", 0,100) 
RainToday = col3.select_slider("Did it rain today?", ['No','Yes'])

def predict(): 
    columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine','WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm','WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm','Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm', 'RainToday']
    row = np.array([MinTemp,MaxTemp,Rainfall,Evaporation,Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Temp9am,Temp3pm,RainToday]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    progress_bar = st.progress(0)
    for percent_completed in range(100):
        time.sleep(0.005)
        progress_bar.progress(percent_completed+1)
    if prediction[0] == "Yes": 
        st.success('It will rain tomorrow  :rain_cloud:')
    else: 
        st.error('It will be sunny tomorrow :sun_with_face:') 

trigger = col1.button('Predict', on_click=predict)