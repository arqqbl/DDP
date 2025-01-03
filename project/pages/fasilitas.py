import streamlit as st

def display_unit(nama_unit, image_paths, fasilitas):
    for img_path in image_paths:
        st.image(img_path, caption=f"Gambar: {img_path}", width=300)
    st.header("Fasilitas")
    for facility, detail in fasilitas.items():
        st.write(f"{facility} : {detail}")

unit = st.selectbox("Pilih Unit", ["Perumahan", "Unit A", "Unit B", "Unit C"])

if unit == "Unit A":
    display_unit("Unit A", ["Unit A.jpg"], {
        "🛏️ Kamar tidur": "3",
        "🛁 Kamar mandi": "2",
        "🏠 Rooftop": "1",
        "🅿️ Garasi": "7x5",
        "🏊‍♀️ Kolam renang": "1"
    })

elif unit == "Unit B":
    display_unit("Unit B", ["Unit B.jpg"], {
        "🛏️ Kamar tidur": "3",
        "🛁 Kamar mandi": "2",
        "🅿️ Garasi": "5x5"
    })

elif unit == "Unit C":
    display_unit("Unit C", ["Unit C.jpg"], {
        "🛏️ Kamar tidur": "3",
        "🛁 Kamar mandi": "2",
        "🅿️ Garasi": "5x3"
    })

elif unit == "Perumahan":
    st.header("Taman")
    st.write("Bayangkan Anda melangkah keluar dari rumah ke sebuah taman yang hijau dan penuh warna, di mana udara segar menyambut Anda setiap pagi, dan suara gemerisik dedaunan menciptakan ketenangan di sore hari. Taman ini bukan sekadar ruang hijau, tetapi juga tempat untuk merajut kebahagiaan bersama keluarga, menikmati momen bersama orang tercinta, dan menemukan kedamaian setelah hari yang sibuk")
    st.image("Taman.jpg", caption="Gambar: Taman", width=300)
    
    st.header("Playground")
    st.write("Yuk, temukan keseruan di playground! Tempat di mana tawa tak pernah habis, imajinasi tak terbatas, dan setiap permainan membawa cerita seru. Di sini, anak-anak bebas menjelajah, bermain, dan bersenang-senang sambil belajar. Ayo, jadikan hari ini penuh kenangan indah di playground yang tak terlupakan!")
    st.image("Playground.jpg", caption="Gambar: Playground", width=200)
    
    st.header("Masjid")
    st.write("Masjid bukan sekadar tempat ibadah, tapi juga rumah kedamaian, pusat ilmu, dan jembatan silaturahmi. Di sini, hati tenang dalam lantunan doa, pikiran tercerahkan dalam kajian, dan jiwa dipenuhi cinta kepada Sang Pencipta. Mari, jadikan masjid sebagai bagian dari perjalanan hidup kita, tempat menemukan makna sejati dan kekuatan untuk melangkah lebih baik setiap hari.")
    st.image("Masjid.jpg", caption="Gambar: Masjid", width=300)
    
    st.header("Lapangan")
    st.write("Lapangan olahraga adalah arena semangat dan perjuangan! Tempat di mana keringat menjadi bukti kerja keras, tawa dan sorak-sorai menyatu, serta persahabatan tumbuh dalam setiap permainan. Di sini, tubuh sehat, jiwa kuat, dan mimpi besar diraih bersama. Ayo, jadikan lapangan olahraga sebagai tempatmu beraksi dan menunjukkan potensi terbaikmu!")
    st.image("Lapangan.jpg", caption="Gambar: Lapangan", width=300)
