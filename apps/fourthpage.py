import streamlit as st
import requests
from streamlit_lottie import st_lottie




def app():
    st.title('Mengatasi Data Breach')
    # with st.sidebar:
    #     selected = option_menu("Halaman Utama", ["Second Page", 'Third Page'], 
    #         icons=['house', 'gear'], menu_icon="cast", default_index=1)
    #     selected
    # image=Image.open('gambar1.gif', "rb")
    
    # contents = image.read()
    # data_url = base64.b64encode(contents).decode("utf-8")
    # image.close()

    # st.markdown(
    #     f'<img src="data:image/gif;base64,{data_url}" alt="temp gif">',
    #     unsafe_allow_html=True,
    # )
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
   
    con_user, con_mark=st.columns((1,1))
    with con_user:
        st.subheader("Penanggulangan dari sisi Pengguna")
        tab1,tab2, tab3=st.tabs(["Update Software", "Backup", "Password"])
        with tab1:
            st.write(""" 
            Melakukan update security software secara berkala penting dilakukan demi meningkatkan keamanan data. Pastikan memilih software keamanan tingkat
             tinggi yang sudah dilengkapi dengan antivirus dan perlindungan dari berbagai jenis malware.""")
        with tab2:
             st.write(""" 
            Backup data dengan rutin adalah salah satu tindakan yang penting dilakukan untuk 
            pencegahan serangan pelanggaran data. Lakukan pembersihan data yang sudah tidak diperlukan secara menyeluruh. 
            Buat instalasi baru di sistem operasi untuk menghapus drive.""")
        with tab3:
            st.write("""Seperti yang kamu ketahui, salah satu metode pelanggaran data yaitu
             melalui brute force attack atau peretasan dengan mencoba memecahkan password dan kredensial login. 
             Maka itu, gunakanlah kombinasi kata sandi yang kuat untuk mencegah terjadinya pelanggaran data dan 
             lakukan penggantian kata sandi tersebut secara berkala
            """)
    with con_mark:
        st.subheader("Penanggulangan dari sisi E-Commerce")
        tab3, tab4 =st.tabs(["Isolasi Sistem", "Enkripsi"])
      
        with tab3:
            st.write(""" 
            Segera isolasi sistem yang diserang. Jika mengalami pelanggaran data, lakukan isolasi sistem untuk membatasi akses ke data-data berharga. 
            Sebaiknya langkah ini segera dilakukan agar hacker tidak dapat mengakses dan merusak sistem lebih lanjut.
            Setelah itu gunakan infrastruktur keamanan yang lebih tinggi agar serangan tidak terjadi secara berulang.""")
        with tab4:
             st.write(""" 
            Enkripsi bekerja dengan cara mengacak data menjadi tidak dapat dipahami oleh orang lain. 
            Secara teknis, enkripsi berarti proses mengubah plaintext–teks yang bisa dipahami manusia–, menjadi ciphertext yang tidak bisa dipahami. Hal ini tentunya bertujuan untuk menjaga privasi pengguna data. Dengan data yang terenkripsi, 
            masalah kebocoran privasi juga dapat dicegah dengan lebih baik.""")

