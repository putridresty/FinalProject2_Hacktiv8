import pickle
import streamlit as st

model = pickle.load(open('rain_predict.sav', 'rb'))

st.title("Prediksi Hujan di Australia")

# Membagi visualisasi menjadi 2 kolom
col1, col2 = st.columns(2)

with col1:
    RainToday = st.number_input('cuaca hari ini (0=tidak hujan, 1=hujan)') #yesno ques
with col2:
    Rainfall = st.number_input('Berapa curah hujan hari ini?')
with col1:
    WindGustSpeed = st.number_input('Berapa nilai kecepatan angin pada hari sebelumnya?') #input select
with col2:
    WindSpeed9am = st.number_input('Berapa nilai kecepatan angin di sekitar jam 9 pagi?') #input selecr
with col1:
    WindSpeed3pm = st.number_input('Berapa nilai kecepatan angin di sekitar jam 3 sore?') #input select
with col2:
    Humidity9am = st.number_input('Berapa nilai kelembapan di sekitar jam 9 Pagi?')
with col1:
    Humidity3pm = st.number_input('Berapa nilai kelembapan di sekitar jam 3 sore?')
with col2:
    Month = st.number_input('Bulan ke berapakah saat ini?')    

predict = ''

if st.button("Prediksi Hujan pada Esok Hari"):
    predict = model.predict(
        [[RainToday, Rainfall, WindGustSpeed,
       WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Month]]
    )
    if(predict[0]==1):
        rain_predict = 'Besok akan turun hujan'
    else:
        rain_predict = 'Besok tidak akan turun hujan'
    
    st.success(rain_predict)
    