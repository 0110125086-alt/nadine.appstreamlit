import streamlit as st

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('menu',['luas persegi','luas segitiga','luas lingkaran'])
if menu == 'luas persegi':
    st.write('ini halaman untuk menghitung luas persegi')
    st.markdown(':red[luas persegi]')
    st.image('https://tse1.mm.bing.net/th/id/OIP.tb5ldcpW9pqz82ERPhkvDwAAAA?w=180&h=181&c=7&r=0&o=7&cb=ucfimg2&dpr=1.5&pid=1.7&rm=3&ucfimg=1', caption='gambar persegi')
    sisi = st.number_input('silahkan masukkan sisi', min_value=0, )
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')

if menu == 'luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')
    

if menu == 'luas lingkaran':
    st.write('ini halaman untuk menghitung luas lingkaran')