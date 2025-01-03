import streamlit as st
from PIL import Image


st.title("Bukti Pembayaran")
 
with st.form("cicilan"):
    Nama_Lengkap = st.text_input("Masukkan Nama Lengkap")
    No_Telepon= st.text_input("Masukkan No Telepon")
    Alamat_Email = st.text_input("Masukkan Alamat Email")
    Bulan_Berapa = st.text_input("Bulan ke berapa")
    pembayaran = st.text_input("Pembayaran")
    uploaded_file = st.file_uploader("Silakan unggah bukti pembayaran:", type=["jpg", "jpeg", "png"])


    submitButton = st.form_submit_button("Simpan")

    if submitButton:
        st.write(Nama_Lengkap)
        st.write(No_Telepon)
        st.write(Alamat_Email)
        st.write(Bulan_Berapa)
        st.write(pembayaran)
        image = Image.open(uploaded_file)
        st.image(image, caption="Foto yang diunggah", use_column_width=True)

        if 'Cicilan' not in st.session_state:
            st.session_state.Nabung = []

        st.session_state['Nabung'].append({
            "Nama Lengkap": Nama_Lengkap,
            "No Telepon": No_Telepon,
            "Alamat Email": Alamat_Email,
            
        })
        st.success("Berhasil!")


    
 