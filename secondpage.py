import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

st.subheader('TOKOPEDIA')
st.write("""Sekitar 91 juta data pengguna Tokopedia dan lebih dari 7 juta data merchant Tokopedia mengalami peretasan pada bulan Maret 2020.
 Adapun kronologi lengkap bobolnya akun Tokopedia tersebut bermula saat peretas Whysodank pertama kali 
 mempublikasikan hasil peretasan di Raid Forum pada Sabtu (2/5). Di situs itu, Whysodank menggunakan nama akun ShinyHunters. 
 Keesokan harinya di hari Minggu (3/5) Whysodank mengumumkan telah menjual seluruh 91 juta data pengguna Tokopedia di forum darkweb 
 bernama EmpireMarket. Adapun harga jualnya sebesar US$ 5.000 atau sekitar Rp 74,5 juta. 
 Email, nama, dan kata sandi adalah jenis data yang mengalami peretasan.""")
