import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


def app():

    st.title('Bagaimana Data Breach Terjadi')

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
         return None
        return r.json()

    lottie_url = "https://assets1.lottiefiles.com/packages/lf20_zdtukd5q.json"
    lottie_json = load_lottieurl(lottie_url)

    contact_icon, contact_link = st.columns((1, 1))
    with contact_icon:
        st_lottie(lottie_json, height=200, key="mail")
    with contact_link:
        st.markdown('<div style="text-align: justify;">E-commerce menjadi salah satu ladang pembobolan paling laris di Indonesia. Pembobolan data di Indonesia kian marak terjadi, khususnya pada e-commerce. Berikut contoh e-commerce yang pernah mengalami pembobolan data di Indonesia</div>', unsafe_allow_html=True)
   

   
    st.subheader('Lalu, Bagaimana Data Breach Bisa Terjadi?')
    st.write(""" 
    1. Pishing
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

   