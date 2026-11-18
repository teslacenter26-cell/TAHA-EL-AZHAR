"""Rejoue la règle sur le journal synthétique livré avec le laboratoire."""
import csv
import re
import sys
from datetime import datetime
from ipaddress import ip_address
from collections.abc import Iterable, Sequence
import sqlite3
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent


COLONNES = ["id", "compte", "ip", "instant", "resultat"]


def valider(lignes: Iterable[Sequence]) -> list[tuple]:
    resultat = []
    ids = set()
    for numero, ligne in enumerate(lignes, 2):
        try:
            identifiant, compte, ip, instant, etat = ligne
            if not re.fullmatch(r"[1-9][0-9]{0,17}", str(identifiant)):
                raise ValueError
            identifiant = int(identifiant)
            if identifiant in ids or not re.fullmatch(r"[a-zA-Z0-9_.-]{1,64}", compte):
                raise ValueError
            ip = str(ip_address(ip))
            if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", instant):
                raise ValueError
            datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ")
            if etat not in {"echec", "succes"}:
                raise ValueError
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Événement invalide à la ligne {numero}.") from exc
        ids.add(identifiant)
        resultat.append((identifiant, compte, ip, instant, etat))
    return resultat


def lire(path: Path) -> list:
    with path.open(encoding="utf-8", newline="") as fichier:
        lecteur = csv.reader(fichier, strict=True)
        if next(lecteur, None) != COLONNES:
            raise ValueError("En-tête du journal invalide.")
        return list(lecteur)


def detecter(lignes: Iterable[Sequence]) -> list[tuple]:
    base = sqlite3.connect(":memory:")
    try:
        base.execute("""CREATE TABLE evenements (
            id INTEGER PRIMARY KEY, compte TEXT, ip TEXT, instant TEXT,
            resultat TEXT CHECK (resultat IN ('succes', 'echec')))""")
        base.executemany("INSERT INTO evenements VALUES (?, ?, ?, ?, ?)", valider(lignes))
        return base.execute((DOSSIER / "detection.sql").read_text()).fetchall()
    finally:
        base.close()


if __name__ == "__main__":
    try:
        for _, compte, ip, instant, echecs in detecter(lire(DOSSIER / "evenements.csv")):
            print(f"{instant} | {compte} | {ip} | {echecs} échecs avant réussite")
    except (ValueError, csv.Error, sqlite3.Error, OSError):
        sys.exit("Analyse interrompue. Vérifiez le journal et les fichiers du laboratoire.")
