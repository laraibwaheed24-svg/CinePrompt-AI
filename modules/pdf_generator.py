from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image
import os


def create_storyboard_pdf(movie):

    file_path = "CinePrompt_Storyboard.pdf"

    doc = SimpleDocTemplate(
        file_path
    )

    styles = getSampleStyleSheet()

    content = []


    # =========================
    # COVER PAGE
    # =========================

    poster_path = "movie_poster.png"

    if os.path.exists(poster_path):

        content.append(
            Image(
                poster_path,
                width=250,
                height=350
            )
        )

        content.append(
            Spacer(1, 20)
        )



    
    content.append(
        Paragraph(
            "🎬 CinePrompt AI",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 30)
    )


    content.append(
        Paragraph(
            movie["movie_title"],
            styles["Heading1"]
        )
    )

    content.append(
        Spacer(1, 20)
    )


    content.append(
        Paragraph(
            f"Genre: {movie['genre']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Duration: {movie['duration']}",
            styles["Normal"]
        )
    )


    content.append(
        Spacer(1, 20)
    )


    content.append(
        Paragraph(
            "Story Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            movie["summary"],
            styles["Normal"]
        )
    )


    content.append(
        PageBreak()
    )


    # =========================
    # SCENE PAGES
    # =========================

    content.append(
        Paragraph(
            "🎬 Movie Storyboard",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )


    for scene in movie["scenes"]:

        content.append(
            Paragraph(
                f"Scene {scene['scene_number']}: {scene['title']}",
                styles["Heading2"]
            )
        )


        content.append(
            Paragraph(
                "<b>Description:</b> " + scene["description"],
                styles["Normal"]
            )
        )


        content.append(
            Spacer(1, 10)
        )


        content.append(
            Paragraph(
                "<b>Camera Shot:</b> " + scene["camera_shot"],
                styles["Normal"]
            )
        )


        content.append(
            Paragraph(
                "<b>Narration:</b> " + scene["narration"],
                styles["Normal"]
            )
        )


        content.append(
            Spacer(1, 20)
        )


    doc.build(content)

    return file_path
