import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

st.subheader('Lalu, Bagaimana Data Breach Bisa Terjadi?')
st.write(""" 1. Pshing
Phising adalah suatu serangan dengan cara memanipulasi psikologis, agar bisa mengelabui si pengguna, sehingga mereka akan menyerahkan data-data pribadinya.
Pelaku akan mengelabui korban dengan mengaku sebagai pihak yang berwenang dan memberikan penawaran yang menggiurkan kepada korbannya. Ada berbagai jenis phishing, misalnya dari email, SMS, telepon, chat, dan sebagainya.

2. Brute Force Attack
Metode ini merupakan metode peretasan menggunakan cara trial and error untuk memecahkan kata sandi, kredensial login, maupun kunci enkripsi.
Jika kamu menggunakan password yang mudah ditebak, ini akan menjadi celah yang gampang dimasuki oleh peretas dalam menjalankan aksinya.

3. Penyusupan Malware
Para hacker atau pelaku kejahatan akan memasukkan malware ke dalam device korbannya agar pencurian data bisa terjadi.
Semua perangkat yang kita gunakan terhubung dengan sistem operasi, software, dan jaringan yang memiliki celah keamanan. Celah ini yang dimanfaatkan hacker untuk menyusupi malware untuk merusak sistem dan mengambil informasi penting.

4.  Spyware

Spyware merupakan salah satu jenis malware yang di-instal ke suatu perangkat secara diam-diam untuk mencuri data pribadi yang ada di dalamnya.
Jika sudah terinfeksi spyware, maka segala aktivitas yang dilakukan oleh perangkat tersebut akan dimata-matai. Mulai dari aktivitas internet, kredensial login, hingga mengakses data sensitif. Dengan begitu password login, nomor kartu kredit, informasi perbankan dan data penting lainnya dapat diketahui pelaku.

5. Hilangnya Device
Kehilangan device juga bisa jadi penyebab seseorang mengalami data breach. Laptop atau hard drive eksternal yang tidak terenkripsi dan tidak dikunci akan 
sangat rentan terhadap hilangnya informasi penting di dalamnya.""")

st.subheader('Cara Mengatasi Data Breach')
st.write(""" 1. Segera isolasi sistem yang diserang
Jika mengalami pelanggaran data, lakukan isolasi sistem untuk membatasi akses ke data-data berharga. Sebaiknya langkah ini segera dilakukan agar hacker tidak dapat mengakses dan merusak sistem lebih lanjut. Setelah itu gunakan infrastruktur keamanan yang lebih tinggi agar serangan tidak terjadi secara berulang.

2. Update security software
Melakukan update security software secara berkala penting dilakukan demi meningkatkan keamanan data. Pastikan memilih software keamanan tingkat tinggi yang sudah dilengkapi dengan antivirus dan perlindungan dari berbagai jenis malware.

3. Enkripsi
Enkripsi bekerja dengan cara mengacak data menjadi tidak dapat dipahami oleh orang lain. Secara teknis, enkripsi berarti proses mengubah plaintext–teks yang bisa dipahami manusia–, menjadi ciphertext yang tidak bisa dipahami. Hal ini tentunya bertujuan untuk menjaga privasi pengguna data. Dengan data yang terenkripsi, masalah kebocoran privasi juga dapat dicegah dengan lebih baik.

4. Melakukan backup data
Backup data dengan rutin adalah salah satu tindakan yang penting dilakukan untuk pencegahan serangan pelanggaran data. Lakukan pembersihan data yang sudah tidak diperlukan secara menyeluruh. Buat instalasi baru di sistem operasi untuk menghapus drive.

5. Gunakan password yang kuat
Seperti yang kamu ketahui, salah satu metode pelanggaran data yaitu melalui brute force attack atau peretasan dengan mencoba memecahkan password dan kredensial login. Maka itu, gunakanlah kombinasi kata sandi yang kuat untuk mencegah terjadinya pelanggaran data dan  lakukan penggantian kata sandi tersebut secara berkala.


Barangkali terlihat sepele, cyber attack ini telah merugikan ribuan hingga jutaan orang dan perusahaan tiap tahunnya. 
Tugas kita sebagai pengguna device untuk berhati-hati dan teliti ketika sedang melakukan aktivitas di internet.
 
Data breach bisa membawa berbagai dampak negatif untuk bisnis, mulai dari tercurinya data-data sensitif sampai hilangnya kepercayaan pelanggan. 
Untuk menghindarinya, Anda perlu mencegahnya dengan poin-poin yang sudah disebutkan di atas.""")
