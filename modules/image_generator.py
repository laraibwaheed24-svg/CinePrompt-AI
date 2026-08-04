import requests
from urllib.parse import quote


def generate_image(prompt):
    """
    Generate an AI image using Pollinations AI.
    """

    encoded_prompt = quote(prompt)

    image_url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    )

    return {
        "status": "success",
        "image_url": image_url,
        "prompt": prompt,
    }
