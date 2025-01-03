import streamlit as st
import pandas as pd

# Membuat sidebar dengan menu navigasi
menu = st.sidebar.selectbox("Pilih Menu", ["Menu 1: DataFrame", "Menu 2: Input Nama", "Menu 3: Kalkulator"])

# Menu 1: Menampilkan Data CSV
if menu == "Menu 1: DataFrame":
    st.header("Fitur 1: DataFrame")
    data = {
        'Nama': ['Alice', 'Bob', 'Charlie', 'David'],
        'Usia': [24, 30, 22, 35],
        'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Medan']
    }
    df = pd.DataFrame(data)
    st.write(df)

# Menu 2: Input Nama Pengguna
elif menu == "Menu 2: Input Nama":
    st.header("Fitur 2: Masukkan Nama Pengguna")
    
    # Input teks untuk nama
    user_name = st.text_input("Masukkan nama Anda:")
    
    # Menampilkan pesan sambutan jika nama dimasukkan
    if user_name:
        st.success(f"Selamat datang, {user_name}! Senang bertemu dengan Anda.")

# Menu 3: Kalkulator
elif menu == "Menu 3: Kalkulator":
    st.header("Fitur 3: Kalkulator Sederhana")
    
    # Slider untuk memilih angka
    number = st.slider("Pilih angka antara 1 dan 100", 1, 100)
    
    # Menampilkan hasil perkalian angka yang dipilih dengan 2
    result = number * 2
    st.write(f"Angka yang Anda pilih: {number}")
    st.write(f"Hasil perkalian angka dengan 2: {result}")