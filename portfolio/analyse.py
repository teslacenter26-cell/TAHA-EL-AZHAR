"""Rejoue la règle sur le journal synthétique livré avec le laboratoire."""
import csv
import sqlite3
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent


def detecter(lignes):
    base = sqlite3.connect(":memory:")
    try:
        base.execute("""CREATE TABLE evenements (
            id INTEGER PRIMARY KEY, compte TEXT, ip TEXT, instant TEXT,
            resultat TEXT CHECK (resultat IN ('succes', 'echec')))""")
        base.executemany("INSERT INTO evenements VALUES (?, ?, ?, ?, ?)", lignes)
        return base.execute((DOSSIER / "detection.sql").read_text()).fetchall()
    finally:
        base.close()


if __name__ == "__main__":
    with (DOSSIER / "evenements.csv").open(newline="") as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)
        for identifiant, compte, ip, instant, echecs in detecter(lecteur):
            print(f"{instant} | {compte} | {ip} | {echecs} échecs avant réussite")
