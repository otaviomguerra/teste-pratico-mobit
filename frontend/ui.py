import streamlit as st

from frontend_utils import classify_distortion, score_input_image

BACKEND_URL = "http://backend:8000/"
QUALITY_SCORE_THRESHOLD = 25

st.title("Image quality scorer and Classifier")

st.write(
    """
    Obtain quality score, generally between 0 and 100, for any input image
    and, if applicable, classify some of the most common quality problems in it.
    
    To see the project source code, please visit:
    
    https://github.com/otaviomguerra/teste-pratico-mobit

    Visit the URL at `:8000/docs` for backend(REST API) documentation.
    """
)

# Upload image
st.subheader("Insert image")
input_image = st.file_uploader("")

# Calculate Quality Score
if st.button("Evaluate image"):

    if input_image:
        
        # Calculates BRISQUE Score
        score = score_input_image(input_image, server_url=BACKEND_URL+'brisque-score') 
        
        # Check if request is valid
        if score is None:
            st.error("""Problem processing the image, please make
            sure to upload a valid image"""
            )
            st.button("Retry")
        else:
            # if valid, show results
            st.header("Input Image")
            st.image(input_image, use_column_width=True)
            st.write(f"**BRISQUE Score**: `{score}`")

            # Classify problem only if score is high enough (distorted image)
            if float(score) > QUALITY_SCORE_THRESHOLD:
                problem_label, probability = classify_distortion(
                    input_image,
                    server_url=BACKEND_URL+'classification'
                )
                st.write(f"**Problem class**: `{problem_label}`")
                st.write(f"**Probability**: `{probability} %`")
    
    else:
        st.warning("Please, insert an image!")
