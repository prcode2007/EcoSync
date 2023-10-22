import streamlit as st
from PIL import Image

image1 = Image.open("EcoSync_title_logo.png")
st.set_page_config(page_icon="image1",page_title = "EcoSync")

_,col2,_= st.columns([1,4,1])
with col2:
    st.title("Welcome to :green[EcoSync]")

image2 = Image.open("EcoSync_logo.png")
st.image(image2)


st.write("EcoSync is a public website that works towards\
         developing a community in the name of sustainability.\
        Participate in the many activities that support the environment\
        and become a better citizen today with EcoSync.")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.header(":green[Try these activities on our website:]",divider = "green")
st.subheader("🍃 Carbon footprint calculator:")
st.write("Find how much you contribute in favour of greenhouse gasses!")
st.subheader("🍃 Sustainable events:")
st.write("Boost your involvement ecofriendly events.")
st.subheader("🍃 Eco-Friendly Products:")
st.write("Your list  of everyday items to aid the environment.")
st.subheader("🍃 Leftover food:")
st.write("Check out some restaurants near your area that give out leftover food.")




