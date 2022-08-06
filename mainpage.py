import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected


st.title("Kasus Pembobolan Data Pelanggan Pada E-Commerce di Indonesia")

st.caption("Tugas Kelompok WIT oleh Luh Intan Ratna Sari Dewi, Inggit Putri Naria, Salsabila Rahmah, 5 Agustus 2022")

st.write(""" Data breach adalah kasus serangan cyber, suatu kondisi ketika hacker mampu menyusup masuk ke dalam sistem dan mengekstraksi data-data penting di dalamnya. 
Pengertian lain, dilansir Norton, data breach adalah insiden keamanan ketika suatu data pribadi pengguna device telah diakses tanpa adanya otorisasi. 
Jenis pembobolan dan pencurian data ini dapat merugikan bisnis atau konsumen dengan berbagai cara.

Hal ini dianggap sebagai tindakan kriminal yang dapat merusak reputasi pribadi maupun perusahaan. Memang, mengembalikan data yang hilang bisa saja dilakukan, 
tapi reputasi yang tercoreng karena tersebarnya data pribadi tidak akan pulih. Dampaknya, mulai dari tercurinya data-data sensitif sampai hilangnya kepercayaan pelanggan.

Secara teknis, data breach mirip dengan security breach atau pelanggaran keamanan, tapi berbeda tujuan. Security breach hanyalah pembobolan, 
sedangkan data breach adalah aktivitas mencuri informasi. Perlu digaris bawahi, data breach berbeda dengan data leakage (kebocoran data). 
Data breach terjadi karena unsur kesengajaan yang dilakukan oleh oknum tidak bertanggung jawab, sementara data leakage terjadi karena data security yang buruk.""")

st.subheader('Apa Dampak Data Breach?')
st.write("""Aktivitas pencurian data ini tentunya akan mengancam data privasi pengguna. 
Di mana, data profiling bisa saja digunakan oleh pihak tidak bertanggung jawab untuk melakukan kejahatan cyber 
seperti blast sms penipuan, peretasan nomor WhatsApp, praktik phising dan sejenisnya.""")

st.subheader('Apa Saja Sih, Kasus Pembobolan Data yang Pernah Terjadi di Indonesia?')
st.write("""Pembobolan data di Indonesia kian marak terjadi, khususnya pada e-commerce. 
Berikut contoh e-commerce yang pernah mengalami pembobolan data di Indonesia:""")

st.subheader('TOKOPEDIA')
st.write("""Sekitar 91 juta data pengguna Tokopedia dan lebih dari 7 juta data merchant Tokopedia mengalami peretasan pada bulan Maret 2020.
 Adapun kronologi lengkap bobolnya akun Tokopedia tersebut bermula saat peretas Whysodank pertama kali 
 mempublikasikan hasil peretasan di Raid Forum pada Sabtu (2/5). Di situs itu, Whysodank menggunakan nama akun ShinyHunters. 
 Keesokan harinya di hari Minggu (3/5) Whysodank mengumumkan telah menjual seluruh 91 juta data pengguna Tokopedia di forum darkweb 
 bernama EmpireMarket. Adapun harga jualnya sebesar US$ 5.000 atau sekitar Rp 74,5 juta. 
 Email, nama, dan kata sandi adalah jenis data yang mengalami peretasan.""")


st.subheader('BUKALAPAK')
st.write("""Seorang hacker yang memakai username "Startexmislead" mengaku punya sekitar 13 juta data pengguna Bukalapak. 
Pengumuman ini ia publikasi pada Senin, 4 Mei 2020, di Raid Forums. Data yang ditampilkan mulai dari email, nama pengguna,
password, salt, last login, email Facebook dengan hash, alamat pengguna, tanggal ulang tahun, hingga nomor telepon.

Menanggapi kabar itu, Bukalapak mengatakan tidak ada data baru penggunanya yang diretas dan dijual di forum hacker. 
Sementara 13 juta data akun yang dijual "Startexmislead" itu merupakan percobaan peretasan yang pernah terjadi pada Maret 2019 yang  berisi data Bukalapak tahun 2015-2017.

Diketahui pada Maret 2019, data 13 juta pelanggan Bukalapak dilaporkan dicuri oleh hacker asal Pakistan bernama Gnosticplayers. 
Sang hacker mengaku menjual jutaan akun tersebut di situs Dream Market.""")

st.subheader('BHINEKA')
st.write("""Sekelompok peretas dengan nama ShinyHunters mengklaim memiliki data pengguna dari 10 perusahaan digital. 
Total data pengguna yang dihimpun mencapai 73,2 juta, di mana 1,2 juta di antaranya disebut merupakan data pengguna dari Bhinneka.com.

Data berjumlah banyak tersebut dijual di situs pasar gelap internet untuk produk-produk ilegal di dark web, dengan harga 18.000 dollar AS atau Rp 266 juta untuk keseluruhan database pengguna yang berumlah 73,2 juta. 1,2 juta pelanggan Bhinneka.com yang bocor dijual di forum peretasan online.

Bhinneka mengatakan password pengguna telah dilindungi dengan enkripsi. Dipastikan juga tidak ada data kartu pembayaran yang disimpan di server mereka. 
Namun, tidak ada penjelasan data apa saja yang mungkin telah dicuri oleh peretas.""")

st.subheader('Lalu, Bagaimana Data Breach Bisa Terjadi?')
st.write(""" 1. Phishing
Phising adalah suatu serangan dengan cara memanipulasi psikologis, agar bisa mengelabui si pengguna, sehingga mereka akan menyerahkan data-data pribadinya.
Pelaku akan mengelabui korban dengan mengaku sebagai pihak yang berwenang dan memberikan penawaran yang menggiurkan kepada korbannya. Ada berbagai jenis phishing, misalnya dari email, SMS, telepon, chat, dan sebagainya.

2. Brute Force Attack
Metode ini merupakan metode peretasan menggunakan cara trial and error untuk memecahkan kata sandi, kredensial login, maupun kunci enkripsi.
Jika kamu menggunakan password yang mudah ditebak, ini akan menjadi celah yang gampang dimasuki oleh peretas dalam menjalankan aksinya.

3. Penyusupan Malware
Para hacker atau pelaku kejahatan akan memasukkan malware ke dalam device korbannya agar pencurian data bisa terjadi.
Semua perangkat yang kita gunakan terhubung dengan sistem operasi, software, dan jaringan yang memiliki celah keamanan. Celah ini yang dimanfaatkan hacker untuk menyusupi malware untuk merusak sistem dan mengambil informasi penting.

4.  Spyware

Spyware merupakan salah satu jenis malware yang di-install ke suatu perangkat secara diam-diam untuk mencuri data pribadi yang ada di dalamnya.
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






