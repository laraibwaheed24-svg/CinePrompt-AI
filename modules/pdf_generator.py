from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_storyboard_pdf(movie):

    file_path = "CinePrompt_Storyboard.pdf"

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            movie["movie_title"],
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))


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


    content.append(Spacer(1, 20))


    content.append(
        Paragraph(
            movie["summary"],
            styles["Normal"]
        )
    )


    content.append(Spacer(1, 20))


    for scene in movie["scenes"]:

        content.append(
            Paragraph(
                f"Scene {scene['scene_number']}: {scene['title']}",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                scene["description"],
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Camera Shot: {scene['camera_shot']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Narration: {scene['narration']}",
                styles["Normal"]
            )
        )

        content.append(Spacer(1, 15))


    doc.build(content)

    return file_path
