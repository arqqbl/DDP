import streamlit as st

st.title("꧁༺NF Terrace༻꧂")
st.write("")
st.write("Konsep utama yang Nf Terrace tawarkan kepada \nkonsumen adalah hunian Private Townhouse yang \nmengutamakan keamanan lingkungan, kenyamanan &\n kesehatan dalam rumah.")
st.write("Kami juga memberikan Water Management yang prima di setiap rumah. Kami percaya bahwa air merupakan kebutuhan primer manusia yang perlu dijaga kualitasnya agar senantiasa jernih, bebas bakteri dan tidak berbau.")
st.write("Area Townhouse dengan akses satu pintu (One Gate System), Security & CCTV 24 Jam.")
st.write("Tidak hanya lokasi yang super strategis, kami membangun rumah yang kuat, kokoh dengan material standar Jepang.")
st.write("Setiap unit rumah di Nf Terrace memiliki Ceiling yang tinggi dan jendela besar agar konsumen merasa sejuk dan memberi sirkulasi udara terbaik dalam rumah")
st.write("Anda berhak memiliki rumah dengan spek premium dan investasi jangka panjang yang terus meningkat. Nf Terrace berlokasi di area Kota Depok, dengan nilai NJOP yang terus meningkat tajam setiap tahun.")
   
images = ["Unit A.jpg","Unit B.jpg","Unit C.jpg"]
for img_path in images:
        st.image(img_path, caption=f"Gambar: {img_path}", width=500)

st.session_state['data_cicilan']

