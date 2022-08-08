import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# with st.sidebar:
#     selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected
def app():
    st.title('Apa Saja Sih, Kasus Pembobolan Data yang Pernah Terjadi di Indonesia?')
    st.caption("")
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
         return None
        return r.json()

    lottie_url = "https://assets1.lottiefiles.com/packages/lf20_5tl1xxnz.json"
    lottie_json = load_lottieurl(lottie_url)

    contact_icon, contact_link = st.columns((1, 1))
    with contact_icon:
        st_lottie(lottie_json, height=200, key="mail")
    with contact_link:
        st.markdown('<div style="text-align: justify;">E-commerce menjadi salah satu ladang pembobolan paling laris di Indonesia. Pembobolan data di Indonesia kian marak terjadi, khususnya pada e-commerce. Berikut contoh e-commerce yang pernah mengalami pembobolan data di Indonesia</div>', unsafe_allow_html=True)
   
    st.subheader('TOKOPEDIA')
    words, icons = st.columns((1, 0.5))
    with words:
        st.write("""Sekitar 91 juta data pengguna Tokopedia dan lebih dari 7 juta data merchant Tokopedia mengalami peretasan pada bulan Maret 2020.
    Adapun kronologi lengkap bobolnya akun Tokopedia tersebut bermula saat peretas Whysodank pertama kali 
    mempublikasikan hasil peretasan di Raid Forum pada Sabtu (2/5). Di situs itu, Whysodank menggunakan nama akun ShinyHunters. 
    Keesokan harinya di hari Minggu (3/5) Whysodank mengumumkan telah menjual seluruh 91 juta data pengguna Tokopedia di forum darkweb 
    bernama EmpireMarket. Adapun harga jualnya sebesar US$ 5.000 atau sekitar Rp 74,5 juta. 
    Email, nama, dan kata sandi adalah jenis data yang mengalami peretasan.""")
    with icons:
        image=Image.open('tokopedia.jpg')
        st.image(image)

    st.subheader('BUKALAPAK')

    icons2, words2=st.columns(( 0.5, 1))
    with icons2:
        image2=Image.open('bukalapak.png')
        st.image(image2)
    with words2:
        st.write("""Seorang hacker yang memakai username "Startexmislead" mengaku punya sekitar 13 juta data pengguna Bukalapak. 
    Pengumuman ini ia publikasi pada Senin, 4 Mei 2020, di Raid Forums. Data yang ditampilkan mulai dari email, nama pengguna,
    password, salt, last login, email Facebook dengan hash, alamat pengguna, tanggal ulang tahun, hingga nomor telepon.
    Menanggapi kabar itu, Bukalapak mengatakan tidak ada data baru penggunanya yang diretas dan dijual di forum hacker. 
    """)
# Sementara 13 juta data akun yang dijual "Startexmislead" itu merupakan percobaan peretasan yang pernah terjadi pada Maret 2019 yang  berisi data Bukalapak tahun 2015-2017.
#     Diketahui pada Maret 2019, data 13 juta pelanggan Bukalapak dilaporkan dicuri oleh hacker asal Pakistan bernama Gnosticplayers. 
#     Sang hacker mengaku menjual jutaan akun tersebut di situs Dream Market.
    st.subheader('BHINNEKA')
    words3, icons3= st.columns((1, 0.5))
    with words3:
        st.write("""Sekelompok peretas dengan nama ShinyHunters mengklaim memiliki data pengguna dari 10 perusahaan digital. 
    Total data pengguna yang dihimpun mencapai 73,2 juta, di mana 1,2 juta di antaranya disebut merupakan data pengguna dari Bhinneka.com. Data berjumlah banyak tersebut dijual di situs pasar gelap internet untuk produk-produk ilegal di dark web, dengan harga 18.000 dollar AS atau Rp 266 juta untuk keseluruhan database pengguna yang berumlah 73,2 juta. 1,2 juta pelanggan Bhinneka.com yang bocor dijual di forum peretasan online.
    Bhinneka mengatakan password pengguna telah dilindungi dengan enkripsi. Dipastikan juga tidak ada data kartu pembayaran yang disimpan di server mereka. 
    Namun, tidak ada penjelasan data apa saja yang mungkin telah dicuri oleh peretas.""")

    with icons3:
        image3=Image.open('bhinneka.png')
        st.image(image3)
