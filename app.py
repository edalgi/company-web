import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title="Valerapp", page_icon="🤖", layout="wide")
email_contact = "edalgi@gmail.comk"  # Replace with your actual email address

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/main.css")

url="https://lottie.host/cab1e94d-0a8a-4a2a-894f-8e07506fa5a0/dqEpEcKMel.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottie(url)

#intro

with st.container():
    st.header("Hola, somos Valerapp 👋")
    st.title("Creamos soluciones para tu negocio")
    st.write("Somos una empresa de desarrollo de software que se especializa en la creación de aplicaciones web y móviles. Nuestro objetivo es ayudarte a llevar tu negocio al siguiente nivel con tecnología de vanguardia.")
    st.write("[Conoce más sobre nosotros](https://valerapp.com)")

#sobre nosotros
with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros 🔍")
        st.write("En Valerapp, nos apasiona la tecnología y la innovación. Nuestro equipo está formado por expertos en desarrollo de software, diseño de interfaces y marketing digital. Nos enorgullece ofrecer soluciones personalizadas para cada cliente, adaptadas a sus necesidades y presupuesto.")
        st.write("[Conoce más sobre nosotros](https://valerapp.com)")
    with animation_column:
        st_lottie(lottie,  height=400)

#nuestros servicios
with st.container():
    st.write("---")
    st.header("Nuestros servicios 🛠️")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open("imagenes/services.jpeg")
        st.image(image, caption="Nuestros servicios", use_column_width=True)
    with text_column:
        st.subheader("Desarrollo de aplicaciones web y móviles")
        st.write("""Diseñamos y desarrollamos aplicaciones web y móviles a medida, adaptadas a las necesidades de tu negocio.""")
        st.write("[Ver servicios](https://valerapp.com)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open("imagenes/consultoria.jpg")
        st.image(image, caption="Nuestros servicios", use_column_width=True)
    with text_column:
        st.subheader("Consultoria tecnológica")
        st.write("""Diseñamos y desarrollamos aplicaciones web y móviles a medida, adaptadas a las necesidades de tu negocio.""")
        st.write("[Ver servicios](https://valerapp.com)")   

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open("imagenes/automatizacion.jpg")
        st.image(image, caption="Nuestros servicios", use_column_width=True)
    with text_column:
        st.subheader("Automatización de procesos")
        st.write("""Diseñamos y desarrollamos aplicaciones web y móviles a medida, adaptadas a las necesidades de tu negocio.""")
        st.write("[Ver servicios](https://valerapp.com)")   

#contacto



with st.container():
    st.write("---")
    st.header("Contacto 📞")
    st.write("###")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea type="message" name="message" placeholder="Message" required></textarea>
        <input type="hidden" name="_captcha" value="false">
        <button type="submit">Enviar</button>
    </form>
    """
    left, right = st.columns(2)
    with left:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right:
        st.empty()