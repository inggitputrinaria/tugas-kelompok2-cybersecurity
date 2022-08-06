import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

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
