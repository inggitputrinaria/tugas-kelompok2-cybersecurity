import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
# import pandas as pd
# import numpy as np

# with st.sidebar:
#     selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

def app():
    st.title("Kasus Pembobolan Data Pelanggan Pada E-Commerce di Indonesia")
    st.caption("Tugas Kelompok WIT oleh Luh Intan Ratna Sari Dewi, Inggit Putri Naria, Salsabila Rahmah, 5 Agustus 2022")

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
         return None
        return r.json()

    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_gxcnsfk2.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json)

    # image=Image.open('databreaches.jpg')
    # st.image(image, caption=None,  use_column_width=None, clamp=False, channels="RGB")
    st.write(""" Data breach adalah kasus serangan cyber, suatu kondisi ketika hacker mampu menyusup masuk ke dalam sistem dan mengekstraksi data-data penting di dalamnya. 
    Pengertian lain, dilansir Norton, data breach adalah insiden keamanan ketika suatu data pribadi pengguna device telah diakses tanpa adanya otorisasi. 
    Jenis pembobolan dan pencurian data ini dapat merugikan bisnis atau konsumen dengan berbagai cara.

    Hal ini dianggap sebagai tindakan kriminal yang dapat merusak reputasi pribadi maupun perusahaan. Memang, mengembalikan data yang hilang bisa saja dilakukan, 
    tapi reputasi yang tercoreng karena tersebarnya data pribadi tidak akan pulih. Dampaknya, mulai dari tercurinya data-data sensitif sampai hilangnya kepercayaan pelanggan.""")
    
    with st.expander("Tonton Video Berikut"):
     st.write("""
         Merupakan video mengenai pengenalan Cyber Security
     """)
     st.video("https://www.youtube.com/watch?v=0kK902-ZvNM")
    
    st.write("""Secara teknis, data breach mirip dengan security breach atau pelanggaran keamanan, tapi berbeda tujuan. Security breach hanyalah pembobolan, 
    sedangkan data breach adalah aktivitas mencuri informasi. Perlu digaris bawahi, data breach berbeda dengan data leakage (kebocoran data). 
    Data breach terjadi karena unsur kesengajaan yang dilakukan oleh oknum tidak bertanggung jawab, sementara data leakage terjadi karena data security yang buruk.""")
 
    st.subheader('Apa Dampak Data Breach?')
    st.write("""Aktivitas pencurian data ini tentunya akan mengancam data privasi pengguna. 
    Di mana, data profiling bisa saja digunakan oleh pihak tidak bertanggung jawab untuk melakukan kejahatan cyber 
    seperti blast sms penipuan, peretasan nomor WhatsApp, praktik phising dan sejenisnya.""")

   

    # st.subheader('Apa Saja Sih, Kasus Pembobolan Data yang Pernah Terjadi di Indonesia?')
    # st.write("""Pembobolan data di Indonesia kian marak terjadi, khususnya pada e-commerce. 
    # Berikut contoh e-commerce yang pernah mengalami pembobolan data di Indonesia:""")

    # st.subheader('TOKOPEDIA')
    # st.write("""Sekitar 91 juta data pengguna Tokopedia dan lebih dari 7 juta data merchant Tokopedia mengalami peretasan pada bulan Maret 2020.
    # Adapun kronologi lengkap bobolnya akun Tokopedia tersebut bermula saat peretas Whysodank pertama kali 
    # mempublikasikan hasil peretasan di Raid Forum pada Sabtu (2/5). Di situs itu, Whysodank menggunakan nama akun ShinyHunters. 
    # Keesokan harinya di hari Minggu (3/5) Whysodank mengumumkan telah menjual seluruh 91 juta data pengguna Tokopedia di forum darkweb 
    # bernama EmpireMarket. Adapun harga jualnya sebesar US$ 5.000 atau sekitar Rp 74,5 juta. 
    # Email, nama, dan kata sandi adalah jenis data yang mengalami peretasan.""")

    # chart_data = pd.DataFrame(
    #  chart=['23,7%','67,4%', '8,9%'],
    #  columns=['bukapalak', 'tokopedia', 'lazada'])
    # st.area_chart(chart_data)







