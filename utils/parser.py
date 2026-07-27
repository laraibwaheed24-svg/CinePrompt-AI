import re


def parse_story(story_text):
    data = {
        "title": "",
        "genre": "",
        "duration": "",
        "characters": "",
        "summary": "",
        "scenes": []
    }

    lines = story_text.splitlines()

    current_scene = None

    for line in lines:

        line = line.strip()

        if line.startswith("Movie Title:"):
            data["title"] = line.replace("Movie Title:", "").strip()

        elif line.startswith("Genre:"):
            data["genre"] = line.replace("Genre:", "").strip()

        elif line.startswith("Estimated Duration:"):
            data["duration"] = line.replace("Estimated Duration:", "").strip()

        elif line.startswith("Main Characters:"):
            data["characters"] = ""

        elif line.startswith("Story Summary:"):
            data["summary"] = ""

        elif re.match(r"Scene \d+:", line):

            if current_scene:
                data["scenes"].append(current_scene)

            current_scene = {
                "title": "",
                "description": ""
            }

        elif line.startswith("Title:"):

            if current_scene:
                current_scene["title"] = line.replace("Title:", "").strip()

        elif line.startswith("Description:"):

            if current_scene:
                current_scene["description"] = line.replace(
                    "Description:",
                    ""
                ).strip()

        else:

            if current_scene:

                current_scene["description"] += " " + line

    if current_scene:
        data["scenes"].append(current_scene)

    return data
