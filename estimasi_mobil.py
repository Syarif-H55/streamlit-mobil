import pickle
import streamlit as st

# Memuat model yang telah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# Input dari pengguna
year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

# Tombol untuk melakukan prediksi
if st.button('Estimasi Harga'):
    # Melakukan prediksi menggunakan model
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )

    # Menampilkan hasil prediksi dalam Ponds dan IDR (Juta)
    st.write('Estimasi harga mobil bekas dalam Ponds :', predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta) :', predict * 19000)