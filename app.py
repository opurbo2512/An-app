import streamlit as st
import json
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

menu = st.sidebar.selectbox("Select page:",["Home","My Projects","Admin"])
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #00172B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
if menu == "Home":
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

if menu == "My Projects":
    st.subheader("There are some projects of me.")
    with st.container():
        c7,c8 = st.columns(2)
        with c7:
            st.subheader("Death Calculator")
            st.markdown("Github:    https://github.com/opurbo2512/Death-Calculator.git")
            st.markdown("[Click here to visit](https://death-calculator.streamlit.app/)")
        with c8:
            img2 = Image.open("img.jpeg")
            st.image(img2,width=200)

if menu == "Admin":
    if "context" not in st.session_state:
        st.session_state.context = False

    k1 = "opurbo"
    k2 = "2B@ornot2B"

    if not st.session_state.context:
        st.subheader("This page is only for admin.")
        with st.container():
            st.write("Enter your name and password:")
            t1 = st.text_input("Name")
            t2 = st.text_input("Password")
        b3 = st.button("Submit")
        if b3:
            if t1==k1 and t2==k2:
                st.session_state.context = True
            else:
                st.error("Your given data is wrong.\nTry again")

    if st.session_state.context:
        st.write("Hello Opurbo.")
        st.write("She is gone.Focus on yourself")


    
