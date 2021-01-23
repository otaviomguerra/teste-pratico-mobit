from json.decoder import JSONDecodeError

import requests
from PIL import UnidentifiedImageError
from requests.exceptions import ConnectionError
from requests_toolbelt.multipart.encoder import MultipartEncoder


def score_input_image(image, server_url: str):
    """Calls image quality score
    service given a input image.

    Parameters
    ----------
    image : binary
        Image object to be scored
    server_url : str
        URL of the endpoint that will
    make the scoring with the model

    Returns
    -------
    str
        Quality score between 0 and 100 returned by the
        service.
    """

    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

    response = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    try:
        response_json = response.json()
        return response_json
    except (ConnectionError, JSONDecodeError, UnidentifiedImageError):
        return None
