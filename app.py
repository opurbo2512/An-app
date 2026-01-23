import streamlit as st
import json
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

#load photo   
img = Image.open("image.jpg")
image_lottie = Image.open("image.jpg")

#Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style.css")

#Header Section
with st.container():
    st.subheader("Hi, I am Opurbo :wave:")
    st.title("An Materials Engineer from Bangladesh")
    st.write("A student passionate about learning technology and materials science")

#What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            - A student passionate about learning technology and materials science
            - Studying MME(Materials and Mettalugical Engineering)
            - My university is BUET(Bangladesh University of Engineering and Technology)
            """
        )
    with right_column:
        lottie_anim = load_lottiefile("coding.json")
        st_lottie(lottie_anim,speed=1,loop=True,height=300)

#Doing
with st.container():
    st.write("---")
    image_column,text_column =st.columns((1,2))
    with image_column:
        st.image(image_lottie)
    with text_column:
        st.header("What I am learning")
        st.markdown("""
        - Materials Science and Engineering
        - Python
        - Machine Learning
        - Streamlit
        """)

with st.container():
    st.write("---")
    st.header("If you want to send a message to me")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/opurbo2512@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
