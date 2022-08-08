from Crypto.PublicKey import RSA
import streamlit as st
from Crypto import Random
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import requests
from streamlit_lottie import st_lottie

def app():
    st.title("Kriptografi")
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
         return None
        return r.json()

    lottie_url = "https://assets1.lottiefiles.com/packages/lf20_3yNFWP.json"
    lottie_json = load_lottieurl(lottie_url)
    col2,col1=st.columns((1,1))
    with col2:
        st_lottie(lottie_json, height=200, key="mail")
    with col1:
         st.markdown('<div style="text-align: justify;">Kriptografi adalah proses menyembunyikan informasi dengan cara mengkonversi data yang dapat dibaca, kedalam data yang tidak bisa dibaca menggunakan sejumlah kunci (key) atau algoritma enkripsi.Apa saja yang bisa kita enkripsi? Informasi yang dapat kita enkripsi menggunakan kriptografi meliputi email, gambar, video, file dan data sensitif lainnya.Tujuan dari kriptografi adalah untuk memastikan informasi yang terenkripsi selalu tetap rahasia, integritas, otentikasi dan asli tidak terbantahkan (non-repudiation</div>', unsafe_allow_html=True)
        
    
    st.subheader("DES")
    st.write("""DES Data Encryption Standard adalah standar enkripsi data menggunakan algoritma symmetric encryption.Pada algoritma ini, 
    kunci (key) hanya memiliki ukuran blok data tetap sebesar 8 byte. 
    Tetapi, Secret Key yang digunakan untuk enkripsi dan dekripsi ada 64 byte. 56 byte digenerate secara random, dan 8 byte digunakan untuk error checking""")
    st.code("""
    key = b'1n1kunC1' 
    BLOCK_SIZE = 32 
    data = st.text_input('Input Text')
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(data.encode(), BLOCK_SIZE)
    encrypted_text = des.encrypt(padded_text)
    decrypted_text = des.decrypt(encrypted_text)
    hsl_enkripsi, hsl_deskripsi =st.columns((1,1))
    with hsl_enkripsi:
        if st.button('enkripsi'):
            st.write("text:", data)
            st.write("hasil enkripsi:", encrypted_text)
    with hsl_deskripsi:
        if st.button('deskripsi'):
            st.write("teks enkripsi:", encrypted_text )
            st.write("hasil deskripsi:", decrypted_text.decode('utf-8'))""")
    st.write("Expect Output")
    st.code("""
    text: halo
    hasil enkripsi: b'\xeb|\x85=\xda\x81\xc1\xd66\xf6\xe2m\xf5z\xb7\xe26\xf6\xe2m\xf5z\xb7\xe26\xf6\xe2m\xf5z\xb7\xe2'
    """)
    #code
    st.write("Test ALgoritma DES")
    key = b'1n1kunC1' 
    BLOCK_SIZE = 32 
    data = st.text_input('Input Text')
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(data.encode(), BLOCK_SIZE)
    encrypted_text = des.encrypt(padded_text)
    decrypted_text = des.decrypt(encrypted_text)
    hsl_enkripsi, hsl_deskripsi =st.columns((1,1))
    with hsl_enkripsi:
        if st.button('enkripsi'):
            st.write("text:", data)
            st.write("hasil enkripsi:", encrypted_text)
    with hsl_deskripsi:
        if st.button('deskripsi'):
            st.write("teks enkripsi:", encrypted_text )
            st.write("hasil deskripsi:", decrypted_text.decode('utf-8'))

    st.subheader("AES")
    st.write("""AES atau Advanced Encryption Standard adalah algoritma symmetric-key yang melakukan operasi yang sama setiap kali.
    Memiliki block tetap sejumlah 128 byte, yang nantinya akan menjadi tiga kunci yang masing - masing memiliki panjang 128, 192 dan 256 byte.
    AES dikenal cukup cepat dan aman, serta secara defacto diakui sebagai standar algoritma enkripsi simetris""")

    st.code("""
    data2 = st.text_input('Input Text AES')
    key = b'1n1kuNc1k174h3h3' # 16 block size

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data2.encode())
    

    hsl_enkripsi2, hsl_deskripsi2 =st.columns((1,1))

    with hsl_enkripsi2:
        if st.button('RES'):
            st.write(" nonce : ", nonce)
            st.write(" tag : ", tag)
            st.write(" enkripsi : ", ciphertext)
    with hsl_deskripsi2:
        if st.button('DESC RES'):
            key = b'1n1kuNc1k174h3h3' # 16 block size
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            data2 = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                st.write(data2.decode())
            except ValueError:
                st.write("Kunci salah atau data korup!")""")
    st.write("Expect Output")
    st.code("""
    text:hai
    nonce : b'\x1c(\xc0\xe6\x8e\x07>.$#\\\xa9\x19\xe8,I'
    tag : b'\x8f\x14U\xa9S?k\xebs \x9f\x12u\x0c4%'
    enkripsi : b'\xb8\xe4\x14'""")

    st.write("Test ALgoritma AES")
    data2 = st.text_input('Input Text AES')
    key = b'1n1kuNc1k174h3h3' # 16 block size

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data2.encode())
    

    hsl_enkripsi2, hsl_deskripsi2 =st.columns((1,1))

    with hsl_enkripsi2:
        if st.button('ENKRIPSI RES'):
            st.write(" nonce : ", nonce)
            st.write(" tag : ", tag)
            st.write(" enkripsi : ", ciphertext)
    with hsl_deskripsi2:
        if st.button('DESC RES'):
            key = b'1n1kuNc1k174h3h3' # 16 block size
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            data2 = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                st.write(data2.decode())
            except ValueError:
                st.write("Kunci salah atau data korup!")
            