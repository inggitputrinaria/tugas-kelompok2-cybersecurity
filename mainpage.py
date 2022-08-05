import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected



st.title("Kasus Kebocoran Data Pada E-Commerce di Indonesia")

st.caption("Ditulis oleh Luh Intan Ratna Sari Dewi, Inggit Putri Naria, Salsabila Rahmah, 5 Agustus 2022")

st.write("""Kebocoran data dapat didefinisikan dengan transmisi data yang tidak sah dari dalam suatu organisasi kepada tujuan atau penerima eksternal. 
Istilah ini dapat digunakan untuk menggambarkan data yang ditransfer secara elektronik atau fisik. Ancaman kebocoran data biasanya terjadi melalui 
web dan email, tetapi dapat juga terjadi melalui perangkat penyimpanan data seluler seperti media optik, kunci USB, dan 
laptop. 

Pelanggaran data selalu menjadi berita utama dan hal yang sering terjadi di kehidupan sehari-hari.
Kebocoran data, merupakan masalah besar bagi keamanan data, dan kerusakan yang ditimbulkannya pada organisasi mana pun 
akan menjadi kasus yang serius, terlepas dari ukuran atau industrinya. Mulai dari pendapatan yang menurun hingga reputasi 
yang rusak atau hukuman finansial yang besar hingga tuntutan hukum. Ini adalah ancaman yang harus dilindungi oleh organisasi mana pun.
""")




st.subheader('TOKOPEDIA')
st.write("""Sekitar 91 juta data pengguna Tokopedia dan lebih dari 7 juta data merchant Tokopedia mengalami peretasan pada bulan Maret 2020.
 Adapun kronologi lengkap bobolnya akun Tokopedia tersebut bermula saat peretas Whysodank pertama kali 
 mempublikasikan hasil peretasan di Raid Forum pada Sabtu (2/5). Di situs itu, Whysodank menggunakan nama akun ShinyHunters. 
 Keesokan harinya di hari Minggu (3/5) Whysodank mengumumkan telah menjual seluruh 91 juta data pengguna Tokopedia di forum darkweb 
 bernama EmpireMarket. Adapun harga jualnya sebesar US$ 5.000 atau sekitar Rp 74,5 juta. 
 Email, nama, dan kata sandi adalah jenis data yang mengalami peretasan.""")




st.subheader('BUKALAPAK')
st.write("""Sekitar 91 juta data pengguna Tokopedia dan lebih dari 7 juta data merchant Tokopedia mengalami peretasan pada bulan Maret 2020.
 Adapun kronologi lengkap bobolnya akun Tokopedia tersebut bermula saat peretas Whysodank pertama kali 
 mempublikasikan hasil peretasan di Raid Forum pada Sabtu (2/5). Di situs itu, Whysodank menggunakan nama akun ShinyHunters. 
 Keesokan harinya di hari Minggu (3/5) Whysodank mengumumkan telah menjual seluruh 91 juta data pengguna Tokopedia di forum darkweb 
 bernama EmpireMarket. Adapun harga jualnya sebesar US$ 5.000 atau sekitar Rp 74,5 juta. 
 Email, nama, dan kata sandi adalah jenis data yang mengalami peretasan.""")
