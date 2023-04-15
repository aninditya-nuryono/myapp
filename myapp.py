from scipy.stats import pearsonr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from scipy.stats import ttest_ind
import streamlit as st
from PIL import Image

image = Image.open('C:/Users/anind/OneDrive/Desktop/bike.jpg')
st.sidebar.image(image, caption='bike sharing', use_column_width=True)

st.header(
    """
    Dicoding Bike Sharing Dashbord 
    """
)


hour = pd.read_csv('hour.csv')
day = pd.read_csv('day.csv')


# Menampilkan informasi dari dataframe hour
hour.info()

# Menampilkan deskripsi statistik dari dataframe hour
hour.describe()

# Memeriksa apakah ada missing value dari dataframe hour
hour.isna().sum()

# Menampilkan informasi dari dataframe day
day.info()

# Menampilkan deskripsi statistik dari dataframe day
day.describe()

# Memeriksa apakah ada missing value dari dataframe day
day.isna().sum()


print("Jumlah duplikasi: ", hour.duplicated().sum())
hour.describe()


print("Jumlah duplikasi: ", day.duplicated().sum())
day.describe()


plt.figure(figsize=(8, 6))
plt.boxplot([hour[hour['weathersit']==1]['cnt'],
             hour[hour['weathersit']==2]['cnt'],
             hour[hour['weathersit']==3]['cnt'],
             hour[hour['weathersit']==4]['cnt']],
            labels=['Cuaca Cerah', 'Cuaca Berawan/Kabut', 'Cuaca Hujan Salju Ringan', 'Cuaca Hujan Salju Berat'])
plt.title('Pengaruh Cuaca terhadap Penggunaan Sepeda pada Hour Dataset')
plt.ylabel('Jumlah Sepeda Dipinjam')
plt.xlabel('Weathersit')
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot([day[day['weathersit']==1]['cnt'],
             day[day['weathersit']==2]['cnt'],
             day[day['weathersit']==3]['cnt'],
             day[day['weathersit']==4]['cnt']],
            labels=['Cuaca Cerah', 'Cuaca Berawan/Kabut', 'Cuaca Hujan Salju Ringan', 'Cuaca Hujan Salju Berat'])
plt.title('Pengaruh Cuaca terhadap Penggunaan Sepeda pada Day Dataset')
plt.ylabel('Jumlah Sepeda Dipinjam')
plt.xlabel('Weathersit')
plt.show()


# Data setiap jam
sns.boxplot(x='weathersit', y='cnt', hue='workingday', data=hour)
plt.title('Boxplot Weathersit dan Jumlah Sepeda yang Dipinjam pada Hari Kerja dan Hari Libur')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Sepeda yang Dipinjam')
plt.show()



# Data Harian
sns.boxplot(x='season', y='cnt', hue='workingday', data=day)
plt.title('Cuaca dan Jumlah Sepeda yang Dipinjam pada Hari Kerja dan Hari Libur')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Sepeda yang Dipinjam')
plt.show()


hour.isnull().sum()

day.isnull().sum()


plt.figure(figsize=(15,12))
plt.subplots_adjust(hspace = 0.5)

