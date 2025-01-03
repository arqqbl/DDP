import streamlit as st

dashboard = st.Page("./pages/dashboard.py", title= "Dashboard")
fasilitas = st.Page("./pages/fasilitas.py", title= "Fasilitas")
cicilan = st.Page("./pages/cicilan.py", title= "Cicilan")
data_cicilan = st.Page("./pages/data_cicilan.py", title= "Data Cicilan")

pg = st.navigation({
    "Dashboard": [dashboard],
    "Fasilitas": [fasilitas],
    "Cicilan": [cicilan],
    "Data Cicilan": [data_cicilan],

})
pg.run()




