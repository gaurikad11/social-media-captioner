import streamlit as st
import os
import base64
from PIL import Image
from brain import get_image_description, get_instagram, get_twitter, get_linkedin
import pandas as pd

st.set_page_config(page_title="Social Media Captioner App",
                   page_icon="🧊",
                   layout="wide")


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
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

st.title(":blue[Social Media] Captioner")
st.caption(
    "Enter the details and get cool captions for your posts! :sunglasses:")

col1, col2 = st.columns(2)

# st.write(" ")
# st.write(" ")
# st.write(" ")
caption = ""
with col1:
    # st.subheader("", divider="gray")
    with st.form(key='my_form'):
        instructions = st.text_area("Describe what you want.")
        platform = st.radio("Platform:", ["Linkedin", "Instagram", "Twitter"])
        option = st.selectbox(
            "Tone",
            ("Cheerful", "Professional", "Sad", "Emotional", "Funny",
             "Sarcastic", "happy", "Energetic"),
            placeholder="Select tone of caption...",
        )

        uploaded_file = st.file_uploader("Choose an image...",
                                         type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button(label='Submit')
        if platform == "Linkedin":
            caption = get_linkedin(instructions, "")
        if platform == "Instagram":
            caption = get_instagram(instructions, "")
        if platform == "Twitter":
            caption = get_twitter(instructions, "")

    if uploaded_file is not None:
        save_path = os.path.join("uploads", uploaded_file.name)
        os.makedirs("uploads", exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        image = Image.open(save_path)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        st.write("Image path:", save_path)
        image_description = get_image_description(save_path)
        if platform == "Linkedin":
            caption = get_linkedin(instructions, image_description)
        if platform == "Instagram":
            caption = get_instagram(instructions, image_description)
        if platform == "Twitter":
            caption = get_twitter(instructions, image_description)
    else:
        st.write("Please upload an image file.")

with col2:
    st.subheader("Results:")
    if submit_button:

        caption = st.text_area("Edit your caption:", caption, height=500)
