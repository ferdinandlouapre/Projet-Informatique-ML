import re
import numpy as np
import pandas as pd
from docx import Document

document = Document()

# taille des "phrases"
n = 5


def document(texte: str):
    f = open(texte, "rb")
    doc = Document(f)
    f.close()
    return doc


def vecteur_ref(doc):
    res = []
    with open("Couleurs.docx", "rb") as f:
        color = Document(f)

    for paragraph in color.paragraphs:
        for run in paragraph.runs:
            if run.text != "":
                font = run.font
                res.append(font.color.rgb)

    with open("Surlignage.docx", "rb") as f:
        surlign = Document(f)
    for paragraphe in surlign.paragraphs:
        for run in paragraphe.runs:
            if run.text != "":
                font = run.font
                res.append(font.highlight_color)

    for paragraphe in doc.paragraphs:
        for run in paragraphe.runs:
            for mot in re.split(r"\s+", run.text):
                if mot != "" and mot not in res:
                    res.append(mot)

    return res
