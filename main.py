import streamlit as st
from PIL import Image


def main():
    st.title("Minecraft Image Builder")

    uploaded_img = st.file_uploader("Choose an image")

    if uploaded_img is not None:
        img = Image.open(uploaded_img)

        # Display the uploaded image
        st.image(img, caption="Uploaded Image", use_container_width=True)


if __name__ == "__main__":
    main()