plt.subplot(4, 4, 1)
sns.histplot(data=hour, x='instant', kde=True)
plt.xlabel('Instant')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 2)
sns.histplot(data=hour, x='season', kde=True)
plt.xlabel('Musim')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 3)
sns.histplot(data=hour, x='yr', kde=True)
plt.xlabel('Tahun')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 4)
sns.histplot(data=hour, x='mnth', kde=True)
plt.xlabel('Bulan')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 5)
sns.histplot(data=hour, x='hr', kde=True)
plt.xlabel('Jam')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 6)
sns.histplot(data=hour, x='holiday', kde=True)
plt.xlabel('Hari Libur')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 7)
sns.histplot(data=hour, x='weekday', kde=True)
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 8)
sns.histplot(data=hour, x='workingday', kde=True)
plt.xlabel('Hari Kerja')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 9)
sns.histplot(data=hour, x='weathersit', kde=True)
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 10)
sns.histplot(data=hour, x='temp', kde=True)
plt.xlabel('Suhu (Celsius)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 11)
sns.histplot(data=hour, x='atemp', kde=True)
plt.xlabel('Suhu Perasaan (Celsius)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 12)
sns.histplot(data=hour, x='hum', kde=True)
plt.xlabel('Kelembaban (%)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 13)
sns.histplot(data=hour, x='windspeed', kde=True)
plt.xlabel('Kecepatan Angin (km/jam)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 14)
sns.histplot(data=hour, x='casual', kde=True)
plt.xlabel('Jumlah Pengguna Casual')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 15)
sns.histplot(data=hour, x='registered', kde=True)
plt.xlabel('Jumlah Pengguna Registered')
plt.ylabel('Frekuensi')


plt.figure(figsize=(15,12))
plt.subplots_adjust(hspace = 0.5)

plt.subplot(4, 4, 1)
sns.histplot(data=day, x='instant', kde=True)
plt.xlabel('Instant')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 2)
sns.histplot(data=day, x='season', kde=True)
plt.xlabel('Musim')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 3)
sns.histplot(data=day, x='yr', kde=True)
plt.xlabel('Tahun')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 4)
sns.histplot(data=day, x='mnth', kde=True)
plt.xlabel('Bulan')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 5)
sns.histplot(data=day, x='holiday', kde=True)
plt.xlabel('Hari Libur')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 6)
sns.histplot(data=day, x='weekday', kde=True)
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 7)
sns.histplot(data=day, x='workingday', kde=True)
plt.xlabel('Hari Kerja')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 8)
sns.histplot(data=day, x='weathersit', kde=True)
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 9)
sns.histplot(data=day, x='temp', kde=True)
plt.xlabel('Suhu (Celsius)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 10)
sns.histplot(data=day, x='atemp', kde=True)
plt.xlabel('Suhu Perasaan (Celsius)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 11)
sns.histplot(data=day, x='hum', kde=True)
plt.xlabel('Kelembaban (%)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 12)
sns.histplot(data=day, x='windspeed', kde=True)
plt.xlabel('Kecepatan Angin (km/jam)')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 13)
sns.histplot(data=day, x='casual', kde=True)
plt.xlabel('Jumlah Pengguna Casual')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 14)
sns.histplot(data=day, x='registered', kde=True)
plt.xlabel('Jumlah Pengguna Registered')
plt.ylabel('Frekuensi')

plt.subplot(4, 4, 15)
sns.histplot(data=day, x='cnt', kde=True)
plt.xlabel('Jumlah Total Pengguna')
plt.ylabel('Frekuensi')


sns.heatmap(hour.corr(), annot=True, cmap='coolwarm')


hour.hist(bins=15, figsize=(15,10))
plt.show()

hour.hist(bins=15, figsize=(15,10))
plt.show()



hour[['registered', 'casual']].describe()

st.subheader('Pengaruh Cuaca')

# buat  line plot
#fig_u, ax = plt.subplots(figsize=(4, 3))
fig_u, ax = plt.subplots(figsize=(4, 3))
sns.lineplot(data=hour, x='hr', y='cnt', hue='weathersit', palette=['green', 'blue', 'red', 'purple'], ax=ax)

# Set labels and titles
ax.set_title('Peminjaman Sepeda Berdasarkan Waktu dan Kondisi Cuaca', fontsize=7)
ax.set_xlabel('Waktu (Jam)', fontsize=6)
ax.set_ylabel('Jumlah Sepeda Dipinjam', fontsize=6)
ax.legend(labels=['Cerah', 'Berawan', 'Hujan Ringan/Salju Ringan', 'Hujan Berat/Salju Berat'], prop={'size': 4})

fig_u.set_size_inches(4, 3)
fig_u.tight_layout()

# Display plot
st.pyplot(fig_u)


with st.expander("Deskripsi"):
    st.write(
        """
        Pada 'Cerah' memiliki warna hijau, 'Berawan' memiliki warna biru, 'Hujan Ringan/Salju Ringan' memiliki warna merah, dan 'Hujan Berat/Salju Berat' memiliki warna ungu.
        
        Cuaca memiliki pengaruh yang signifikan pada penggunaan sepeda.penggunaan sepeda menurun dibandingkan dengan hari-hari dengan cuaca yang baik. Pada penggunaan sepeda harian, cuaca yang buruk (weathersit=4) memiliki pengaruh negatif terhadap penggunaan sepeda, sedangkan cuaca yang baik (weathersit=1) memiliki pengaruh positif terhadap penggunaan sepeda.

        Selain itu, pada penggunaan sepeda secara harian dan mingguan, terlihat bahwa semakin buruk cuaca maka semakin sedikit orang yang menggunakan sepeda. Sedangkan pada penggunaan sepeda secara jam, terlihat bahwa cuaca buruk memiliki pengaruh negatif terhadap penggunaan sepeda pada jam-jam tertentu, terutama pada jam sibuk (jam 7-9 pagi dan jam 4-6 sore).
        
        """
    )


corr_hour = np.corrcoef(hour['weathersit'], hour['cnt'])[0, 1]
print('Nilai korelasi Pearson antara variabel weathersit dan cnt pada file hour.csv adalah:', corr_hour)



corr_day = np.corrcoef(day['weathersit'], day['cnt'])[0, 1]
print('Nilai korelasi Pearson antara variabel weathersit dan cnt pada file day.csv adalah:', corr_day)



weekday_df = day[day['workingday'] == 1]
holiday_df = day[day['workingday'] == 0]



working_day_rentals = weekday_df['cnt'].sum()
holiday_rentals = holiday_df['cnt'].sum()


plt.bar(['Hari Kerja', 'Hari Libur'], [working_day_rentals, holiday_rentals])
plt.title('Peminjaman Sepeda Antara Hari Kerja dan Hari Libur')
plt.ylabel('Jumlah Peminjaman Sepeda')
plt.show()



weekday_std = weekday_df['cnt'].std()
holiday_std = holiday_df['cnt'].std()

weekday_mean = int(weekday_df['cnt'].mean())
holiday_mean = int(holiday_df['cnt'].mean())

weekday_median = weekday_df['cnt'].median()
holiday_median = holiday_df['cnt'].median()



print("Standar deviasi jumlah sepeda pada hari kerja: ", weekday_std)
print("Standar deviasi jumlah sepeda pada hari libur: ", holiday_std)

print("Rata-rata jumlah sepeda pada hari kerja: ", weekday_mean)
print("Rata-rata jumlah sepeda pada hari libur: ", holiday_mean)

st.subheader('Distribusi Pinjaman Sepeda')

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Avg working day", value=weekday_mean)

with col2:
    st.metric(label="Avg holiday", value=holiday_mean)

print("Median jumlah sepeda pada hari kerja: ", weekday_median)
print("Median jumlah sepeda pada hari libur: ", holiday_median)


# Data
labels = ['Hari Kerja', 'Hari Libur']
mean_values = [weekday_mean, holiday_mean]

# Assign colors based on values
colors = ['green' if value == max(mean_values) else 'blue' for value in mean_values]

# Plotting
x = np.arange(len(labels))
width = 0.7

fig_a, ax = plt.subplots()
rects2 = ax.bar(x, mean_values, width, label='Rata-rata tertinggi', color=colors)

ax.set_ylabel('Jumlah Sepeda', fontsize=6)
ax.set_title('Jumlah Sepeda Dipinjam', fontsize=7)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=6)
ax.legend()
ax.legend(prop={'size': 4})

