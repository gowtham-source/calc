import streamlit as st
import calc as c
from PIL import Image

import base64


@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("tttf.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 130%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""


st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("Basic calculator app:")

no1 = st.text_input("Enter no1")
no2 = st.text_input("Enter no2")


option = st.selectbox(
    'What operation should be followed',
    ('add', 'sub', 'mul', 'div'))

if no2:
    try:
        a = int(no1)
        b = int(no2)
    except ValueError as e:
        pass

if st.button("Calculate"):

    try:
        if option == "add":
            st.write("#### Addition of two no.s ", str(c.add(a, b)))
        if option == "sub":
            st.write("#### Subraction of two no.s ", str(c.sub(a, b)))
        if option == "mul":
            st.write("#### mul of two no.s ", str(c.mul(a, b)))
        if option == "div":
            x = c.div(a, b)
            st.write("#### div of two no.s ", str(c.div(a, b)))

    except NameError as e:
        st.write("#### Pls enter any no.")
