import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Analisis Temporal (Berdasarkan Waktu)")

# --- 1. Membuat Data Time Series Sampel ---
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='ME')
nilai = np.random.randint(50, 150, size=len(dates))
df_temporal = pd.DataFrame({'Tanggal': dates, 'Nilai': nilai})

st.write("**Data Time Series Sampel:**")
st.dataframe(df_temporal)

# --- 2. Slider Waktu (Komponen Temporal) ---
st.subheader("Filter Rentang Waktu")
min_date = df_temporal['Tanggal'].min().date()
max_date = df_temporal['Tanggal'].max().date()

range_date = st.slider(
    "Pilih Rentang Bulan",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM"
)

# Konversi ke datetime dan filter
start_date, end_date = pd.to_datetime(range_date[0]), pd.to_datetime(range_date[1])
mask = (df_temporal['Tanggal'] >= start_date) & (df_temporal['Tanggal'] <= end_date)
filtered_temporal = df_temporal.loc[mask]

# --- 3. Visualisasi Grafik Interaktif ---
st.subheader("Grafik Tren Nilai")
fig = px.line(filtered_temporal, x='Tanggal', y='Nilai', 
              title='Perubahan Nilai dari Waktu ke Waktu',
              markers=True, template='plotly_white')
fig.update_layout(xaxis_title="Periode Waktu", yaxis_title="Nilai")
st.plotly_chart(fig, use_container_width=True)
