import streamlit as st
from PIL import Image
import requests
from utils import resize_image
from claude_client import call_analyzer
from io import BytesIO


def call_starter(username):
    """username can be your hard-coded Minecraft name, or you could add a text input to capture this"""
    url = "http://localhost:5000/spawn_bot"  # This will have to change once deployed

    params = {"username": username}
    try:
        response = requests.get(url, params=params)  # Make the GET request
        if response.status_code == 200:
            data = response.json()
            st.session_state["api_data"] = (
                data  # Store the result in session state. This state will last while the tab is open
            )
            st.success("API call successful!")
        else:
            st.error(f"API call failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")


def main():
    st.title("Minecraft Image Builder")

    if st.button("Start Bot"):
        call_starter("AustinMinty")

    uploaded_img = st.file_uploader("Choose an image")

    if uploaded_img is not None:
        img_bytes = BytesIO(uploaded_img.read())
        img = Image.open(img_bytes)
        img = resize_image(img)

        # Display the uploaded image
        st.image(img, caption="Uploaded Image", use_container_width=True)

        # Convert the resized PIL image back to bytes for the API call
        resized_bytes = BytesIO()
        img.save(
            resized_bytes, format="WEBP"
        )  # WARNING: this will only work if the original image is a webp image. You may want to add some logic to handle different formats.
        resized_bytes.seek(0)

        json_str = call_analyzer(uploaded_img, resized_bytes)
        st.code(json_str, language="json")


if __name__ == "__main__":
    main()
