import streamlit as st
from model import predict_caption
from PIL import Image

st.set_page_config(
    page_title="Image Captioning AI",
    page_icon="🖼️"
)

st.title("🖼️ AI Image Captioning")

st.write(
    "Upload an image and let AI describe it."
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image,
             caption="Uploaded Image",
             use_container_width=True)

    with open("temp.jpg","wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Generate Caption"):

        with st.spinner("Generating Caption..."):

            caption = predict_caption("temp.jpg")

        st.success("Caption Generated!")

        st.write("### Caption")

        st.info(caption)

        st.balloons()