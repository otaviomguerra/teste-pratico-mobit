import streamlit as st

from frontend_utils import score_input_image

BACKEND_URL = "http://backend:8000/brisque-score"

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

    col1, _ = st.beta_columns(2)

    if input_image:
        
        # Calculate BRISQUE Score
        score = score_input_image(input_image, server_url=BACKEND_URL)
        
        col1.header("Image:")
        col1.image(input_image, use_column_width=True)
        
        col1.header("Score: ")
        col1.write(score)

    else:
        st.write("Please insert an image!")
