import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")


# Judul dan subjudul
st.header('Data Collection Bike Sharing :sparkles:')
st.subheader('Weather Conditions with the most Bicycle Rentals')

# Sidebar
with st.sidebar:
    # Logo perusahaan
    st.image("bike.png")

# Caption
st.caption('Bike Sharing Every Day')

# Membuat plot
sum_order_items_df = day_df.groupby("weathersit").cnt.sum().sort_values(ascending=False).reset_index()
st.dataframe(sum_order_items_df)


fig, ax = plt.subplots(figsize=(12, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Mapping cuaca dengan label
weather_labels = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
}

# Mengganti nilai weathersit dengan label
sum_order_items_df['weathersit_label'] = sum_order_items_df['weathersit'].map(weather_labels)

# Merubah range pada sumbu y
y_range = {
    'Cerah': 2257952,
    'Berawan': 996858,
    'Hujan Ringan': 37869,
}

sns.barplot(x="weathersit_label", y="cnt", data=sum_order_items_df.head(5), palette=colors, ax=ax)
ax.set_ylabel("Jumlah Total Penyewa Sepeda")
ax.set_xlabel("Cuaca")
ax.set_title("Korelasi Kondisi Cuaca dengan Jumlah Sewa Sepeda", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=12)

# Mengatur range pada sumbu y
ax.set_yticks([0, 500000, 1000000, 1500000, 2000000, 2500000])
ax.set_yticklabels(['0', '500,000', '1,000,000', '1,500,000', '2,000,000', '2,500,000'])

# Menampilkan plot di Streamlit
st.pyplot(fig)


st.caption('Bike Sharing Every Hour')

sum_order_items_df = hour_df.groupby("weathersit").cnt.sum().sort_values(ascending=False).reset_index()
st.dataframe(sum_order_items_df)


fig, ax = plt.subplots(figsize=(12, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Mapping cuaca dengan label
weather_labels = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
    4: 'Hujan Lebat'
}

# Mengganti nilai weathersit dengan label
sum_order_items_df['weathersit_label'] = sum_order_items_df['weathersit'].map(weather_labels)

# Merubah range pada sumbu y
y_range = {
    'Cerah': 2338173,
    'Berawan': 795952,
    'Hujan Ringan': 158331,
    'Hujan Lebat' : 223
}

sns.barplot(x="weathersit_label", y="cnt", data=sum_order_items_df.head(5), palette=colors, ax=ax)
ax.set_ylabel("Jumlah Total Penyewa Sepeda")
ax.set_xlabel("Cuaca")
ax.set_title("Korelasi Kondisi Cuaca dengan Jumlah Sewa Sepeda", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=12)

# Mengatur range pada sumbu y
ax.set_yticks([0, 500000, 1000000, 1500000, 2000000, 2500000])
ax.set_yticklabels(['0', '500,000', '1,000,000', '1,500,000', '2,000,000', '2,500,000'])

st.pyplot(fig)

st.caption('© 2024 Zumroatul Afifah. All rights reserved.')




