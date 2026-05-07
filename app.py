import streamlit as st

st.set_page_config(page_title="Tugas Visualisasi", page_icon="🌍", layout="wide")

st.title("Dashboard Visualisasi Spasio-temporal")
st.markdown("---")
st.write("""
Selamat datang di dashboard tugas **Kelompok Genap**.
Gunakan menu di samping kiri untuk navigasi:
- **Home**: Halaman ini.
- **Eksplorasi Komponen**: Melihat berbagai widget Streamlit.
- **Visualisasi Spasial**: Menampilkan data pada peta interaktif.
- **Analisis Temporal**: Menampilkan tren berdasarkan waktu.
""")

# Menampilkan data di sidebar (opsional)
st.sidebar.success("Pilih halaman di atas.")