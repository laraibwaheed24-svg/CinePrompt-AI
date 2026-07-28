from urllib.parse import quote


def generate_movie_poster(movie):
    """
    Generate a movie poster using Pollinations AI.
    """

    characters = ", ".join(movie["characters"])

    prompt = f"""
Movie poster for "{movie['movie_title']}"

Genre: {movie['genre']}

Characters:
{characters}

Story:
{movie['summary']}

Epic cinematic movie poster,
Hollywood blockbuster,
beautiful composition,
dramatic lighting,
ultra detailed,
high quality,
4K,
movie poster,
centered title,
masterpiece.
"""

    url = (
        "https://image.pollinations.ai/prompt/"
        + quote(prompt)
        + "?width=768&height=1152&model=flux&nologo=true"
    )

    return url
