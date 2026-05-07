import streamlit as st
import pandas as pd
import numpy as np

st.title("Eksplorasi Komponen Streamlit")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Controls")
    nama = st.text_input("Masukkan Nama")
    umur = st.slider("Pilih Rentang Umur", 0, 100, (20, 50))
    warna = st.selectbox("Pilih Warna Favorit", ["Merah", "Biru", "Hijau"])

with col2:
    st.subheader("Output Display")
    if nama:
        st.write(f"Halo **{nama}**!")
    st.write(f"Rentang Umur: **{umur[0]} - {umur[1]}** tahun")
    st.write(f"Warna favorit: **{warna}**")

st.markdown("---")
st.subheader("Contoh Dataframe Interaktif")
data = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])
st.dataframe(data.style.highlight_max(axis=0))