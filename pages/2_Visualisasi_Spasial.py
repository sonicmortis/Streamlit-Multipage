import streamlit as st
import pandas as pd
import numpy as np

st.title("Visualisasi Spasial (Titik Lokasi)")

# --- 1. Membuat Data Spasial Sampel (Koordinat Bandung Raya) ---
np.random.seed(42)
n_points = 50
data = {
    # Latitude sekitar -6.9 (Bandung)
    'lat': -6.9 + np.random.normal(0, 0.05, n_points),
    # Longitude sekitar 107.6
    'lon': 107.6 + np.random.normal(0, 0.05, n_points),
    'value': np.random.randint(10, 100, n_points),
    'kategori': np.random.choice(['Titik Panas', 'Kepadatan Tinggi', 'Normal'], n_points)
}
df_spasial = pd.DataFrame(data)

st.write("**Data Sampel Posisi:**")
st.dataframe(df_spasial.head())

# --- 2. Filter Interaktif di Sidebar ---
st.sidebar.header("Filter Peta")
selected_cat = st.sidebar.multiselect(
    "Pilih Kategori", 
    options=df_spasial['kategori'].unique(), 
    default=df_spasial['kategori'].unique()
)

# Filter data
filtered_df = df_spasial[df_spasial['kategori'].isin(selected_cat)]

# --- 3. Menampilkan Peta Menggunakan st.map (Komponen Spasial!) ---
st.subheader("Peta Persebaran Titik")
st.map(filtered_df, latitude='lat', longitude='lon', size='value', color='#ff0000')

# --- 4. Informasi Tambahan ---
st.caption(f"Menampilkan {len(filtered_df)} dari {n_points} titik. Ukuran titik merepresentasikan nilai.")
st.info("💡 **Catatan Spasial**: Komponen `st.map` secara otomatis menangani plotting koordinat (Lat/Long). Untuk visualisasi yang lebih kompleks (heatmap, shapefile), Anda bisa menggunakan `pydeck` atau `folium`.")