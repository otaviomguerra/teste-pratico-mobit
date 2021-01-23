import io

import streamlit as st
from PIL import Image

from utils import score_input_image

BACKEND_URL = "http://fastapi:8000/segmentation"

st.title("Image quality scorer")

st.write(
    """
    Obtain quality score for any input image.
    
    Visit the URL at `:8000/docs` for bakend documentation.
    """
)

# Upload image
input_image = st.file_uploader("insert image")

# Calculate Quality Score
if st.button("Get quality score"):

    col1 = st.beta_columns(1)

    if input_image:

        # Display image
        original_image = Image.open(input_image).convert("RGB")
        
        
        # TODO: Calculate score
        score = score_input_image(original_image)
        
        col1.header("Image:")
        col1.image(original_image, use_column_width=True)

        # Display score

    else:
        st.write("Please insert an image!")
