import re


def clean_lyrics(lyrics):
    # Remove Songtext line
    lyrics = re.sub(r"^.*Songtext zu.*$", "\n", lyrics, flags=re.MULTILINE)
    lyrics = re.sub(r"^.*Testo di.*$", "\n", lyrics, flags=re.MULTILINE)

    lyrics = re.sub(r"\[\?\]", "\n", lyrics, flags=re.MULTILINE)

    # Clean tags
    lyrics = re.sub(
        r"^(\[|\(|).*(Strophe|Stophe|Strofa|Strohe|Schtrofä|Verse|Vers).*(\]|\)|:)",
        "[Verse]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(Bridge|Brdge|Brugg).*(\]|\)|:)",
        "[Bridge]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(Pre-Chorus).*(\]|\)|:)",
        "[Pre-Chorus]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(Post-Chorus).*(\]|\)|:)",
        "[Post-Chorus]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^(\[|\(|).*((?<!-)Chorus).*(\]|\)|:)", "[Chorus]", lyrics, flags=re.MULTILINE
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(Interlude|Interludio|Instrumental|Instrumenteller Breakdown).*(\]|\)|:)",
        "[Interlude]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^(\[|\(|).*((?<!-)Hook).*(\]|\)|:)", "[Hook]", lyrics, flags=re.MULTILINE
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(Intro).*(\]|\)|:)", "[Intro]", lyrics, flags=re.MULTILINE
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(Outro|Schluss).*(\]|\)|:)", "[Outro]", lyrics, flags=re.MULTILINE
    )
    lyrics = re.sub(r"^(\[|\(|).*(Part).*(\]|\)|:)", "\n", lyrics, flags=re.MULTILINE)
    lyrics = re.sub(r"^(\[|\(|).*(Skit).*(\]|\)|:)", "\n", lyrics, flags=re.MULTILINE)
    lyrics = re.sub(
        r"^(\[|\(|).*(Post-Refrain(?!\/)|Post-Ritornello).*(\]|\)|:)",
        "[Post-Refrain]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(Pre-Refrain|Pre-Ritonello|Pre-Ritornello|Vorrefrain).*(\]|\)|:)",
        "[Pre-Refrain]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^(\[|\(|).*(?<!-)(Refrain(?!\/)|Ritonello|Ritornello|Röfrä).*(\]|\)|:)",
        "[Refrain]",
        lyrics,
        flags=re.MULTILINE,
    )
    lyrics = re.sub(
        r"^\[(?!.*Bridge.*|.*Chorus.*|.*Drop.*|.*Hook.*|.*Refrain.*|.*Interlude.*|.*Intro.*|.*Outro.*|.*Verse.*).*\]$",
        "\n",
        lyrics,
        flags=re.MULTILINE,
    )

    return lyrics.strip()