fig_a.set_size_inches(4, 3)
fig_a.tight_layout()

st.pyplot(fig_a)

with st.expander("Deskripsi"):
    st.write(
        """
        Rata-rata jumlah sepeda yang dipinjam pada hari kerja (4584) lebih tinggi daripada pada hari libur (4330). Hal ini menunjukkan bahwa pada hari kerja, penggunaan sepeda lebih tinggi dibandingkan pada hari libur.
        
        Uji hipotesis yang digunakan adalah uji t-test independen. Uji hipotesis t-test independen dengan tujuan untuk mengetahui apakah terdapat perbedaan yang signifikan dalam rata-rata jumlah peminjaman sepeda antara hari kerja dan hari libur pada dataset Bike Sharing.
        
        Hipotesis yang akan diuji adalah sebagai berikut:
        <ul>
        <li>Hipotesis nol (H0): Tidak ada perbedaan yang signifikan dalam rata-rata jumlah peminjaman sepeda antara hari kerja dan hari libur.</li>
        <li>Hipotesis alternatif (H1): Ada perbedaan yang signifikan dalam rata-rata jumlah peminjaman sepeda antara hari kerja dan hari libur.</li>
        </ul>
        
        Berdasarkan hasil uji hipotesis menggunakan t-test independen, diperoleh nilai t-stat sebesar 1.601 dan p-value sebesar 0.110. Karena p-value lebih besar dari level of significance yang telah ditetapkan (0.05), maka hipotesis nol tidak dapat ditolak yang menyatakan bahwa tidak ada perbedaan yang signifikan dalam rata-rata jumlah peminjaman sepeda antara hari kerja dan hari libur.
        """
        ,
        unsafe_allow_html=True,
    )


