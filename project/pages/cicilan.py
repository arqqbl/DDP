import streamlit as st
import math

def kalkulator_kpr(jumlah, ratarata, tahun):
    """Fungsi untuk menghitung cicilan bulanan KPR."""
    # Ubah suku bunga tahunan ke bulanan
    ratarata_perbulan = ratarata / 12 / 100
    # Total bulan dalam masa pinjaman
    total_bulan = tahun * 12

    if ratarata_perbulan == 0:
        # Jika bunga 0%, cicilan sederhana
        bayaran_perbulan = jumlah / total_bulan
    else:
        # Rumus cicilan bulanan dengan bunga
        bayaran_perbulan = jumlah * (ratarata_perbulan * (1 + ratarata_perbulan)**total_bulan) / ((1 + ratarata_perbulan)**total_bulan - 1)

    return bayaran_perbulan

# Streamlit app
st.title("Kalkulator KPR")
st.write("Masukkan detail KPR Anda di bawah ini:")

# Input pengguna
jumlah = st.number_input("Jumlah Pinjaman (Rp):", min_value=0, value=500000000, step=1000000)
ratarata = st.number_input("Suku Bunga Tahunan (%):", min_value=0.0, value=5.0, step=0.1)
tahun = st.number_input("Lama Pinjaman (Tahun):", min_value=1, value=15, step=1)

# Tombol untuk menghitung
if st.button("Hitung Cicilan"):
    bayaran_perbulan = kalkulator_kpr(jumlah, ratarata, tahun)
    st.success(f"Cicilan Bulanan Anda adalah: Rp {bayaran_perbulan:,.2f}")

st.write("\n")
st.info("Catatan: Kalkulasi ini hanya estimasi dan tidak termasuk biaya tambahan seperti asuransi atau biaya administrasi.")
