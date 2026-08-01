import edge_tts
import asyncio
import tempfile
from gtts import gTTS
import os


async def _generate(text, voice, output):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output)


def generate_narration(text):

    output = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    asyncio.run(
        _generate(
            text,
            "en-US-JennyNeural",
            output.name
        )
    )

    return output.name