# mengambil data untuk hari kerja
weekday_data = day[day['workingday'] == 1]['cnt']
# mengambil data untuk hari libur
holiday_data = day[day['weekday'] == 0]['cnt']



t_stat, p_value = ttest_ind(weekday_data, holiday_data, equal_var=False)



alpha = 0.05


print("Nilai t-stat: ", t_stat)
print("Nilai p-value: ", p_value)

if p_value < alpha:
  print("Ada perbedaan yang signifikan dalam rata-rata jumlah peminjaman sepeda antara hari kerja dan hari libur")
else:
  print("Tidak ada perbedaan yang signifikan dalam rata-rata jumlah peminjaman sepeda antara hari kerja dan hari libur")


st.subheader('Korelasi antara Registered dan Casual Users')

fig, ax = plt.subplots()

ax.scatter(hour['registered'], hour['casual'], s=4)
ax.set_xlabel('Registered Users', fontsize=6)
ax.set_ylabel('Casual Users', fontsize=6)
ax.set_title('Data Hour',fontsize=7)

fig.set_size_inches(4, 3)
fig.tight_layout()

st.pyplot(fig)


figur, ax = plt.subplots()
ax.scatter(day['registered'], day['casual'], s=4, color='orange')
ax.set_xlabel('Registered Users', fontsize=6)
ax.set_ylabel('Casual Users', fontsize=6)
ax.set_title('Data Day',fontsize=7)

figur.set_size_inches(4, 3)
figur.tight_layout()

st.pyplot(figur)


with st.expander("Deskripsi"):
    st.write(
        """
        Terdapat korelasi positif antara jumlah pengguna registered dan casual, yang berarti semakin banyak pengguna registered, semakin banyak juga pengguna casual.
        
        Selain itu, dilakukan uji korelasi Pearson untuk melihat seberapa kuat korelasi antara kedua variabel tersebut.
        
        Dari hasil uji korelasi, terlihat bahwa korelasi antara jumlah pengguna registered dan casual adalah sebesar 0.51 didata hour dan 0.4 didata day, yang berarti ada korelasi positif yang cukup kuat antara kedua variabel tersebut.
        
        Artinya, semakin banyak pengguna yang terdaftar, semakin besar juga kemungkinan ada pengguna casual yang menggunakan layanan tersebut.
        
        Sementara itu, nilai p-value yang sangat kecil (0.00) menunjukkan bahwa hasil korelasi tersebut signifikan secara statistik, sehingga dapat dianggap sebagai bukti kuat bahwa terdapat hubungan antara kedua variabel tersebut.
        """
    )

corr, p_value = pearsonr(hour['registered'], hour['casual'])
print(f"Korelasi Pearson antara registered dan casual adalah {corr:.2f}, dengan p-value {p_value:.2f}")


corr, p_value = pearsonr(day['registered'], day['casual'])
print(f"Korelasi Pearson antara registered dan casual adalah {corr:.2f}, dengan p-value {p_value:.2f}")

st.caption('Copyright (c) Aninditya 2023')