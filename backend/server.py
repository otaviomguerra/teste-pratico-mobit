import io

import imquality.brisque as brisque
from fastapi import FastAPI, File
from fastapi.responses import PlainTextResponse
from PIL import Image

app = FastAPI(
    title="Quality score and 'problem' classification ",
    description="""Obtain a quality score for any given image and if it has a distortion
    classifies that distortion.""",
    version="0.1.0",
)


@app.post("/brisque-score", response_class=PlainTextResponse)
def get_brisque_score(file: bytes = File(...)):
    """Commputes the brisque score for a 
    given image.

    Parameters
    ----------
    file : bytes, optional
        Image to be scored, by default File(...)

    Returns
    -------
    str
        BRISQUE Score for the given image
    """
    input_image = Image.open(io.BytesIO(file)).convert("RGB")

    print("BRISQUE SCORE: ", str(round(brisque.score(input_image), 4)))

    return str(round(brisque.score(input_image), 4))

@app.post("/classification")
def get_distortion_class(file: bytes = File(...)):
    """Classifies image in 

    Parameters
    ----------
    file : bytes, optional
        Image file object, by default File(...)

    Returns
    -------
    str
        Distortion class
    """
    return NotImplemented
